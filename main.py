from fastapi import FastAPI
from routers.hello import Router

app=FastAPI()
app.include_router(Router)