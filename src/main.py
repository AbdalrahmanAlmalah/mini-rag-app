from fastapi import FastAPI
from routes import base, data

app = FastAPI()
# Fixed the typo here: "include_router" instead of "inculde_router"
app.include_router(base.base_router)
app.include_router(data.data_router)