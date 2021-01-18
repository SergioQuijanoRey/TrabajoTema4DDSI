import MongoDatabase from main

class entradas(MongoDatabase):
    def crear_entradas():
        """
        Datos sobre las entradas
        """
        id_entrada = [1,2,3]

        id_actividad = [1,2,3]        ]

        cantidad = [1,2,1]

        devolucion = [
            "true",
            "false",
            "false"
        ]

        for index in range(len(id_entrada)):
            entradas_data = {
                'id_entrada': id_entrada[index]
                'id_actividad': id_actividad[index]
                'cantidad': cantidad[index]
                'devolucion' : devolucion[index]
            }

            result = self.db.entradas.insert_one(client_data)
