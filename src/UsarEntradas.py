from MongoDatabase import MongoDatabase

class UsarEntradas(MongoDatabase):
    # TODO -- falta alguna que otra funcionalidad
    def insert_usar_entrada(self):
        """
        Insertamos datos en UsarEntradas
        """
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

        id_ent = [1,1,1,1,1,1,1,1,1]

        # Insertamos los datos
        for index in range(len(dni)):
            usar_data = {
                'dni_asistente': dni[index],
                'id_actividad': id_act[index],
                'id_entrada' : id_ent[index]
            }

            result = self.db.usar_entradas.insert_one(usar_data)
    
    def erase(self, dni: str):
        self.db.usar_entradas.remove({'dni_asistente': dni})

    def select_entrada_given_dni(self, input_dni):
        """Selecciona las entradas dado el dni """

        return self.db.usar_entradas.find({'dni_asistente': input_dni})

    def mostrar_todos(self):
        """Muestra toda la informacion de la base de datos"""
        resultados = self.db.usar_entradas.find()
        for resultado in resultados:
            print(resultado)
