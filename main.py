import io
from typing import Union
import uvicorn
from fastapi import FastAPI, UploadFile, File, Form, Body, Depends,Cookie, Header,Query, Path, Security
from pydantic import BaseModel
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()




@app.get("/")
async def face_gender_detector():
    return "successfully loaded"
