from fastapi.testclient import TestClient
from app.configs.db_test import override_get_db, engine
from app.configs.db import get_db, Base

from main import app

client = TestClient(app)

app.dependency_overrides[get_db] = override_get_db

def test_create_character():
    character_data = {
        "id": 999,
        "name": "Test character",
        "height": 155,
        "mass": 22,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1999
    }
    response = client.post("/character/add", json=character_data)
    assert response.status_code == 201
    assert response.json() == character_data

def test_create_character_already_exists():
    character_data = {
        "id": 999,
        "name": "Test character",
        "height": 155,
        "mass": 22,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1999
    }
    expect_value = {"detail": f"Character with ID {character_data['id']} already exists"}
    response = client.post("/character/add", json=character_data)
    assert response.status_code == 400
    assert response.json() == expect_value

def test_create_character_with_field_value_none():
    character_data = {
        "id": 9991,
        "height": 155,
        "mass": 22,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1999
    }
    response = client.post("/character/add", json=character_data)
    data = response.json()

    assert data['detail'][0]['msg'] == "Field required"
    assert response.is_error == True
    assert response.reason_phrase == 'Unprocessable Entity'
    assert response.status_code == 422

def test_create_character_field_value_less_than_0():
    character_data = {
        "id": 9991,
        "name": "Test character",
        "height": -155,
        "mass": 22,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1999
    }
    expect_value = {"detail":"Numeric fields must be greater than zero in the field: height"}
    response = client.post("/character/add", json=character_data)
    assert response.status_code == 400
    assert response.json() == expect_value

def test_create_character_field_no_numbers():
    character_data = {
        "id": 9991,
        "name": "Test character",
        "height": 155,
        "mass": 22,
        "hair_color": "blond12",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1999
    }
    expect_value = {"detail":"Numbers are not allowed in the field: hair_color"}
    response = client.post("/character/add", json=character_data)
    assert response.status_code == 400
    assert response.json() == expect_value

def test_get_characters():
    expect_value = {
        "characters":
                [{
                    "id": 999,
                    "name": "Test character",
                    "height": 155,
                    "mass": 22,
                    "eye_color": "blue",
                    "birth_year": 1999
                }]
    }
    response = client.get("/character/getAll")
    assert response.status_code == 200
    assert response.json() == expect_value

def test_get_character():
    test_id = 999
    expect_value = {
        "id": 999,
        "name": "Test character",
        "height": 155,
        "mass": 22,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1999
    }
    response = client.get(f"/character/get/{test_id}")
    assert response.status_code == 200
    assert response.json() == expect_value

def test_get_character_not_found_id():
    test_id = 1000
    expect_value = {"detail": f"Character not found with id: {test_id}"}
    response = client.get(f"/character/get/{test_id}")
    assert response.status_code == 400
    assert response.json() == expect_value

def test_delete_character():
    test_id = 999
    expect_value = {"message": "Character deleted successfully"}
    response = client.delete(f"/character/delete/{test_id}")
    assert response.status_code == 200
    assert response.json() == expect_value

def test_delete_character_not_found_id():
    test_id = 1000
    expect_value = {"detail": f"Character not found with id: {test_id}"}
    response = client.delete(f"/character/delete/{test_id}")
    assert response.status_code == 400
    assert response.json() == expect_value

def setup():
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)

def teardown():
    # Drop the tables in the test database
    Base.metadata.drop_all(bind=engine)