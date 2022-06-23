from pydantic import BaseModel
from typing import List


class UsuarioCreateInput(BaseModel):
    nome: str
    senha: str

class UsuarioListaAdd(BaseModel):
    usuario_id: int
    nome: str

class ListaItemAdd(BaseModel):
    lista_id: int
    produto: str
    quantidade: int
    preco: str

class StandardOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class Lista(BaseModel):
    id: int
    nome: str
    usuario_id: int

    class Config:
        orm_mode = True

class Item(BaseModel):
    id: int
    produto: str
    quantidade: int
    preco: str
    lista_id: int

    class Config:
        orm_mode = True

class UsuarioListOutput(BaseModel):
    id: int
    nome: str
    senha: str
    listas: List[Lista]
    
    class Config:
        orm_mode = True

class ListaListOutput(BaseModel):
    id: int
    nome: str
    usuario_id: int
    itens: List[Item]
    
    class Config:
        orm_mode = True




""" class DaySummaryOutput(BaseModel):
    highest: float
    lowest: float
    symbol: str """