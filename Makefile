all:
	@echo "Comandos de este Makefile:"
	@echo "	make install: instala todos los componentes necesarios para lanzar la aplicacion"
	@echo "		- Es necesario tener docker instalado y configurado previamente en el sistema"
	@echo "	make run: lanza la aplicacion"
	@echo "		- Es necesario que la aplicacion haya sido instalada previamente"
	@echo "	make run_docker: lanza la aplicacion pero con python en docker"
	@echo "		- Es necesario que la aplicacion haya sido instalada previamente"

install:
	@echo "Build de la imagen de la base de datos"
	@echo "================================================================================"
	docker build -t mongoddsi:latest .
	@echo ""

	@echo "Build de la imagen de la aplicacion python"
	@echo "================================================================================"
	docker build -t pythonddsi:latest -f ./DockerfilePython .
	@echo ""

	@echo "Asignando red de Docker"
	@echo "================================================================================"
	docker network create --subnet=172.20.0.0/16 own_network 2> /dev/null || echo "La red ya existe"
	@echo ""

	@echo "Borrando contenedores anteriores"
	docker stop mongoddsi 2> /dev/null || echo "El contenedor no estaba corriendo"
	docker rm mongoddsi 2> /dev/null || echo "El contenedor no estaba creado previamente"
	@echo "================================================================================"
	@echo ""

	@echo "Lanzando un contenedor de dicha imagen"
	@echo "================================================================================"
	docker run --name mongoddsi --net=own_network --ip 172.20.0.2 -d mongoddsi:latest
	@echo ""

	@echo ""
	@echo "Instalando paquetes de pipenv"
	@echo "================================================================================"
	pipenv install

run:
	@echo "Lanzando la aplicacion"
	docker start mongoddsi
	pipenv run python3 src/main.py

# No esta pensado para que lo corra el usuario a mano
# Esta pensado para ser invocado por otras etapas del Makefile
refresh_python:
	@echo "Borrando contenedores anteriores corriendo python"
	docker stop pythonddsi 2> /dev/null || echo "El contenedor de python no estaba corriendo"
	docker rm pythonddsi 2> /dev/null || echo "El contenedor de python no estaba creado previamente"
	@echo ""

	@echo "Creando una imagen con el codigo actualizado"
	docker build -t pythonddsi:latest -f ./DockerfilePython .

run_docker:
	@echo "Lanzando la aplicacion de base de datos"
	docker start mongoddsi
	@echo ""

	@echo "Lanzando aplicacion de python"
	make refresh_python
	docker run --name pythonddsi --rm --net=own_network --ip 172.20.0.3 pythonddsi:latest
