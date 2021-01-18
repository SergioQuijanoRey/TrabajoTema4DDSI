from MongoDatabase import MongoDatabase

class Asistentes(MongoDatabase):
    def insert_assistant_data(self):
        """
        Insertamos datos en una coleccion 'Asistentes'
        """

        # Datos ficticios sobre los clientes
        assistant_name = [
            "Pilar Aranda 1",
            "Pilar Aranda 2",
            "Pilar Aranda 3",
            "Pilar Aranda 4",
            "Pilar Aranda 5",
            "Pilar Aranda 6",
            "Pilar Aranda 7",
            "Pilar Aranda 8",
            "Pilar Aranda 9",
            "Pilar Aranda 10"
        ]

        assistant_id = [
            "0000000k",
            "0000001k",
            "0000002k",
            "0000003k",
            "0000004k",
            "0000005k",
            "0000006k",
            "0000007k",
            "0000008k",
            "0000009k"
        ]

        assistant_bank_account = [
            "123456780jjx",
            "123456781jjx",
            "123456782jjx",
            "123456783jjx",
            "123456784jjx",
            "123456785jjx",
            "123456786jjx",
            "123456787jjx",
            "123456788jjx",
            "123456789jjx"
        ]

        # Insertamos los datos
        for index in range(len(assistant_name)):

            if index % 2 == 0:
                contagiado = True
            else:
                contagiado = False

            assistant_data = {
                'name': assistant_name[index],
                'dni': assistant_id[index],
                'bank_account': assistant_bank_account[index],
                'covid': contagiado
            }

            result = self.db.assistant.insert_one(assistant_data)

    def select_assistant_given_dni(self, input_dni):
        """Selecciona los clientes dado el dni """

        return self.db.assistant.find({'dni': input_dni})

    def select_assistant_with_covid(self):
        """Selecciona los clientes dado el dni """

        return self.db.assistant.find({'covid': True})
