
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

# <h1 align=center> **Introducción** </h1>

En este proyecto de Machine Learning, abordamos tres etapas esenciales. Comienza con la Preparación, la Exploración y Transformación de Datos, luego el Análisis exploratorio de datos (EDA) y finalmente la Aplicación de Técnicas de Machine Learning, donde se lleva a cabo la exploración y entrenamiento del modelo.

El proyecto se basa en un conjunto de datos relacionado con los juegos de la plataforma Steam.

# <h1 align=center> **Descripción** </h1>

En la primera etapa, asumimos el rol de Data Engineer y comenzamos el proceso de Extracción, Transformación y Carga (ETL). Durante esta fase, nos enfocamos en la limpieza de datos de los tres conjuntos de datos, eliminando valores nulos, creando una nueva columna llamada "sentiment_analysis" basada en la columna "recommend", y descartando columnas irrelevantes. Esto nos permitió preparar los datos para la siguiente fase.

A continuación, comenzamos la preparación de datos al crear funciones específicas para construir una API utilizando FastAPI. Esta API facilitará la interacción eficiente con nuestros datos y se alojará en un servidor web de Render para simplificar el acceso y la consulta de información valiosa. Hemos diseñado consultas especializadas para obtener datos como: la cantidad de ítems o el porcentaje de recomendación basado en revisiones, también exploraremos los tres desarrolladores con juegos más recomendados por los usuarios para un año específico. 

Nuestra próxima etapa se centra en explorar y transformar los datos. Durante esta fase, nos enfocamos en la limpieza y exploración de los datos, preparándolos para futuras predicciones. Utilizamos el Análisis Exploratorio de Datos (EDA) como nuestra herramienta clave para comprender las relaciones entre variables y detectar posibles patrones e irregularidades. 

Finalmente, llegamos a la creación de un modelo predictivo. Entrenamos un algoritmo de aprendizaje automático que se dedica a recomendar juegos, ya sea por elemento o usuario, utilizando técnicas de recomendación con la biblioteca "surprise", diseñada específicamente para sistemas de recomendación y filtrado colaborativo.

Además, reconocemos la importancia de comunicar nuestros resultados de manera efectiva. Por lo tanto, hemos preparado un video que demuestra cómo funcionan las funciones contenidas en el endpoint de la API, lo que facilitará la comprensión y el acceso a nuestros avances.


# <h1 align=center> **Links de utilidad** </h1>

➮ [Link a Render](https://) <br>
➮ [Link al Video](https://) <br>

# <h1 align=center> **Desarrollo Fast API** </h1>

**`Desarrollo API`**: Se disponibilizan las siguientes funciones de consulta a traves de FastAPI:


+ def **PlayTimeGenre( *`genero` : str* )**:
    Devuelve el `año` con mas horas jugadas para dicho género.


+ def **UserForGenre( *`genero` : str* )**:
    Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.


+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. 


+ def **UsersWorstDeveloper( *`año` : int* )**:
   Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. 


+ def **sentiment_analysis( *`empresa desarrolladora` : str* )**:
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 


<br/>

**`Deployment`**: Se desplegó la API con Render para poder ser consumida desde la web.

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

En esta fase del proyecto, después de haber limpiado los datos, se llevaron a cabo investigaciones para comprender las relaciones entre las variables del conjunto de datos. Se buscó identificar outliers o anomalías, que no necesariamente son errores, y se detectaron patrones interesantes que podrían ser explorados en análisis posteriores. En esta ocasión, se realizó un EDA de manera manual, sin el uso de bibliotecas automatizadas, con el objetivo de aplicar los conceptos y tareas involucradas en este proceso. Finalmente, se realizó un análisis para estudiar la distribución de los datos en cada columna y la relación entre ellas a través de gráficos.


**`Modelo de predicción`**: 

La data es consumible por la API, está lista para ser utilizada por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso. Se realizaron dos propuestas de trabajo: En la primera, el modelo tiene  una relación ítem-ítem, esto es se toma un item, en base a que tan similar es ese ítem al resto, se recomiendan similares. Aca el input es un juego y el output es una lista de juegos recomendados, para ello se aplico la similitud del coseno. 
La otra propuesta para el sistema de recomendación aplica el filtro user-item, esto es tomar un usuario, se encuentran usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron. En este caso el input es un usuario y el output es una lista de juegos que se le recomienda a ese usuario. 