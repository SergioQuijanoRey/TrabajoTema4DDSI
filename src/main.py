from usar import UsarEntradas
from MongoDatabase import MongoDatabase
from pprint import pprint
from Asistentes import Asistentes

from Entradas import Entradas

if __name__ == "__main__":
    mongo = MongoDatabase()



    usar_entradasdb = UsarEntradas()
    usar_entradasdb.insert_usar_entrada()

    # Insercion de datos de las entradas
    entradasdb = Entradas()
    entradasdb.crear_entradas()

    # Insercion de datos de asistentes
    asistentesdb = Asistentes()
    asistentesdb.insert_assistant_data()

    # Hacemos una consulta sobre la coleccion de asistentes
    dni = "0000003k"
    print(f"El asistente con dni {dni} es: " )
    print("=" * 80)
    asistentesdb.print_query_result(asistentesdb.select_assistant_given_dni(dni))
    print("")

    # Hacemos otra consulta sobre asistentes con COVID
    print("Los asistentes que tienen covid son ")
    print("=" * 80)
    mongo.print_query_result(asistentesdb.select_assistant_with_covid())
    print("")
