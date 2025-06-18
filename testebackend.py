from fastapi import FastAPI 
from pydantic import BaseModel
from typing import List

app= FastAPI()

@app.get('/')
def welcome():
    return{'message':'Welcome to my FastAPI application'}

class Usuario(BaseModel):
    id: int
    name:str

usuarios=[]

@app.get("/usuarios", response_model=List[Usuario])
async def read_usuarios():
    return usuarios
    
@app.post("/usuarios", response_model=Usuario)
async def create_usuario(usuario: Usuario): # type: ignore
        usuario.append(Usuario)
        return usuario
    
@app.delete("/usuarios/{usuarios_id}")
async def delete_usuario(usuarios_id: int):
        del Usuario[usuarios_id]
        return{"message": "Usuario deleted"}