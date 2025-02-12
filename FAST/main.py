from typing import Optional
from fastapi import FastAPI, HTTPException


app = FastAPI(
    title='Mi Primer API 192',
    description='Bienvenide al intento de hacer APIs',
    version='1.0.1'
    
) 
# diccionario de objetos
usuarios = [
    {"id": 1, "nombre":"Marlen", "edad":24},
    {"id": 2, "nombre":"Tatiana", "edad":15},
    {"id": 3, "nombre":"Majencio", "edad":16},
    {"id": 4, "nombre":"Fany", "edad":27}
]

#Endpoint Home
@app.get('/',tags=['Hola Mundo'])#Asiganación del nombre del titulo
def home():
    return {'Hello': 'world FastAPI'}

#Endpoint Consulta Usuarios 
@app.get('/todosUsuarios',tags=['Operaciones CRUD'])
def leerUsuarios():
    return{"Los usuarios registrados son":usuarios}

#Endpoint Agregar nuevos /post
@app.post('/usuario/',tags=['Operaciones CRUD POST'])
def agregarUsuario(usuario:dict):# parametro con tipo
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El id ya existe")
    
    usuarios.append(usuario)
    return usuario

#Endpoint Agregar nuevos /put
@app.put('/usuario/{id}',tags=['Operaciones CRUD PUT'])
def actualizarUsuario(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    
    raise HTTPException(status_code=400, detail="El id no existe")

    