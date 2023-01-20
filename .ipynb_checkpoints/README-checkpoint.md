<p align=center><img src=https://media.istockphoto.com/id/1361894912/es/vector/extracci%C3%B3n-transformaci%C3%B3n-y-carga-de-datos.jpg?s=612x612&w=is&k=20&c=2BN9qDMLJ8avedxayE-TKJu3tWU1X2aTwCHzq0AndHA=><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>
## <h1 align=center>**`Juan Jose Perez`**</h1>



¡Bienvenidos a mi primer proyecto individual de la etapa de labs! Mi nombre es Juan Jose Pérez y presento en mi trabajo el rol de un ***Data Engineer***.  

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Se requiere realizar una proceso de ETL (Extracción, Transformación y Carga) de datos a partir de cuatro archivos en formato csv. Estos archivos poseen la misma estructura de campos lo cual permite unirlos en un solo archivo luego de realizar todas las transformaciones que son requeridas por el area de Analisi de datos de la empresa, estos datos seran  disponibilizados  mediante la elaboración y ejecución de una API.



## Rol a desarrollar

Como parte del equipo de data de la empresa, el área de análisis de datos le solicita al área de Data Engineering al que pertenesco ciertos requerimientos para el óptimo desarrollo de las actividades de analisis. 



## **Procedimento**

**`Transformaciones`**:  El analista de datos requiere estas transformaciones para sus datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:  Para disponibilizar los datos la empresa usa el framework ***FastAPI***. El analista de datos requiere consultar:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating
<br/>


**`Deployment`**: La empresa suele usar Deta  para realizar el deploy de sus aplicaciones.
<br/>

<br/>

**`Video`**: El Tech Lead que solicitó esta tarea pidió que sintetice en un video de ***5 minutos*** mi trabajo resaltando cómo este ayuda a los analistas de datos. Ver [aqui](https://fnhfue.deta.dev/) el video sobre el trabajo)


<br/>

## **Criterios de evaluación**

**`Código`**: El codigo esta bien documentado en dos archivos: el archivo **transformaciones.ipynb** que es un notebook que contiene cada uno de los pasos para realizar las transformaciones requeridas sobre los datos brutos (esta ubicado en el directorio raiz) y el archivo **main.py** que implementa las consultas que luego alimentan a la API (ubicado en el directorio fastapi), ambos archivos estan bien documentados. 

**`Repositorio`**: El link del repositorio engithub esta [aqui](https://github.com/gurufractal/PI01-Data-Engineering.git) 

**`url de la API`**: El link para hacer el deploy de la API que desarrolle esta [aqui](https://fnhfue.deta.dev/)



<br/>

