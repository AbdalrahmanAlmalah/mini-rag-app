from fastapi import FastAPI
from  dotenv import load_dotenv
load_dotenv(".env")
from routes import base
app = FastAPI()
# Fixed the typo here: "include_router" instead of "inculde_router"
app.include_router(base.base_router)