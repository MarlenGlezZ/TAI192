from fastapi import FastAPI

app = FastAPI(
    title='Mi Primer API 192',
    description='Bienvenide al intento de hacer APIs',
    version='1.0.1'
    
) 

#Endpoint Home
@app.get('/',tags=['Hola Mundo'])#Asiganación del nombre del titulo
def home():
    return {'Hello': 'world FastAPI'}

#Endpoint promedio
@app.get('/promedio', tags=['Mi calificación TAI'])
def promedio():
    return 5.2

#Endpoint parametro obligatorio
@app.get('/usuario/{id}', tags=['Parámetro Obligatorio'])
def consultaUsuario(id:int):
    #conexion a la bd
    #consulta
    return {'Se encontró el usuario':id}


