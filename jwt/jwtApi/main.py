from fastapi import FastAPI, Request
from config.db import engine, Base
from routers import auth,users
import time
app= FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=['users'])
app.include_router(auth.router, prefix="/auth",tags=['auth'])


@app.middleware("http")
async def timing_middleware(request: Request, call_next):

    start_time=time.time()
    response=await call_next(request)
    process_time=time.time()-start_time
    response.headers["X-Process-Time"]=f"{process_time:.4f}s"
    print(f"{request.method} {request.url.path} -> {response.status_code}: {process_time: .4f}s")
    return response


