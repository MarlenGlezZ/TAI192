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

#Endpoint buscar tarea especifica
@app.get('/tareas/{tarea_id}', tags=['Tareas'])
def obtener_tarea(tarea_id: int):
    tarea = next((tarea for tarea in tareas if tarea["id"] == tarea_id), None)
    if tarea:
        return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#Endpoint Crear nueva tarea
@app.post('/tarea/', tags=['Tareas'])
def agregar_tarea(tarea: dict):  # parámetro con tipo
    for t in tareas:
        if t["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="El id ya existe")
    
    tareas.append(tarea)
    return tarea

# Endpoint Actualizar una tarea existente
@app.put('/tareas/{tarea_id}', tags=['Tareas'])
def actualizar_tarea(tarea_id: int, tarea_actualizada: dict):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea.update(tarea_actualizada)
            tarea["id"] = tarea_id 
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Endpoint Eliminar una tarea
@app.delete('/tareas/{tarea_id}', tags=['Tareas'])
def eliminar_tarea(tarea_id: int):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tareas.pop(index)
            return {"mensaje": "Tarea eliminada con éxito"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")