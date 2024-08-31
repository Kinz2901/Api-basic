from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies import get_db

from app.db.user import User
from app.models.user import User as UserModel
router = APIRouter()

@router.get("/all",dependencies=[Depends(get_db)])
def read_users():
    return  list(User.select().dicts())

@router.get("/{user_id}",dependencies=[Depends(get_db)])
def read_user(user_id: int):
    user = User.get_or_none(User.id == user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/",dependencies=[Depends(get_db)])
def create_user(user: UserModel):
    user = User.create(**{
        "username": user.username,
        "password": user.password
    })
    return user

@router.put("/{user_id}",dependencies=[Depends(get_db)])
def update_user(user_id: int, user: UserModel):
    User.update(**{
        "username": user.username,
        "password": user.password
    }).where(User.id == user_id).execute()


@router.delete("/{user_id}",dependencies=[Depends(get_db)])
def delete_user(user_id: int):
    User.delete().where(User.id == user_id).execute()
    


