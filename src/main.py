from pymongo import MongoClient
from pprint import pprint

class MongoDatabase:
    """Clase quwe representa la base de datos de MongoDB"""

    def __init__(self):
        """Inicializa la clase"""
        self.database_ip =  "172.20.0.2"
        self.client = None
        self.db = None

        self.connect_to_database()

    def connect_to_database(self):
        """Realiza la conexion con la base de datos"""
        self.client = MongoClient(self.database_ip)
        self.db = self.client.admin

    def execute_command(self, command: str):
        """Ejecuta un comando dado y devuelve los resultados"""
        return self.db.command(command)

    def server_status(self):
        """Muestra el status del servidor"""
        return self.execute_command("serverStatus")

    def insert_example_data(self):
        """
        Insertamos datos en una coleccion 'clientes'
        A diferencia de otras bases de datos, no hace falta la sentencia tipo 'CREATE TABLE'
        """
        # Datos ficticios sobre los clientes
        client_name = [
            "Sergio Quijano",
            "Lucia Salamanca",
            "Jesus Lopez",
            "Juan Jose Herrera"
        ]

        client_city = [
            "Santander",
            "Malaga",
            "Linares",
            "Jodar"
        ]

        client_dni = [
            "00000000k",
            "00000001k",
            "00000002k",
            "00000003k"
        ]

        # Insertamos los datos
        for index in range(len(client_name)):
            client_data = {
                'name': client_name[index],
                'city': client_city[index],
                'DNI': client_dni[index]
            }

            result = self.db.clientes.insert_one(client_data)

    def select_client_given_city(self, input_city: str):
        """Selecciona los clientes de una determinada ciudad"""

        return self.db.clientes.find({'city': input_city})

    def print_query_result(self, query_result):
        """Muestra de buena forma un resultado de una consulta"""
        for result in query_result:
            print(result)

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

            if index%2 == 0:
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


    def select_assistant_given_dni(self, input_dni: str):
        """Selecciona los clientes dado el dni """

        return self.db.assistant.find({'dni': input_dni})

    def select_assistant_with_covid(self):
        """Selecciona los clientes dado el dni """

        return self.db.assistant.find({'covid': True})

if __name__ == "__main__":
    mongo = MongoDatabase()

    # Mostramos el estado de la base de datos
    print("El estado del servidor es:")
    print("=" * 80)
    pprint(mongo.server_status())
    print("")

    # Insertamos datos de ejemplo
    mongo.insert_example_data()

    # Hacemos unas cuantas consultas de prueba sobre los datos insertados
    print("Los clientes de Santander son:")
    print("=" * 80)
    mongo.print_query_result(mongo.select_client_given_city("Santander"))

    print("-" * 100)

    # Hacemos una consulta de los asistentes
    mongo.insert_assistant_data()

    dni = "0000003k"
    print(f"El asistente con dni {dni} es: " )
    mongo.print_query_result(mongo.select_assistant_given_dni(dni))

    print("="*80)
    print("Los asistentes que tienen covid son ")
    mongo.print_query_result(mongo.select_assistant_with_covid())
