# HistoCar
## Sistema para Gestión de servicios vehiculares
Aplicación que funciona como una historia clínica de los vehículos, con el fin de mejorar la gestión de los servicios que les son realizados.


Este proyecto fue desarrollado durtante el curso "ProgramaBIT" de la Cámara Uruguaya de Tecnologías de la Información e INEFOP

Tecnlogías utilizadas:
* Python
* Django
* HTML
* CSS
* Javascript
* Visual Studio Code IDE
* Git / Github
* Trello (Para la gestión de las tareas, historias de usuario)




Pasos para preparar el proyecto:

    1 - Clonar repositorio remoto:
            git clone https://github.com/bITAMINAS/histocar_project.git
    2 - Crear el virtual enviroment: 
            python -m venv env
    3 - Instalar dependencias del proyecto:
            pip install -r requirements.txt 

Otros:
- Para actualizar el archivo de dependencias Requirements.txt (NO ES PARA INSTALAR LOS NUEVOS PAQUETES)
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
        
