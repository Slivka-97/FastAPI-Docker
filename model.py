from pydantic import BaseModel


class Model(BaseModel):
    inn: int
    snn: int