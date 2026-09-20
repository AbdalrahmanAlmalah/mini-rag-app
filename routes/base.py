from fastapi import FastAPI, APIRouter
import os 


base_router = APIRouter(prefix="/api/v1")
@base_router.get("/")
def welcome():
    app_name= os.getenv("APP_NAME")
    app_version=os.getenv("APP_VERSTION")
    return{
        "message": "HI  " +app_name + " Im verstion: "+ app_version 
    }