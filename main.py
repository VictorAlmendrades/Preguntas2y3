# Python
import json

from typing import List


# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, HTTPException
from fastapi import status
from fastapi import Body
from fastapi.param_functions import Path
from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from typing import List

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins  = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
# Models


class Libro(BaseModel):
    name: str
    category: str
    price: float
    summary: str
    author: str
    photo: float
    content: str
    

# Path Operations


## Libros
@app.post(
    path="/registrar",
    response_model=Libro,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar Libro",
    tags=["Libros"]
)
def registrar():
    pass

@app.get(
    path="/",
    response_model=List[Libro],
    status_code=status.HTTP_200_OK,
    summary="Mostrar todos los libros",
    tags=["Libros"]
)
def mostrar_libros():
    with open("libros.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results



### Show a book
@app.get(
    path="/libros/{category}",
    response_model=Libro,
    status_code=status.HTTP_200_OK,
    summary="Mostrar libro",
    tags=["Libros"]
)
def mostrar_libro_categoria(category: str): 
    with open("libros.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user['category'] == category:

                return user
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="This user doesn't exist!"
            ) 

### Delete a book
@app.delete(
    path="/libros/{name}/delete",
    response_model=Libro,
    status_code=status.HTTP_200_OK,
    summary="Eliminar un libro",
    tags=["Libros"]
)
def delete_a_book(name:str ): 
    with open("libros.json", "r", encoding="utf-8") as f:
        results = list(json.loads(f.read()))
        for libro in results:
            if libro["name"] == name:
                results.remove(libro)
                with open("libros.json", "w", encoding="utf-8") as f:
                    f.seek(0)
                    f.write(json.dumps(results))
                return libro
    if 1==1:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Libro no existe ;("
        )

### Update a libro

@app.put(
    path="/libros/{name}/update",
    response_model=Libro,
    status_code=status.HTTP_200_OK,
    summary="Actualizar un libro",
    tags=["Libros"]
)
def Update_a_book(
    name:str=Path(...), 
    libro:Libro=Body(...)
    ):
    name = str(name)
    libro_dict = libro.dict()
    libro_dict["name"] = str(libro_dict["name"])
    libro_dict["category"] = str(libro_dict["category"])
    libro_dict["price"] = float(libro_dict["price"])
    libro_dict["summary"] = str (libro_dict["summary"])
    libro_dict["author"] = str (libro_dict["author"])
    libro_dict["photo"] = float (libro_dict["photo"])
    libro_dict["content"] = str (libro_dict["content"])
    
    with open("libros.json", "r", encoding="utf-8") as f: 
        results = list(json.loads(f.read()))
        for libro in results:
            if libro["name"] == name:
                results[results.index(libro)] = libro_dict
                with open("libros.json", "w", encoding="utf-8") as f:
                    f.seek(0)
                    f.write(json.dumps(results))
                return libro    