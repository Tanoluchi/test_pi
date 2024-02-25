Challenge Python PI
====================
Repositorio para evaluación de la empresa PI Consulting.

Requirements
============

- Python (3.10)
- fastapi (0.109.2)
- uvicorn (0.27.1)
- sqlalchemy (2.0.27)
- httpx (0.27.0)
- pytest (8.0.1)

Run locally
===================

Clone the project

```bash
  git clone https://github.com/Tanoluchi/test_pi
```

Go to the project directory

```bash
  cd test_pi
```

Creating a local virtualenv
```sh
python3.10 -m venv .venv && source .venv/bin/activate
```
Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --port=8000 --host=0.0.0.0
```

Run with docker
===================
Se encuentra un archivo Dockerfile para crear la imagen del proyecto y un docker-compose para gestionar el contenedor.

Así mismo esta creado un archivo Makefile con las acciones automatizadas.

Podes crear la imagen y levantar el proyecto ejecutando los siguientes comandos:

Run commands with make

- Create image

    ```bash
    make build
    ```

- Run container

    ```bash
    make up
    ```

Esto levantará el proyecto localmente en la dirección 127.0.0.1:8000

## Running the tests

```sh
make test
```

POSTMAN COLLECTIONS
===================
Se adjunta un archivo de tipo colección que contiene las peticiones GET, POST y DELETE para hacer las pruebas.

- Characters.postman_collection.json

DOCUMENTATION
===================
Ingresando al path /docs se encontrara la documentación de la API