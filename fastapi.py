from fastapi import FastAPI
from typing import t
from enum import Enum
app = FastAPI()

@app.get('/')
def home_page():
    return ("Message : Heelo world")
# uvicorn main:app  to run the fast api app

@app.get("/items/{item_id}")
def echo(item_id : int ):
    return ({'id':item_id})

# how to restrict to certain values using enum
class ModelName(str,Enum):
    Alexnet = "ALEXNET"
    Resnet = 'RESNET'
    Lenet = "LENET"

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):
    return {'model_name' : model_name}


# file path to be passed in query..it contains / 
@app.get("files/{file_path:path}")
def read_file(file_path:str):
    return{"file_path" : file_path}


# QUERY PARAMETERS query parameters not part of path
dummy_db = [{"item_name" : "t-shirt"},{"item_name" : "t-shirt"},{"item_name" : "t-shirt"}]

@app.get("/items/")
async def read_item(skip : int =0 ,limit:int=10, optional_parameter : t.Optimoanl[int] = None):
    return dummy_db[skip : skip+limit]
##http://127.0.0.1:8000/items/        # without specifyging

##http://127.0.0.1:8000/items/?skip=0&limit=1 # specify by ? and separated by &



# POST method. the data needs to be passed in the body and not in url
from pydantic import BaseModel

class Book(BaseModel):
    name : str
    author : str
    description  : t.OPtional[str] = None
    price : float

@app.post("/books/")
def create_iem(book : Book):
    return book


#getting fastapi doc
#http://127.0.0.1:8000/doc

## uvicorn main:app --reload
#pip install uvicorn

# Get
# GET is used to request data from a specified resource.

# Note that the query string (name/value pairs) is sent in the URL of a GET request:


# The POST Method
# POST is used to send data to a server to create/update a resource.

# The data sent to the server with POST is stored in the request body of the HTTP request:

# Create NEW record =>POST
# read=>GET
# If the record exists then update else create a new record=>PUT
# update/modify=>PATCH
# delete=>DELETE


# The PUT Method
# PUT is used to send data to a server to create/update a resource.

# The difference between POST and PUT is that PUT requests are idempotent. That is, calling the same PUT request multiple times will always produce the same result. In contrast, calling a POST request repeatedly have side effects of creating the same resource multiple times.

