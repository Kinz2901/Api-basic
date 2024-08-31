from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.api.routes.router import app_router
import asyncio

from dotenv import dotenv_values
config = dotenv_values(".env")

app = FastAPI()
app.include_router(app_router, prefix="/api")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config['host'], port=int(config['port']))
    
