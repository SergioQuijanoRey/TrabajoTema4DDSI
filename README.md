# Trabajo del tema 4 de Sistemas de Información

## TODO

* [x] Crear un Dockerfile para poner MongoDB en un contenedor
* [x] Crear un Makefile para que todo el mundo pueda ejecutar las prácticas
* [x] Crear un entorno de ejecución básico para MongoDB
* [x] Elegir las tablas que copiar de la práctica: entre todos
* [x] Crear Docker para python porque Jesus no lo ejecuta bien: Sergio
* [ ] Crear un par de estructuras de datos en MongoDB
* [ ] Insertar una serie de datos sobre las anteriores estructuras
* [ ] Otras operaciones sobre los datos
* [ ] Redactar documento PDF

## Esquema

~~~json
Actividades:

{
    'id_actividad': <id_actividad>,
    'descripcion': <descripcion>,
    'fecha': <fecha>,
}

Asistentes
{
    DNIAsistente VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(300),
    CuentaBancaria VARCHAR(400),
    Covid BOOLEAN NOT NULL DEFAULT FALSE
}

Entradas
{
    IdEntrada INT,
    IdActividad INT,
    Cantidad INT DEFAULT 1,
    Devolucion BOOLEAN NOT NULL DEFAULT FALSE,
}

UsarEntrada
{
    DNIAsistente
    id_actividad
}
~~~
