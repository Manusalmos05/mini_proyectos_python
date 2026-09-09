from pydantic import BaseModel, ConfigDict, EmailStr

class UserDto(BaseModel):
    id:int
    email: EmailStr
    is_activate: bool


    model_config=ConfigDict(from_attributes=True)