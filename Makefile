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

	@echo "Borrando contenedores anteriores"
	docker rm mongoddsi | echo "El contenedor no estaba corriendo todavia"
	@echo "================================================================================"
	@echo ""

	@echo "Lanzando un contenedor de dicha imagen"
	@echo "================================================================================"
	docker run --name mongoddsi -d mongoddsi:latest
	@echo ""

run:
	@echo "No estamos haciendo nada"

