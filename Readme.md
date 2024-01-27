<p align='center'>
<img src ="https://assets.soyhenry.com/henry-landing/assets/Henry/logo-white.png">
<p>


<h1 align='center'>
 <b>PROYECTO INDIVIDUAL Nº2: Data Analyst.
</h1>


# *Siniestros viales*
### ***Introducción:***


Los siniestros viales, también conocidos como accidentes de tráfico o accidentes de tránsito, son eventos que involucran vehículos en las vías públicas y que pueden tener diversas causas, como colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques con objetos fijos o caídas de vehículos. Estos incidentes pueden tener consecuencias que van desde daños materiales hasta lesiones graves o fatales para los involucrados.

En el contexto de una ciudad como Buenos Aires, los siniestros viales pueden ser una preocupación importante debido al alto volumen de tráfico y la densidad poblacional. Estos incidentes pueden tener un impacto significativo en la seguridad de los residentes y visitantes de la ciudad, así como en la infraestructura vial y los servicios de emergencia.

Las tasas de mortalidad relacionadas con siniestros viales suelen ser un indicador crítico de la seguridad vial en una región. Estas tasas se calculan, generalmente, como el número de muertes por cada cierto número de habitantes o por cada cierta cantidad de vehículos registrados. Reducir estas tasas es un objetivo clave para mejorar la seguridad vial y proteger la vida de las personas en la ciudad.

Es importante destacar que la prevención de siniestros viales involucra medidas como la educación vial, el cumplimiento de las normas de tráfico, la infraestructura segura de carreteras y calles, así como la promoción de vehículos más seguros. El seguimiento de las estadísticas y la implementación de políticas efectivas son esenciales para abordar este problema de manera adecuada.

En Argentina, cada año mueren cerca de 4.000 personas en siniestros viales. Aunque muchas jurisdicciones han logrado disminuir la cantidad de accidentes de tránsito, esta sigue siendo la principal causa de muertes violentas en el país.
Los informes del Sistema Nacional de Información Criminal (SNIC), del Ministerio de Seguridad de la Nación, revelan que entre 2018 y 2022 se registraron 19.630 muertes en siniestros viales en todo el país. Estas cifras equivalen a 11 personas por día que resultaron víctimas fatales por accidentes de tránsito.

Solo en 2022, se contabilizaron 3.828 muertes fatales en este tipo de hechos. Los expertos en la materia indican que en Argentina es dos o tres veces más alta la probabilidad de que una persona muera en un siniestro vial que en un hecho de inseguridad delictiva.


# ***ETL & EDA*** 

Para el desarrollo de la Extracción, Transformación y posterior Carga de los datos, se observó que el dataset "homicidios.xlsx" esta anidado en varias páginas, por lo cual se procede a tener cada una en un dataframe diferente.
Luego, se recorren las diferentes columnas observando los datos y se unen ambos dataframes utilizados con la columna "ID" en común, se eliminan las columnas duplicadas y columnas irrelevantes. 

Los datos nulos estaban representados por "Sd" los cuales se refieren a "Sin Dato", por criterio personal, se eliminan o reemplazan según la columna. En nuestro análisis no encontramos datos duplicados para nuestro dataset. Tampoco no se encontraron outliers, pero sí se podría tomar como valor atípico los casos en que la víctima era el conductor de un vehículo y tenía más de 65 años de edad.

Además, se creó una nueva columna llamada "semestre" para el desarrollo de el KPI; se extrajo sólo el año de la fecha del siniestro para sumar a nuestro KPI y población; se realizó WebScrapping para obtener datos de la poblacion para cada año, por cada Comuna; se realizó Geolocalización con la librería GeoPy.GeoCoders con el objetivo de lograr obtener las coordenadas de nuestros datos faltantes en la ubicación de los accidentes, se reorganizó la columna "LUGAR_DEL_HECHO" pasando por ejemplo: Centenario Av., a su correcta forma: Av. Centenario.

***El promedio de censos realizados para obtener la población, fue realizado en base al porcentaje de crecimiento, son datos estimativos para realizar el KPI correctamente***

Luego de nuestro proceso de ETL, se procede a darle una visión gráfica a nuestros datos, para así poder observar con detenimiento los puntos a investigar y el por qué suceden los accidentes en la Ciudad Autonoma de Buenos Aires.

### Víctimas fatales según sexo. Ciudad de Buenos Aires, año 2021:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/4.png?raw=true)

### Víctimas fatales según la edad. Ciudad de Buenos Aires, año 2021:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/5.png?raw=true)

### Víctimas fatales según tipo de usuario/a de la vía. Ciudad de Buenos Aires, año 2021:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/6.png?raw=true)

### Víctimas fatales según tipo de usuario/a de la vía. Ciudad Autónoma de Buenos Aires, 2015-2021:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/7.png?raw=true)

### Víctimas fatales por tipo de usuario/a de la vía según sexo. Ciudad de Buenos Aires, año 2021:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/8.png?raw=true)

### Víctimas fatales motociclistas, peatones/as, ocupantes de automóvil según edades. Ciudad de Buenos Aires, año 2021.:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/9.png?raw=true)

### Víctimas fatales según mes de ocurrencia. Ciudad de Buenos Aires, año 2021 comparación con promedio 2015-2020:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/11.png?raw=true)

### Mapa con la ubicación de las victimas fatales. Ciudad de Buenos Aires, 2015-2020 y 2021:
![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/13.png?raw=true)



# ***KPI 1*** 

El Observatorio de Movilidad y Seguridad Vial (OMSV) nos solicitó 2 indicadores de desempeño, el primero pide como objetivo reducir en un 10% la tasa de mortalidad en la ciudad de Buenos aires, objetivo el cuál se cumple en ciertos rangos de tiempo. 

![KPI](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/KPI1%202019.png?raw=true)

Como se puede observar en la imagen, en el primer semestre de 2019 el objetivo se cumple en un -16.1% respecto al semestre anterior, logrando ampliamente el objetivo solicitado.

# ***KPI 2*** 

Nuestro indicador de desempeño número 2 solicita cumplir con la baja de mortalidad para motovehículos en un -7% respecto al año anterior.

![KPI2](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/KPI2%20en%202019.png?raw=true)

Se observa en los gráficos que el año seleccionado es 2019, el cual cumple con el objetivo propuesto triplicando el descenso de la tasa de mortalidad en un -21.31% respecto al anterior.

# ***Observaciones***

En ambos indicadores de desempeño hay puntos de observación que pueden ser analizados en profundidad. Como conclusión, se observa que los accidentes se suelen dar más en avenidas que en calles, y que las víctimas suelen ser motovehículos y peatones, ésto requiere de una inversión en infraestructura para poder lograr un tráfico más fluido, como lo es invertir en los llamados "lomos de burro" en calles o bien la instalación de semáforos en lugares donde los accidentes se den más amenudo, a su vez, instaurar consciencia en los peatones y conductores de diferentes vehículos podría ser un punto a favor en el futuro para lograr una reducción general de los siniestros de tránsito.

![Image](https://github.com/GalaTaddeo/PI2_DA/blob/main/Images/Frase.jpg?raw=true)

+ Alumna de Henry: Gala Taddeo Giménez
+ Link de Proyecto anterior: https://github.com/GalaTaddeo/PI1_MLOps_1
