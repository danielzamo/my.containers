## Ejecución de app flask

Ejecución inicial

_Estructura ficheros iniciales_

A continuación se muestra la sesión inicial de comandos ejecutados. Para desplegar una aplicación basada en Flask inicial, en secuencia debe ejecutarse:

1. Instalar, si no esta, el paquete `python3.8-venv` (para gestionar diferentes entornos basados en *Python*).
2. Crear un entorno (en este ejemplo de nombre `venv`).
3. Activar el entorno.
4. Instalar el modulo `Flask`.
5. Escribir nuestra aplicación. En el ejemplo se realiza en el fichero `app.py`. Es simplemente mostrar un texto *Hola*.

La secuencia de comandos se muestra a continuación. Estos son:

```bash
$ sudo apt-get install python3.8-venv
$ python -m venv venv
$ source venv/bin/activate
(venv)$ pip install Flask
```

Se muestra el arbol de directorios hasta un nivel 2 de profundidad. La aplicación inicial reside en el fichero `$(pwd)/src/app.py`. Por simplicidad, se da una profundidad de nivel 2 (para limitar la salida del directorio `venv`)

```bash
$ tree -L 2
.
├── README.md
├── src
│   └── app.py
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    ├── pyvenv.cfg
    └── share
```

```bash
(venv)$ cat src/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola</h1>"

if __name__ == '__main__':    
    app.run(port=5000, debug=True, host='0.0.0.0')
 
(venv)$ python src/app.py
```

La aplicación se ejecuta. Se puede verificar con un navegador en el URL `http://localhost:5000`. La captura se muestra [aquí][start.app]

![Inicio de app Flask][start.app]

[start.app]: img/start.app.png

## Creando el primer contenedor

*[1]* Un *Dockerfile* inicial

```bash
(venv) $ cat Dockerfile
FROM alpine:latest
RUN apk add --no-cache python3-dev py3-pip
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt
COPY ./src .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug=True"]
```

*[2]* Fichero *requirements.txt*

Se muestra la generación del fichero y el contenido del mismo. Este contiene los módulos a agregar con `pip` al crearse la imagen del contenedor)

```bash
(venv)$ pip freeze > requirements.txt
(venv)$ cat requirements.txt
click==8.0.3
Flask==2.0.2
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
Werkzeug==2.0.2
```

*[3]* Generar la imagen del contenedor

```bash
podman build -t app1 .
```

*[3.1]* Revisar las imagenes actuales

Con el siguiente comando, se revisa de que este la recien creada. Mostrar las imágenes con el comando:

```bash
podman images
```

*[4]* Ejecutar el contenedor en modo independiente (modo _detached_, opción `--detach` o `-d`)

El siguiente comando ejecuta el contenedor exponiendo el servicio (aplicación basada en _Flask_, interpreta en _Python_) en el puerto 5000. El comando emitido es:

```bash
podman run --rm -d -p 5000:5000 localhost/app1
```

*Donde:*

- `podman`: comando `podman`
- `run`: ejecuta el contenedor
- `--rm`: el contenedor sera borrado al ser apagado
- `-d`: se ejecuta en modo *detached* (independinte. El contenedor queda como en modo demonio, ofreciendo el servicio).
- `-p 5000:5000`: puerto expuesto `5000` tanto adentro del contenedor como hacia el host.
- `localhost/app1`: nombre de la imagen a ejecutar instancia del contenedor lanzado.


