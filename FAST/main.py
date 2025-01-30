from typing import Optional
from fastapi import FastAPI

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

#Endpoint con parametro opcional
@app.get('/usuario/', tags=['Parámetro Opcional']) #Sólo se deja la diagonal para indicar que lleva algo de forma opcional
def consultaUsuario2(id: Optional[int] = None): 
    
    #validaciones con el diccionario
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {"Mensaje": "Usuario Encontrado", "usuario":usu}
            
        return {"Mensaje":f"No se encontró usuario con id : {id}"}
    else:
        return {"Mensaje":"No se proporcionó un id"}
        
    


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
        
    


