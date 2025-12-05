import os
from typing import Union
from fasftapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows


@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Mujer Maravilla", "Aquaman"]
    return rows

@app.get("/cursosPlatzi")
def get_cursos():
    rows = ["Docker", "Bash", "Linux", "Ingles", "Python" "Javascript", "Azure", "DevOps"]
    retorn rows