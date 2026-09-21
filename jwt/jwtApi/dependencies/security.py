from fastapi import  Request
from entities.user import User as UserEntity

def get_current_user(request: Request)->UserEntity:
    
    user: UserEntity=request.state.user
    return user

    