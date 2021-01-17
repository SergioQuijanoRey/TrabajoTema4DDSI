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
            "Esta tampoco"
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

        return self.db.clientes.find_one({'city': input_city})






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
    pprint(mongo.select_client_given_city("Santander"))
