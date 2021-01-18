from MongoDatabase import MongoDatabase
from Asistentes import Asistentes
from Entradas import Entradas
from Actividades import Actividades
from UsarEntradas import UsarEntradas

if __name__ == "__main__":
    mongo = MongoDatabase()

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

    # Insertamos los datos de las actividades
    actividadesdb = Actividades()
    actividadesdb.insert_activity_data()

    # Mostramos una actividad
    id_actividad = "Actividad 1"
    print(f"Mostrando la actividad con identificador {id_actividad}")
    print("=" * 80)
    mongo.print_query_result(actividadesdb.select_activity_given_id(id_actividad))
    print("")

    # Insertamos uso de entradas
    usar_entradasdb = UsarEntradas()
    usar_entradasdb.insert_usar_entrada()
