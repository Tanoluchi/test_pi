from fastapi import Depends

from app.models.CharacterModel import Character
from app.schemas.CharacterSchema import CharacterSchema

from app.repositories.CharacterRepository import CharacterRepository

class CharacterService:
    characterRepository = CharacterRepository

    def __init__(self, characterRepository: CharacterRepository = Depends()) -> None:
        self.characterRepository = characterRepository

    def create(self, character_body: CharacterSchema) -> Character:
        "Create a new character in the database"
        return self.characterRepository.create(Character(**character_body.dict()))

    def get_all(self) -> list[Character]:
        "Get all characters in the database"
        return self.characterRepository.get_all()

    def get(self, id: int) -> Character:
        "Get a character by id in the database"
        return self.characterRepository.get(id)

    def delete(self, id: int) -> None:
        "Delete a character by id in the database"
        return self.characterRepository.delete(id)
