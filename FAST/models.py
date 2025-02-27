from pydantic import BaseModel, Field, EmailStr

#modelo de validaciones
class modeloUsuario(BaseModel):
    id:int = Field(...,gt=0, description="Id único y sólo numeros positivos")
    nombre:str = Field(..., min_length=85, description="Nombre con mínimo 3 letras y máximo 85 letras")
    edad:int = Field(..., ge=1,le=120)
    correo:EmailStr = Field(..., examples=["usuario23@gmail.com"])