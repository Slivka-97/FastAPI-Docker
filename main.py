from fastapi import FastAPI
from model import Model
app = FastAPI()


@app.get('/api/{age:int}')
async def main(age: int, name: str = 'dd'):
    return {'message': f'Hello {age}--{name}'}


@app.post('/api/post/')
async def new(model: Model):
    return model