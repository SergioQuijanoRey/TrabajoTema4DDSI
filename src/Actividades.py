from MongoDatabase import MongoDatabase

#======================= ACTIVIDADES ===========================
class Actividades(MongoDatabase):

    def insert_activity_data(self):
        """
        Insertamos datos en una coleccion 'Actividades'
        """
        # Datos ficticios sobre las actividades
        # TODO -- esto deberian ser enteros
        id_actividad = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
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

    def select_activity_given_id(self, input_actividad: int):
        """Selecciona la actividad dado el id """

        return self.db.activity.find({'id_actividad': input_actividad})


