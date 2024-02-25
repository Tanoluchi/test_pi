from fastapi import HTTPException
from pydantic import BaseModel, ValidationInfo, Field, field_validator
from typing import List

class CharacterSchema(BaseModel):
    id: int
    name: str = Field(min_length=2)
    height: int
    mass: int
    hair_color: str = Field(min_length=3)
    skin_color: str = Field(min_length=3)
    eye_color: str = Field(min_length=3)
    birth_year: int

    @field_validator("height", "mass", "birth_year")
    def validate_greater_zero(cls, v, info: ValidationInfo):
        if v <= 0:
            raise HTTPException(status_code=400, detail=f"Numeric fields must be greater than zero in the field: {info.field_name}")
        return v

    @field_validator("hair_color", "skin_color", "eye_color")
    def validate_field_no_numbers(cls, v, info: ValidationInfo):
        if any(char.isdigit() for char in v):
            raise HTTPException(status_code=400, detail=f"Numbers are not allowed in the field: {info.field_name}")
        return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "1",
                    "name": "Luke Skywalker",
                    "height": 172,
                    "mass": 77,
                    "hair_color": "blond",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "1998"
                }
            ]
        }
    }

class CharacterGetAllSchema(BaseModel):
    id: int
    name: str = Field(min_length=2)
    height: int
    mass: int
    eye_color: str = Field(min_length=3)
    birth_year: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "1",
                    "name": "Luke Skywalker",
                    "height": 172,
                    "mass": 77,
                    "eye_color": "blue",
                    "birth_year": "1998"
                }
            ]
        }
    }

class ListCharactersSchema(BaseModel):
    characters: List[CharacterGetAllSchema]

    model_config = {
        "json_schema_extra": {
            "characters": [
                [{
                    "id": "1",
                    "name": "Luke Skywalker",
                    "height": 172,
                    "mass": 77,
                    "eye_color": "blue",
                    "birth_year": "1998"
                },
                {
                    "id": "2",
                    "name": "C-3PO",
                    "height": 167,
                    "mass": 75,
                    "eye_color": "yellow",
                    "birth_year": "2000"
                }]
            ]
        }
    }
