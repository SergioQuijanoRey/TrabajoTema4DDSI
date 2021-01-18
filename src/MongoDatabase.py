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

    def print_query_result(self, query_result):
        """Muestra de buena forma un resultado de una consulta"""
        for result in query_result:
            print(result)
