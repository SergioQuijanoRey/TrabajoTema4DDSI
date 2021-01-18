from main import MongoDatabase

#======================= ACTIVIDADES ===========================
class Activity(MongoDatabase): 

    def insert_activity_data(self):
        """
        Insertamos datos en una coleccion 'Actividades'
        """
        # Datos ficticios sobre las actividades
        id_actividad = [
            "Actividad 1",
            "Actividad 2",
            "Actividad 3",
            "Actividad 4",
            "Actividad 5",
            "Actividad 6",
            "Actividad 7",
            "Actividad 8",
            "Actividad 9",
            "Actividad 10"
        ]

        description = [
            "Descripcion 0",
            "Descripcion 1",
            "Descripcion 2",
            "Descripcion 3",
            "Descripcion 4",
            "Descripcion 5",
            "Descripcion 6",
            "Descripcion 7",
            "Descripcion 8",
            "Descripcion 9"
        ]

        date = [
            "Fecha 0",
            "Fecha 1",
            "Fecha 2",
            "Fecha 3",
            "Fecha 4",
            "Fecha 5",
            "Fecha 6",
            "Fecha 7",
            "Fecha 8",
            "Fecha 9"
        ]


        # Insertamos los datos
        for index in range(len(id_actividad)):

            activity_data = {
                'id_actividad': id_actividad[index],
                'descripcion': description[index],
                'fecha': date[index],
       
            }

            result = self.db.activity.insert_one(activity_data)

    def select_activity_given_id(self, input_actividad: str):
        """Selecciona los clientes dado el dni """

        return self.db.activity.find({'id_actividad': input_actividad})

    