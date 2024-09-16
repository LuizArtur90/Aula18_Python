import requests
from db_3 import SessionLocal, engine, Base
from model_2 import Pokemon
from schema_1 import PokemonSchema

Base.metadata.create_all(bind=engine)

#Função pegar pokemon
def fetch_pokemon_data(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    print(response)
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchema(name=data['name'], type=types)
    else:
        return None

#Função add no banco de dados
def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon
