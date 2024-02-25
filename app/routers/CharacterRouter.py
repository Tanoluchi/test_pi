from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.services.CharacterService import CharacterService
from app.schemas.CharacterSchema import ListCharactersSchema, CharacterSchema

CharacterRouter = APIRouter(prefix="/character", tags=["Character"])

# Get characters (GET)
@CharacterRouter.get("/getAll", status_code=status.HTTP_200_OK, response_model=ListCharactersSchema, summary="Get all characters")
def get_characters(characterService: CharacterService = Depends()):
    """
    Return a list of characters with information:
    - **id**
    - **name**
    - **height**
    - **mass**
    - **eye_color**
    - **birth_year**
    """
    characters_data = characterService.get_all()
    return ListCharactersSchema(characters=jsonable_encoder(characters_data))

# Get character by id (GET)
@CharacterRouter.get("/get/{id}", status_code=status.HTTP_200_OK, response_model=CharacterSchema, summary="Get character by id")
def get_character(id: int, characterService: CharacterService = Depends()):
    """
    Return a character by id with all information:
    - **id**
    - **name**
    - **height**
    - **mass**
    - **hair_color**
    - **skin_color**
    - **eye_color**
    - **birth_year**

    **Args**:
        id (int): The id of the character

    **Raises**:
        HTTPException: If the character is not found
    """
    if db_character := characterService.get(id):
        return CharacterSchema(**jsonable_encoder(db_character))
    raise HTTPException(status_code=400, detail=f"Character not found with id: {id}")

# Create character (POST)
@CharacterRouter.post("/add", status_code=status.HTTP_201_CREATED, response_model=CharacterSchema, summary="Create character")
def create_character(character: CharacterSchema, characterService: CharacterService = Depends()):
    """
    Create an character with all information:

    - **id**: Each character will have a unique identifier (integer)
    - **name**: Each character must have a name (string)
    - **height**: Required (integer)
    - **mass**: Required (integer)
    - **hair_color**: Required (string)
    - **skin_color**: Required (string)
    - **eye_color**: Required (string)
    - **birth_year**: Required (integer)

    **Args**:
        character (Character): The character to be created

    **Raises**:
        HTTPException: If the character already exists
    """
    if characterService.get(character.id):
        raise HTTPException(status_code=400, detail=f"Character with ID {character.id} already exists")

    create_character = characterService.create(character)
    return CharacterSchema(**jsonable_encoder(create_character))

# Delete character by id (DELETE)
@CharacterRouter.delete("/delete/{id}", status_code=status.HTTP_200_OK, summary="Delete character by id")
def delete_character(id: int, characterService: CharacterService = Depends()):
    """
    Delete a character by id

    **Args**:
        id (int): The id of the character to be deleted

    **Raises**:
        HTTPException: If the character not found

    """
    if not characterService.get(id):
        raise HTTPException(status_code=400, detail=f"Character not found with id: {id}")

    characterService.delete(id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Character deleted successfully"})