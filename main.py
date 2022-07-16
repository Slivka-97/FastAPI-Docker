from fastapi import FastAPI
from model import Model
app = FastAPI()


@app.get('/')
async def main():
    return {'Hello'}


@app.post('/api/post/')
async def new(model: Model):
    return model