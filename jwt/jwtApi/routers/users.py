from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from typing import List
from dependencies.di import get_service
from schemas.user_dto import UserDto
from schemas.user_request import UserRequest
from services.user_services import UserService

router=APIRouter()

@router.get("/", response_model=List[UserDto])
def list_users(service: UserService=Depends(get_service)):
    return service.find_all()


@router.get("/{user_id}", response_model=UserDto)
def get_user(user_id:int, service: UserService=Depends(get_service)):
    user=service.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="el usuario con id= {user_id} no fue encontrado")
    return user


@router.post("/", response_model=UserDto, status_code=status.HTTP_201_CREATED)
def create_user(user:UserRequest, service: UserService=Depends(get_service)):
    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))