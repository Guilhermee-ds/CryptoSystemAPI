from fastapi import APIRouter
from services import UserService  


user_router = APIRouter(perfix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create')
async def user_create():
    try:
       await UserService.create_user(name='name..')
    except:
        pass