from asyncio import gather
from typing import List

from starlette import responses
from fastapi import APIRouter, HTTPException, Response

from services import UserService, FavoriteService, AssetService

from schemas import (UserCreateInput, 
                     StandardOutput,
                     ErrorOutput,
                     UserFavoriteAddInput, 
                     UserListOutout,
                     DaySummaryOutput,
                     )


user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create',description="this is my documentation for using my api created with Python and FastAPI" ,response_model=StandardOutput, responses={400:{'model':ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
       await UserService.create_user(name=user_input.name)
       return StandardOutput(message="OK")
    except Exception as error:
        raise HTTPException(400, detail= str(error))
    

    
@user_router.delete('/delete/{user_id}',response_model=StandardOutput, responses={400:{'model':ErrorOutput}})
async def user_delete(user_id:int):
    try:
       await UserService.delete_user(user_id)
       return StandardOutput(message="OK")
    except Exception as error:
        raise HTTPException(400, detail= str(error))
    


@user_router.post('/favorite/add',response_model=StandardOutput, responses={400:{'model':ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
       await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
       return StandardOutput(message="OK")
    except Exception as error:
        raise HTTPException(400, detail= str(error))
    

@user_router.delete('/favorite/remove/{user_id}',response_model=StandardOutput, responses={400:{'model':ErrorOutput}})
async def user_favorite_remove(user_id:int, symbol:str):
    try:
       await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
       return StandardOutput(message="OK")
    except Exception as error:
        raise HTTPException(400, detail= str(error))
    

@user_router.get('/list',response_model=List[UserListOutout], responses={400:{'model':ErrorOutput}})
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail= str(error))


@assets_router.get('/day_summary/{user_id}',response_model=List[DaySummaryOutput], responses={400:{'model':ErrorOutput}})
async def days_summary(user_id:int):
    try:
        user = await UserService.get_by_id(user_id)
        favorites_symbols = [favorite.symbol for favorite in user.favorites]
        print(favorites_symbols)
        tasks = [AssetService.day_summary(symbol=symbol) for symbol in favorites_symbols]
        return await gather(*tasks)

    except Exception as error:
        raise HTTPException(400, detail= str(error))