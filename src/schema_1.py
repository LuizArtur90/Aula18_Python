#minha view utilizando pydantic
#Importando modelos base do pydantic
from pydantic import BaseModel

#Criando uma classe utilizando BaseModel.
class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True