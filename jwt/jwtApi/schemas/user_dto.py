from pydantic import BaseModel, ConfigDict, EmailStr

class UserDto(BaseModel):
    id:int
    email: EmailStr
    is_active: bool


    model_config=ConfigDict(from_attributes=True)