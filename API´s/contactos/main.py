from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get(
    "/",
    status_code=202,
    summary ="Endpoint Raiz",
    description="Bienvenido a la API de Agenda")
async def get_root():
    response = {
        "message": "API de la Agenda",
        "datetime": "12/02/2026 10:35:45"
        }
    return response

@app.get (
    "/v1/contactos",
    status_code= 202,
    summary = "Endpoint que regresa los contactos paginados",
    description= """Regresa los contactos paginados,utilizando los siguientes QUERY PARAMS:
    limit:int -> indica el numero de regsitros a regresar
    skip:int -> indica el numero de registros a omitir"""
)
async def get_contactos(skip: int = 40, limit: int = 50):
    response = {
        {"table":"contactos",
         "items": [
            {"id_contacto": 1,
            "nombre": "Itzel",
            "email": "owo@gmail.com",
            "telefono": "1111111"},
            {"id_contacto": 2,
            "nombre": "Chris",
            "email": "uwu@gmail.com",
            "telefono": "22222"},
            ],"count":2,
            "datetime": "12/02/2026 10:28:2026",
            "message":"Datos consultados exitosamente",
            "limit":limit,
            "skip":skip}
    }
    return response