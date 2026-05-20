from fastapi import FastAPI, status, Response 
from pydantic import BaseModel
app = FastAPI()

mis_mascotas = {
   1:{
       'nombre':'baly',
       'raza':'gato' 
   },
   2:{
       'nombre':'layla',
       'raza' :'perro'
   },
   3:{
       'nombre':'pepe',
       'raza' :'cotorro'
   }
}

@app.get("/")
def hola_mundo():
    return {
        "mensaje": "hola mundo"
        }


@app.get("/mascotas/{id}")
def detalle_mascotas(id:int, response:Response):
    #CONSULTAR BASE DE DATOS
    mascota = mis_mascotas.get(id, None)
    print(mascota)
    if not mascota:
        mascota = {}
        response.status_code = status.HTTP_404_NOT_FOUND
    return mascota

class Mascota(BaseModel):
    id:int
    nombre:str
    raza:str

@app.post("/mascotas/")
def registra_mascota(mascota:Mascota):
    mis_mascotas[mascota.id] = mascota
