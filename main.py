from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {"Olá": "Mundo"}

class Usuario(BaseModel):
    id: int
    email: str
    senha: str

base_de_dados = [
    Usuario(id=1, email="maria@maria.com", senha="maria123"),
    Usuario(id=2, email="julho@julho.com", senha="julho123"),
    Usuario(id=3, email="mario@mario.com", senha="mario123")
]

#retorna todos os usuarios
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

#retorna um usuario pelo id
@app.get("/usuarios/{id_usuario}")
def get_usuario_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    return{"Status": 404, "Mensagem": "Usuário não encontrado"}

@app.post("/usuarios")
def insert_usuario(usuario: Usuario):
    existente = False
    for base in base_de_dados:
        if(usuario.id == base.id):
            return{"Status": 404, "Mensagem": "ID existente"}
        if(usuario.email == base.email):
            return{"Status": 404, "Mensagem": "email existente"}

    base_de_dados.append(usuario)
    return{"Status": "true", "Mensagem": "Usuário inserido"}