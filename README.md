# histocar_project
Proyecto de gestión de servicios vehiculares

Pasos para preparar el proyecto:

    1 - Clonar repositorio remoto:
            git clone https://github.com/bITAMINAS/histocar_project.git
    2 - Crear el virtual enviroment: 
            python -m venv env
    3 - Instalar dependencias del proyecto:
            pip install -r requirements.txt 

Otros:
- Para actualizar el archivo de dependencias Requirements.txt:
    pip freeze > requirements.txt

- Para poner a correr el servidor de Django:
    
    python manage.py runserver

- Actualizar base de datos de la aplicación conectada (webapps):
    
    python manage.py makemigrations webapp
    python manage.py migrate

- Para movernos a otra Rama:
    
    git checkout nombre_de_la_rama

- Para hacer un merge, por ejemplo de la rama "desarrollo" hacia la rama "master", primero hay que cambiarse hacia la rama "master", y luego se ejecuta el comando:
    
    git merge desarrollo

Links de interés:
    https://www.campusmvp.es/recursos/post/git-los-conceptos-de-master-origin-y-head.aspx


    Plantilla utilizada
        https://adminlte.io/themes/AdminLTE/
