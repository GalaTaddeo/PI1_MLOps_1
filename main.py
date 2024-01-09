#http://127.0.0.1:8000

from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int

@app.get('/')
def index():
    return 'Hola Mundo'

@app.get('/libros/{id}')
def mostrar_libro(id: int):
    return {'data': id}

@app.post('/libros')
def insertar_libro(libro: Libro):
    return {f'libro {libro.titulo} insertado'}