from asyncio import gather
from typing import List

from fastapi import APIRouter, HTTPException
from starlette import responses

from schemas import (
    StandardOutput, 
    UsuarioCreateInput, 
    ErrorOutput, 
    UsuarioListOutput,
    UsuarioListaAdd,
    ListaListOutput,
    ListaItemAdd
    
)
from services import UsuarioService
from services import ListaService
from services import ItemService

usuario_router = APIRouter(prefix='/usuarios')
lista_router = APIRouter(prefix='/listas')
item_router = APIRouter(prefix='/itens')


@usuario_router.post('/cadastrar', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def cadastrar_usuario(usuario_input: UsuarioCreateInput):
    try:
        await UsuarioService.cadastrar_usuario(nome=usuario_input.nome, senha=usuario_input.senha)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@usuario_router.delete('/deletar/{usuario_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def deletar_usuario(usuario_id: int):
    try:
        await UsuarioService.deletar_usuario(usuario_id)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@usuario_router.get('/listar', response_model=List[UsuarioListOutput], responses={400: {'model': ErrorOutput}})
async def listar_usuario():
    try:
        return await UsuarioService.listar_usuario()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@lista_router.post('/cadastrar', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def usuario_lista_add(lista_add: UsuarioListaAdd):
    try:
        await ListaService.add_lista(usuario_id=lista_add.usuario_id, nome=lista_add.nome)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@lista_router.delete('/deletar/{usuario_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def usuario_lista_remove(usuario_id: int, lista_id: int):
    try:
        await ListaService.remove_lista(usuario_id=usuario_id, lista_id=lista_id) 
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@lista_router.get('/listar', response_model=List[ListaListOutput], responses={400: {'model': ErrorOutput}})
async def listar_usuario():
    try:
        return await ListaService.listar_lista()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@item_router.post('/cadastrar', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def lista_item_add(lista_add: ListaItemAdd):
    try:
        await ItemService.add_item(lista_id=lista_add.lista_id, produto=lista_add.produto, quantidade=lista_add.quantidade, preco=lista_add.preco)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@item_router.delete('/deletar/{lista_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def usuario_lista_remove(lista_id: int, item_id: int):
    try:
        await ListaService.remove_lista(lista_id=lista_id, item_id=item_id) 
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))





""" @assets_router.get('/day_summary/{user_id}', response_model=List[DaySummaryOutput], responses={400: {'model': ErrorOutput}})
async def day_summary(user_id: int):
    try:
        user = await UserService.get_by_id(user_id)
        favorites_symbols = [favorite.symbol for favorite in user.favorites]
        tasks = [AssetService.day_summary(symbol=symbol) for symbol in favorites_symbols]
        return await gather(*tasks)
    
    except Exception as error:
        raise HTTPException(400, detail=str(error)) """