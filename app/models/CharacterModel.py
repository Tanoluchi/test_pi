from app.configs.db import Base
from sqlalchemy import Column, Integer, String

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)