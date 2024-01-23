## Pasos para empezar a colaborar

1. Asignarse un issue
2. Crear una rama desde `main`, con nombre `(issueNr_nombre_de_rama)`
3. Hacer push de cambios a esa rama. Una vez finalizada la funcionalidad, asignar la etiqueta `ready-for-review`
4. El reviewer indicará si se deben hacer cambios (quitando la etiqueta) o no
5. Una vez finalizados los cambios, el reviewer realizará merge a la rama `main`

IMPORTANTE: los únicos commits a la rama `main` deben ser cambios al README

## Para iniciar la app

1. En el directorio que contiene al archivo docker-compose.yml, correr
   ```
   sudo docker compose --env-file docker.env up --build
   ```
   <details>

   <summary>EN CASO DE ERROR DE CONEXIÓN</summary>  

   `django.db.utils.OperationalError: (2002, "Can't connect to server on 'database' (115)")`  
   Detener y eliminar los contenedores con  
   ```
   docker container stop <mysql-id>
   docker container prune
   ```
   </details>

2. Luego, en un navegador, visitar http://127.0.0.1:8000/
   ![image](https://github.com/gianfranco-s/proyecto_resto/assets/69116761/28f9a720-9293-4a90-942a-73eff50eb03d)


## Para realizar migraciones
Es posible realizar migraciones desde la terminal local, o desde docker

* Terminal local: `python manage.py makemigrations`
* Docker: 
```
sudo docker exec django-docker python manage.py makemigrations
sudo docker exec django-docker python manage.py showmigrations
sudo docker exec django-docker python manage.py migrate
```