from pydantic import BaseModel, Field, EmailStr

#modelo de validaciones
class modeloUsuario(BaseModel):
    id:int = Field(...,gt=0, description="Id único y sólo numeros positivos")
    nombre:str = Field(..., min_length=85, description="Nombre con mínimo 3 letras y máximo 85 letras")
    edad:int = Field(..., ge=1,le=120, description="Edad entre 1 y 121 años")
    correo:EmailStr = Field(...,description="correo electronico", example="usuario23@gmail.com")

#modelo de autenticación    
class modeloAuth(BaseModel):
    correo:EmailStr = Field(...,description="correo electronico", example="usuario23@gmail.com")
    passw:str=Field(...,min_length=8, strip_whitespace=True, description="Contraseña min 8 caracteres")
    