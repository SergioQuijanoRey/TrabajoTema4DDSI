all:
	@echo "Comandos de este Makefile:"
	@echo "	make install: instala todos los componentes necesarios para lanzar la aplicacion"
	@echo "		- Es necesario tener docker instalado y configurado previamente en el sistema"
	@echo "	make run: lanza la aplicacion"
	@echo "		- Es necesario que la aplicacion haya sido instalada previamente"

install:
	@echo "Build de la imagen de la base de datos"
	@echo "================================================================================"
	docker build -t mongoddsi:latest .
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
	@echo "No estamos haciendo nada"

