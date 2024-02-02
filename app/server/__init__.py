from os import getenv

IS_DEBUG = getenv('IS_DEBUG', 'false').lower() in ('1', 'true')  # Is true if outside of docker

if IS_DEBUG:
    host = 'localhost'
else:
    host = 'db'  # Utiliza el nombre del servicio definido en tu archivo docker-compose.yml

DB_NAME = getenv('DB_NAME')
DB_USR = getenv('DB_USR')
DB_PWD = getenv('DB_PWD')
DB_ROOT_PWD = getenv('DB_ROOT_PWD')
DB_PORT_CONTAINER = getenv('DB_PORT_CONTAINER')
DB_PORT_HOST = getenv('DB_PORT_HOST')
DB_HOST = host
