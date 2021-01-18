from usar import UsarEntradas
from entradas import entradas
from MongoDatabase import MongoDatabase
from pprint import pprint
from Asistentes import Asistentes

if __name__ == "__main__":
    mongo = MongoDatabase()

    # Hacemos una consulta de los asistentes
    asistentesdb = Asistentes()
    asistentesdb.insert_assistant_data()

    dni = "0000003k"
    print(f"El asistente con dni {dni} es: " )
    asistentesdb.print_query_result(asistentesdb.select_assistant_given_dni(dni))

    print("="*80)
    print("Los asistentes que tienen covid son ")
    mongo.print_query_result(asistentesdb.select_assistant_with_covid())

    usar_entradasdb = UsarEntradas()
    usar_entradasdb.insert_usar_entrada()
    entradasdb = entradas()
    entradasdb.crear_entradas()
