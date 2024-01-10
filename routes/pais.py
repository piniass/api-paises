from fastapi import APIRouter, HTTPException
from config.db import conn
from models.pais import paises
from schemas.pais import Pais
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, select
from typing import List
from fastapi.encoders import jsonable_encoder
from datetime import datetime




pais = APIRouter()


@pais.get("/", response_model=List[Pais])
def get_paises():
    return conn.execute(paises.select()).fetchall()


@pais.post("/paises", response_model=Pais)
def create_pais(pais: Pais):
    try:
        new_pais = {
            "name": pais.name,
            "capital": pais.capital,
            "habitantes": pais.habitantes,
            "diaNacional": pais.diaNacional
        }        
        print(new_pais)
        result = conn.execute(paises.insert().values(new_pais))
        print(result)
        return conn.execute(paises.select().where(paises.c.id == result.lastrowid)).first()
    except SQLAlchemyError as e:
        print(f"Error durante la creación del país: {e}")
        error_message = "Error creando un país"

        

@pais.get("/paises/{id}", response_model=Pais)
def get_pais(id: int):
    try:
        return conn.execute(paises.select().where(paises.c.id == id)).first()
    except Exception as e:
        print(f"Error during pais retrieval: {e}")
        raise HTTPException(status_code=500, detail="Error, ID no encontrada")
    
@pais.delete("/paises/{id}", response_model=dict)
def delete_pais(id: int):
    delete_pais = conn.execute(paises.delete().where(paises.c.id == id))
    if delete_pais.rowcount == 0:
        raise HTTPException(status_code=404, detail="Pais no encontrado")
    return {"message": "Pais eliminado"}


@pais.put("/paises/{id}", response_model=dict)
def update_pais(pais: Pais, id: int):
    updated_pais = conn.execute(
        paises.update()
            .values(name=pais.name, capital=pais.capital, habitantes=pais.habitantes, diaNacional=pais.diaNacional)
            .where(paises.c.id == id)
    )

    if updated_pais.rowcount == 0:
        raise HTTPException(status_code=404, detail="Pais no encontrado")
    
    return {"message": "Pais actualizado correctamente"}