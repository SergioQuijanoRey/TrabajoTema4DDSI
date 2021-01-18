import MongoDatabase from main

class UsarEntradas(MongoDatabase):
    """
        Insertamos datos en UsarEntradas
        """
        # Datos ficticios sobre los clientes
        dni = [
            "0000000k",
            "0000001k",
            "0000002k",
            "0000003k",
            "0000004k",
            "0000005k",
            "0000006k",
            "0000007k",
            "0000008k"
        ]

        id_act = [1,2,3,4,5,6,7,8,9]


        # Insertamos los datos
        for index in range(len(dni)):
            usar_data = {
                'dni_asistente': dni[index],
                'id_actividad': id_act[index]
            }

            result = self.db.usar_entradas.insert_one(client_data)