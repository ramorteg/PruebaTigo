from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import json
import sqlite3

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/prueba/")
async def hola():
    return {"message": "Hello World"}


@app.get("/prueba2/")
async def hola2():
    return "Hola"


class Item(BaseModel):
    nombre: str
    precio: float


@app.post("/items/")
async def crear_item(item: Item):
    return {"mensaje": "Item creado exitosamente"}


@app.post("/getItems/")
async def get_items():
    # conn = sqlite3.connect('C:/Users/ramor/PycharmProjects/djangoProject/ExampleTIGO/db.sqlite3')
    conn = sqlite3.connect('../db.sqlite3')
    columns = ['id','date','measure','element','server']

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM graphs_measure order by date desc")
    rows = cursor.fetchall()
    conn.close()
    json_data = json.dumps(rows)
    # return json_data
    return JSONResponse(content={'columnas': columns, 'datos': rows})

    # {"mensaje": "Item creado exitosamente"}
