# Importaciones
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import api_functions as af

import importlib
importlib.reload(af)

# Se instancia la aplicación
app = FastAPI()

# Funciones
@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    '''
    Página de inicio que muestra una presentación.

    Returns:
    HTMLResponse: Respuesta HTML que muestra la presentación.
    '''
    return af.presentacion()

@app.get(path = '/PlayTimeGenre',
          description = """ <font color="blue">
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el genero en el box abajo.<br>
                        3. Bajar a "Resposes" para ver el año con mas horas jugadas para dicho género.
                        </font>
                        """,
         tags=["Consultas Generales"])
def PlayTimeGenre(genero: str = Query(..., 
                                description="Género del juego", 
                                example="Action")):
        
    return af.PlayTimeGenre(genero)

@app.get(path = '/UserForGenre',
          description = """ <font color="blue">
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el genero en el box abajo.<br>
                        3. Bajar a "Resposes" para ver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
                        </font>
                        """,
         tags=["Consultas Generales"])
def UserForGenre(genero: str = Query(..., 
                                description="Género del juego", 
                                example="Casual")):
        
    return af.UserForGenre(genero)

@app.get(path = '/UsersRecommend',
          description = """ <font color="blue">
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el año en el box abajo.<br>
                        3. Bajar a "Resposes" para ver el top 3 de juegos MÁS recomendados por usuarios para el año dado.
                        </font>
                        """,
         tags=["Consultas Generales"])
def UsersRecommend(año: str = Query(..., 
                                description="Año para filtrar los juegos más recomendados", 
                                example="2017")):
        
    return af.UsersRecommend(año)

@app.get(path = '/UsersWorstDeveloper',
          description = """ <font color="blue">
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el año en el box abajo.<br>
                        3. Bajar a "Resposes" para ver el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.
                        </font>
                        """,
         tags=["Consultas Generales"])
def UsersWorstDeveloper(año: str = Query(..., 
                                description="Año para filtrar los desarrolladores con juegos menos recomendados", 
                                example="2017")):
        
    return af.UsersWorstDeveloper(año)

@app.get('/sentiment_analysis',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese la empresa desarrolladora en box abajo.<br>
                    3. Bajar a "Resposes" para ver una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
                    </font>
                    """,
         tags=["Consultas Generales"])
def sentiment_analysis(empresa_desarrolladora: str = Query(..., 
                                         description="Empresa desarrolladora de juegos", 
                                         example="Valve")):
    return af.sentiment_analysis(empresa_desarrolladora)

@app.get('/recomendacion_juego',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese el nombre de un juego en box abajo.<br>
                    3. Bajar a "Resposes" para ver los juegos recomendados.
                    </font>
                    """,
         tags=["Recomendación"])
def recomendacion_juego(game: str = Query(..., 
                                         description="Juego a partir del cuál se hace la recomendación de otros juego", 
                                         example="Killing Floor")):
    return af.recomendacion_juego(game)


@app.get('/recomendacion_usuario',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese el id del usuario en box abajo.<br>
                    3. Bajar a "Resposes" para ver los juegos recomendados para ese usuario.
                    </font>
                    """,
         tags=["Recomendación"])
def recomendacion_usuario(user: str = Query(..., 
                                         description="Usuario a partir del cuál se hace la recomendación de los juegos", 
                                         example="76561197970982479")):
    return af.recomendacion_usuario(user) 