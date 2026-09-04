from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import messages

app=FastAPI()

app.include_router(messages.router, prefix="/messages", tags=["messages"])

@app.get('/')
async def read_data():
    return {
        "mensage": "Tercera API REST con Python + FastAPI"
    } 

#Errores personalizados para la validación de datos
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    custom_errors=[]
    for error in exc.errors():
        loc=error.get('loc', [])
        field_name=loc[-1] if loc else 'Null'

        custom_errors.append({
            "message": error.get('msg', 'Error de validación'),
            "field": str(field_name),
            "type": error.get('type', 'validation_error')
        })
    return JSONResponse(status_code=422, 
                        content={"errors": custom_errors})