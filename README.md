# pruebaBack-AppLab-
Backend de prueba de Applab.
- [python 3.8](https://www.python.org/downloads/release/python-370/)
- [pipenv](https://pipenv-es.readthedocs.io/es/latest/install.html)

### Run project
Ubicado en la carpeta del proyecto ejecutar los comandos siguientes:

Para preparar el entorno virtual de python sustituya **python3** por la ruta de instalación de python 3.7 de su sistema.
``` sh
# prepare viertualenv python, replace python3 with
$ pipenv --python python3
```
Despues de crear el entonrno virtual es necesario intalar las dependencias del entonrno.
```
# install dependencies
$ pipenv install
```
Finalmente solo debe ejecutar el servidor de flask.
```
# start flask server with hot reload at localhost:5000
$ pipenv run python server.py
```