from functools import lru_cache
from typing import Union
from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from todos import router
import config
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

origins_ejemplo = [
    "http://localhost:3000",
    "https://todo-app-blond-one-92.vercel.app/",
]

# Configuración CORS, necesaria para el desarrollo del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitir todos los orígenes (para desarrollo)
    allow_credentials=True,
    allow_methods=["*"], # Permitir todos los métodos
    allow_headers=["*"], # Permitir todas las cabeceras
)


# manejador global de excepciones http, para manejar errores
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"Error HTTP: {repr(exc)}") # Mejorado el mensaje de log
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# para usar las configuraciones
@lru_cache() # Cachea el resultado de esta función
def get_settings():
    return config.Settings()


@app.get("/", include_in_schema=False)
@app.head("/", include_in_schema=False)
def read_root(settings: config.Settings = Depends(get_settings)):
    print(f"Nombre de la app: {settings.app_name}")
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
import os
print("DATABASE_URL is:", os.environ.get("DATABASE_URL"))
