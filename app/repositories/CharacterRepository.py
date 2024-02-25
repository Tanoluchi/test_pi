from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.db import (
    get_db,
)
from app.models.CharacterModel import Character

class CharacterRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get_all(self) -> list[Character]:
        return self.db.query(Character).all()

    def get(self, id: int) -> Character:
        return self.db.query(Character).filter(Character.id == id).first()

    def create(self, character: Character) -> Character:
        self.db_character = character
        self.db.add(self.db_character)
        self.db.commit()
        self.db.refresh(self.db_character)
        return self.db_character

    def delete(self, id: int) -> None:
        self.db.query(Character).filter(Character.id == id).delete()
        self.db.commit()