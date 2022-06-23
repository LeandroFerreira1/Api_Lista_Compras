
from fastapi import FastAPI, APIRouter
from views import usuario_router,lista_router, item_router

app = FastAPI()

router = APIRouter()

@router.get('/')
def first():
    return 'Hello world!'

app.include_router(prefix='/first', router=router)
app.include_router(usuario_router)
app.include_router(lista_router)
app.include_router(item_router)
