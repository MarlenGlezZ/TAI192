from fastapi import FastAPI, HTTPException

app = FastAPI(
    title='Gestion de Tareas',
    description='API para gestionar una lista de tareas',
    version='1.0.0'
)

# Lista de tareas
tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "2024-02-14",
        "estado": "completada"
    },
    {
        "id": 2,
        "titulo": "Comprar comestibles",
        "descripcion": "Adquirir leche, pan y frutas en el supermercado",
        "vencimiento": "2024-02-16",
        "estado": "no completada"
    },
     {
        "id": 3,
        "titulo": "Hacer ejercicio",
        "descripcion": "Salir a correr 5 km en el parque",
        "vencimiento": "2024-02-15",
        "estado": "no completada"
    },
    {
        "id": 4,
        "titulo": "Preparar presentación",
        "descripcion": "Crear diapositivas para la reunión de trabajo",
        "vencimiento": "2024-02-20",
        "estado": "no completada"
    },
    {
        "id": 5,
        "titulo": "Visitar al dentista",
        "descripcion": "Consulta de revisión semestral",
        "vencimiento": "2024-02-18",
        "estado": "completada"
    },
    
    
]

#Endpoint Obtener todas las tareas
@app.get('/tareas', tags=['Tareas'])
def obtener_tareas():
    return {"tareas": tareas}