from dotenv import load_dotenv
from os import getenv

RUN_OUTSIDE_DOCKER = getenv('RUN_OUTSIDE_DOCKER', 'false').lower() in ('1', 'true')  # Set true if outside of docker


if RUN_OUTSIDE_DOCKER:
    load_dotenv('../docker.env')
    host = 'localhost'

else:
    host = 'database'  # Use the value for the db service defined in docker-compose.yml

# DB_ROOT_PWD = getenv('DB_ROOT_PWD')
DB_PORT_CONTAINER = getenv('DB_PORT_CONTAINER') # Port as seen from inside the container network

DB_DATA = {
    'NAME': getenv('DB_NAME'),
    'USER': getenv('DB_USR'),
    'PASSWORD': getenv('DB_PWD'),
    'PORT': DB_PORT_CONTAINER,
    'HOST': host
}
