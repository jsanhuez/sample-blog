# Sample blog - blog de ejemplo

Este repositorio contiene una aplicación web construida con Django web framework. Es un blog de ejemplo.

El proyecto tiene los siguientes módulos:

* Blog
* Registro de usuarios
* Panel Admin

## Antes de comenzar
Para ejecutar sample-blog debes tener instalar Python3, pip. Esto varía dependiendo de tu sistema operativo.

Instalados python3 y pip, instalar Django:

```
pip install Django
```

## Comenzar

Clona el proyecto

```
git clone https://github.com/jsanhuez/sample-blog.git
```

Ve a la raíz del proyecto

```
cd sample-blog
```

## Preparar entorno virtual
Para instalar las librerías que el proyecto utiliza, crea un entorno virtual

```
python3 -m venv env
```

Luego, activar el entorno.

```
source env/bin/activate
```

Verás el prefijo (env) en la Terminal.

```
(env) ~/sample-blog$
```

## Instalar librerías
A continuación, ejecutar

```
pip install -r requirements.txt
```

Si queremos ver las librerías que tenemos instaladas podemos lanzar el siguiente comando:

```
pip freeze
```

## Crear base de datos
Este proyecto fue construido utilizando el motor MySQL. Pueden utilizarse otras, como PostgreSQL o SQLite.


```
$ mysql -u root -p
mysql> CREATE DATABASE sample_blog;
mysql> CREATE USER sampleblog@localhost IDENTIFIED BY 'sample&blog/pass';
mysql> GRANT ALL PRIVILEGES ON sample_blog.* TO sampleblog@localhost;
mysql> FLUSH PRIVILEGES;
mysql> \q
```

Agregar archivo .env en carpeta sample_blog

```
:~/sample-blog$ cd sample_blog/
```

Aplicar migrations para crear el esquema de base de datos:

```
python manage.py makemigrations
```

Luego,

```
python manage.py migrate
```

## Cargar datos

```
python manage.py loaddata db-data.json
```

## Ejecutar proyecto

Ejecutar en servidor local:

```
python manage.py runserver
```

En un navegador ir a 

```
http://127.0.0.1:8000
```

El panel de administración está en la url

```
http://127.0.0.1:8000/admin
```

Con los siguientes datos

```
User: admin
Pass: 4dm1n%&/
```

## Construido con
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

## Autor

* **Juan Sanhueza Rodríguez** - [Juan SR](https://github.com/jsanhuez)
