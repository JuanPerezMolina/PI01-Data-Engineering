from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd

app = FastAPI()

class Pelicula(BaseModel):
    titulo: str
    director: str
    fecha_lanzamiento: Optional[str]
    duracion: int

# http://127.0.0.1:8000
@app.get('/')
def index():
    return('Gracias por usar esta API para consultar las plataformas de películas')

@app.get('/get_word_count/{plataforma} {keyword}')
def get_word_count(plataforma, keyword):
    ''' 
    Esta función cuenta la cantidad de veces que aparece una keyword en el
    título de peliculas/series, por plataforma
    '''
    df_movies = pd.read_csv('..\Datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Crear un dataframe solo con los registros de la plataforma indicada
    df_plataforma= df_movies[df_movies['title'].str[0] == id_plataforma] 
    # Contamos el numero de veces que aparece la palabra clave en la columna titulo
    cantidad = int(df_plataforma['title'].str.count(keyword).sum())
    return{'Cantidad':cantidad}

@app.get('/get_score_count/{plataforma} {score} {anno}')
def get_score_count(plataforma, score, anno):
    ''' 
    Esta función cuenta la cantidad de películas por plataforma con un puntaje 
    mayor a score en determinado año
    '''
    df_movies = pd.read_csv('..\Datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Creaamos un dataframe df_plataforma solo con los registros de la plataforma indicada
    df_plataforma = df_movies[df_movies['id'].str[0] == id_plataforma] 
    # Creamos un df_filtered solo con las condiciones solicitadas
    df_filtered = df_plataforma[(df_plataforma['score'] > score)&(df_plataforma['release_year']==anno)] 
    #Contamos el numero de registros del dataframe que cumple todas las condiciones
    cantidad= df_filtered.shape[0]
    return{'Cantidad':cantidad}


@app.get('/get_second_score/{plataforma}')
def get_second_score(plataforma):
    ''' 
    Esta función indica la segunda película con mayor score 
    para una plataforma determinada, según el orden alfabético de los títulos
    '''
    df_movies = pd.read_csv('..\Datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Creamos un dataframe df_plataforma solo con los registros de la plataforma indicada
    df_plataforma = df_movies[df_movies['id'].str[0] == id_plataforma] 
    # Ordenamos  df_plataforma desendentemente por las columnas score y titulo 
    df_plataforma = df_plataforma.sort_values(by=['score', 'title'], ascending=[False, True])
    segunda_pelicula = df_plataforma.iloc[1, df_plataforma.columns.get_loc('title')]
    return{'Segunda pelicula con mayor escore':segunda_pelicula}


@app.get('/get_longest/{plataforma} {tipo_duracion} {anno}')
def get_longest(plataforma, tipo_duracion, anno):
    ''' 
    Esta función indica la película que más duró según: año, plataforma y tipo de duración 
    '''
    df_movies = pd.read_csv('..\Datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Creamos un dataframe df_plataforma solo con los registros de la plataforma indicada
    df_plataforma = df_movies[df_movies['id'].str[0] == id_plataforma] 
    # Creamos un df_filtered solo con las condiciones solicitadas
    df_filtered = df_plataforma[(df_plataforma['duration_type']==tipo_duracion)&(df_plataforma['release_year']==anno)] 
    # Ordenamos  df_filtered desendentemente por la columna duration_int 
    df_filtered = df_filtered.sort_values(by=['duration_int'], ascending=[False])
    pelicula_larga = df_filtered.iloc[0, df_filtered.columns.get_loc('title')]
    
    return{'Pelicula que mas duró':pelicula_larga}


@app.get('/get_rating_count/{clasificacion}')
def get_rating_count(clasificacion):
    ''' 
    Esta función cuenta la cantidad de series y películas por rating 
    '''
    df_movies = pd.read_csv('..\Datasets\movies.csv')
    # Crear un dataframe solo con los registros del rating (clasificacion) indicado
    df_rating= df_movies[df_movies['rating'] == clasificacion]
    #Contamos el numero de registros del dataframe que cumple todas las condiciones
    cantidad= int(df_rating.shape[0])
    return{'Cantidad':cantidad}

