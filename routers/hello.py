from fastapi import APIRouter
from pydantic import BaseModel

Router=APIRouter()

class helloRequest(BaseModel):
    name:str

class helloresponse(BaseModel):
    msg:str


@Router.get("/hello")
def h():
    return{
        "msg":"hello"
    }
@Router.get("/hello",response_model=helloresponse)
def hello(request:helloRequest):
    return{
        "msg":f"hello{request.name}"
    }

