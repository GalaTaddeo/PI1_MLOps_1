## FUNCIONES A UTILIZAR:

# Importaciones
import pandas as pd
import operator
import rarfile
import os

# Especifica la ruta completa al ejecutable de WinRAR
rarfile.UNRAR_TOOL = "C:/Program Files/WinRAR/"

def extract_rar(rar_path, extracted_path):
    with rarfile.RarFile(rar_path, 'r') as rar:
        rar.extractall(extracted_path)

rar_path = 'datasets/data/parquet/df_items.rar'
extracted_path = 'datasets/data/parquet/'

extract_rar(rar_path, extracted_path)

ruta_archivo_extraido1 = os.path.join(extracted_path, 'df_items.parquet')
df_items = pd.read_parquet(ruta_archivo_extraido1)

# Repite el proceso para el segundo archivo RAR
rar_path2 = 'datasets/data/parquet/user_sim_df.rar'
extract_rar(rar_path2, extracted_path)

ruta_archivo_extraido2 = os.path.join(extracted_path, 'user_sim_df.parquet')
user_sim_df = pd.read_parquet(ruta_archivo_extraido2)



# Datos a utilizar
df_reviews = pd.read_parquet('datasets/data/parquet/df_reviews.parquet')
df_juegos = pd.read_parquet('datasets/data/parquet/df_games.parquet')
piv_norm = pd.read_parquet('datasets/data/parquet/piv_norm.parquet')
item_sim_df = pd.read_parquet('datasets/data/parquet/item_sim_df.parquet')


def presentacion():
    '''
    Genera una página de presentación HTML para la API de consultas de videojuegos.
    
    Returns:
    str: Código HTML que muestra la página de presentación.
    '''
    return '''
    <html>
        <head>
            <title>API Steam</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>API de consultas de videojuegos SteamGames</h1>
            <p>En esta API podrás hacer diferentes consultas sobre la plataforma de videojuegos.</p>
            <p>INSTRUCCIONES:</p>
            <p>Escribir <span style="background-color: lightgray;">/docs</span> a continuación de la URL actual para realizar consultas en la API</p>
            <p> El desarrollo de este proyecto esta en <a href="https://github.com/GalaTaddeo/PI1_MLOps_1.git"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
        </body>
    </html>
    '''

def PlayTimeGenre(genero):
    '''
    Ésta función 'PlayTimeGenre' debe devolver el año con mas horas jugadas para dicho género.
    '''
    # Se filtra el DataFrame de juegos por el género dado
    juegos_genero = df_juegos[df_juegos['genres'].str.contains(genero)]

    # Se combinan los DataFrames de juegos y items en función del id
    df_combinado = pd.merge(df_items, juegos_genero, left_on='item_id', right_on='id')

    # Se encuentra el año con más horas jugadas para el género dado
    year_most_played = df_combinado.groupby('release_anio')['playtime_forever'].sum().idxmax()

    return {"Año de lanzamiento con más horas jugadas para " + genero: year_most_played}

def UserForGenre(genero):
    '''
    Ésta función 'UserForGenre' debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
    '''
    # Se filtra el DataFrame de juegos por el género dado
    juegos_genero = df_juegos[df_juegos['genres'].str.contains(genero)]

    # Se combinan los DataFrames de juegos y items en función del id
    df_combinado = pd.merge(df_items, juegos_genero, left_on='item_id', right_on='id')

    # Se encuentra el usuario con más horas jugadas para el género dado
    user_most_played = df_combinado.groupby('user_id')['playtime_forever'].sum().idxmax()

    # Se acumulan las horas jugadas por año para el usuario más activo en ese género
    horas_por_anio = df_combinado[df_combinado['user_id'] == user_most_played].groupby('release_anio')['playtime_forever'].sum().reset_index()
    lista_horas_anio = [{"Año": year, "Horas": hours} for year, hours in zip(horas_por_anio['release_anio'], horas_por_anio['playtime_forever'])]

    return {"Usuario con más horas jugadas para " + genero: user_most_played, "Horas jugadas": lista_horas_anio}

def UsersRecommend(año):
    '''
    Ésta función 'UsersRecommend' devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.
    '''
    # Se filtran las reviews para el año dado y que sean positivas o neutrales
    reviews_año = df_reviews[df_reviews['release_anio'] == año]
    reviews_positivas_neutrales = reviews_año[reviews_año['sentiment_analysis'] >= 1]

    # Se cuentan las recomendaciones por juego
    recomendaciones_por_juego = reviews_positivas_neutrales[reviews_positivas_neutrales['reviews_recommend'] == True]['title'].value_counts().reset_index()
    recomendaciones_por_juego.columns = ['Juego', 'reviews_recommend']

    # Se obtiene el top 3 de juegos más recomendados
    top_3_juegos = recomendaciones_por_juego.head(3).to_dict('records')

    return [{"Puesto " + str(idx + 1): juego} for idx, juego in enumerate(top_3_juegos)]

def UsersWorstDeveloper(año):
    '''
    Ésta función 'UsersWorstDeveloper' devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.
    '''
    # Se filtran las reviews para el año dado, que sean negativas y no recomendadas
    reviews_año = df_reviews[df_reviews['release_anio'] == año]
    reviews_negativas_no_recomendadas = reviews_año[(reviews_año['sentiment_analysis'] == 0) & (reviews_año['reviews_recommend'] == False)]

    # Se cuentan las recomendaciones por desarrollador
    recomendaciones_por_desarrollador = reviews_negativas_no_recomendadas['developer'].value_counts().reset_index()
    recomendaciones_por_desarrollador.columns = ['Desarrollador', 'Count']

    # Se obtiene el top 3 de desarrolladoras con menos recomendaciones negativas
    top_3_desarrolladoras = recomendaciones_por_desarrollador.tail(3).to_dict('records')

    return [{"Puesto " + str(idx + 1): desarrollador} for idx, desarrollador in enumerate(top_3_desarrolladoras)]

def sentiment_analysis(empresa_desarrolladora):
    '''
    Ésta función 'sentiment_analysis' según la empresa desarrolladora, devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
    '''
    # Se transforman los valores de 'sentiment_analysis' a las categorías de sentimientos
    mapeo_sentimientos = {0: 'Negativo', 1: 'Neutral', 2: 'Positivo'}
    df_reviews['sentiment_analysis'] = df_reviews['sentiment_analysis'].map(mapeo_sentimientos)

    # Se filtran las reviews por la empresa desarrolladora dada
    reviews_empresa = df_reviews[df_reviews['developer'] == empresa_desarrolladora]

    # Se cuenta el número de reviews en cada categoría de análisis de sentimientos
    conteo_sentimientos = reviews_empresa['sentiment_analysis'].value_counts().to_dict()

    # Se crea el diccionario de salida
    salida = {empresa_desarrolladora: conteo_sentimientos}

    return salida

def recomendacion_juego(game):
    '''
    Ésta función devuelve una recomendación de 5 juegos en función de un juego dado, teniendo en cuenta los valores más altos de similitud del coseno. 
    '''
    # Se obtiene la lista de juegos similares ordenados
    similar_games = item_sim_df.sort_values(by=game, ascending=False).iloc[1:6]

    count = 1
    contador = 1
    recomendaciones = {}
    
    for item in similar_games:
        if contador <= 5:
            item = str(item)
            recomendaciones[count] = item
            count += 1
            contador += 1 
        else:
            break
    return recomendaciones
        
def recomendacion_usuario(user):
    '''
    Ésta función genera una lista de 5 juegos recomendados para un usuario en función de las calificaciones de usuarios similares. Los juegos que son más frecuentemente recomendados por usuarios similares se consideran como las principales recomendaciones para ese usuario.
    '''
    # Se verifica si el usuario está presente en las columnas de piv_norm (si no está, devuelve un mensaje)
    if user not in piv_norm.columns:
        return('No data available on user {}'.format(user))
    
    # Se obtienen los usuarios más similares al usuario dado
    sim_users = user_sim_df.sort_values(by=user, ascending=False).index[1:11]
    
    best = [] # Lista para almacenar los juegos mejor calificados por usuarios similares
    most_common = {} # Diccionario para contar cuántas veces se recomienda cada juego
    
    # Para cada usuario similar, se encuentra el juego mejor calificado y se agrega a la lista 'best'
    for i in sim_users:
        i = str(i)
        max_score = piv_norm.loc[:, i].max()
        best.append(piv_norm[piv_norm.loc[:, i]==max_score].index.tolist())
    
    #   Se cuenta cuántas veces se recomienda cada juego
    for i in range(len(best)):
        for j in best[i]:
            if j in most_common:
                most_common[j] += 1
            else:
                most_common[j] = 1
    
    # Se ordenan los juegos por la frecuencia de recomendación en orden descendente
    sorted_list = sorted(most_common.items(), key=operator.itemgetter(1), reverse=True)
    recomendaciones = {} 
    contador = 1 
    # Se devuelven los 5 juegos más recomendados
    for juego, _ in sorted_list:
        if contador <= 5:
            recomendaciones[contador] = juego 
            contador += 1 
        else:
            break
    
    return recomendaciones 