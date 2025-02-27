from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from modelsPydantic import modeloUsuario, modeloAuth
from gentoken import createToken

app = FastAPI(
    title='Mi Primer API 192',
    description='Bienvenide al intento de hacer APIs',
    version='1.0.1'
    
) 
   
# diccionario de objetos
usuarios = [
    {"id": 1, "nombre":"Marlen", "edad":24, "correo":"example1@example.com"},
    {"id": 2, "nombre":"Tatiana", "edad":15, "correo":"example2@example.com"},
    {"id": 3, "nombre":"Majencio", "edad":16, "correo":"example3@example.com"},
    {"id": 4, "nombre":"Fany", "edad":27, "correo":"example4@example.com"}
]

#Endpoint Home
@app.get('/',tags=['Hola Mundo'])#Asiganación del nombre del titulo
def home():
    return {'Hello': 'world FastAPI'}

#Endpooint Autenticación
@app.post('/auth/', tags=['Autentificacion'])
def login(autorizacion:modeloAuth):
    if autorizacion.correo=='usuario23@gmail.com' and autorizacion.passw=='123456789':
        token:str= createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso": "usuario NO autorizado"}

#Endpoint Consulta Usuarios 
@app.get('/todosUsuarios', response_model=List[modeloUsuario], tags=['Operaciones CRUD'])
def leerUsuarios():
    return{"Los usuarios registrados son":usuarios}

#Endpoint Agregar nuevos /post
@app.post('/usuario/',response_model=modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El id ya existe")
    
    usuarios.append(usuario)
    return usuario

#Endpoint Actualizar
@app.put('/usuario/{id}',response_model=modeloUsuario,tags=['Operaciones CRUD'])
def actualizarUsuario(id:int, usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El id no existe")


#Endpoint Delete
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminarUsuario(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"mensaje": "Usuario eliminado con éxito"}
    
    raise HTTPException(status_code=400, detail="El id no existe, ya fue eliminado")

    