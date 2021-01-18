from usar import UsarEntradas
from entradas import entradas
from MongoDatabase import MongoDatabase
from pprint import pprint

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

    usar_entradasdb = UsarEntradas()
    usar_entradasdb.insert_usar_entrada()
    entradasdb = entradas()
    entradasdb.crear_entradas()
