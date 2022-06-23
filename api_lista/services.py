
from aiohttp import ClientSession
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete

from database.models import Usuario
from database.models import Lista
from database.models import Item
from database.connection import async_session


class UsuarioService:
    async def cadastrar_usuario(nome: str, senha: str):
        async with async_session() as session:
            session.add(Usuario(nome=nome, senha=senha))
            await session.commit()

    async def deletar_usuario(usuario_id: int):
        async with async_session() as session:
            await session.execute(delete(Usuario).where(Usuario.id==usuario_id))
            await session.commit()

    async def listar_usuario():
        async with async_session() as session:
            result = await session.execute(select(Usuario))
            return result.scalars().all()
    
    async def get_by_id(usuario_id):
        async with async_session() as session:
            result = await session.execute(select(Usuario).where(Usuario.id==usuario_id))
            return result.scalar()


class ListaService:
    async def add_lista(usuario_id: int, nome: str):
        async with async_session() as session:
            session.add(Lista(usuario_id=usuario_id, nome=nome))
            await session.commit()

    async def remove_lista(usuario_id: int, lista_id: int):
        async with async_session() as session:
            await session.execute(delete(Lista).where(Lista.usuario_id==usuario_id, Lista.id==lista_id))
            await session.commit()

    async def listar_lista():
        async with async_session() as session:
            result = await session.execute(select(Lista))
            return result.scalars().all()

class ItemService:
    async def add_item(lista_id: int, produto: str, quantidade: int, preco: str):
        async with async_session() as session:
            session.add(Item(lista_id=lista_id, produto=produto, quantidade=quantidade, preco=preco))
            await session.commit()

    async def remove_item(lista_id: int, item_id: int):
        async with async_session() as session:
            await session.execute(delete(Item).where(Item.lista_id==lista_id, Item.id==item_id))
            await session.commit()

""" class AssetService:
    async def day_summary(symbol: str):
        async with ClientSession() as session:
            yesterday = date.today() - timedelta(days=1)
            url = f'https://www.mercadobitcoin.net/api/{symbol}/day-summary/{yesterday.year}/{yesterday.month}/{yesterday.day}/'
            response = await session.get(url)
            data = await response.json()
            return {
                'highest': data['highest'],
                'lowest': data['lowest'],
                'symbol': symbol
            } """