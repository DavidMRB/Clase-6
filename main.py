from constructor_plan import ejecutar_constructor
from buscar_actividad import ejecutar_busqueda
from ciclo_anidado import ejecutar_organizador
from resumen_plan import mostrar_resumen


def mostrar_menu():
    print("\n" + "=" * 60)
    print("PLANATI - MODULO ACADEMICO DE CONSOLA")
    print("=" * 60)
    print("1. Crear / modificar plan")
    print("2. Buscar actividad en el plan")
    print("3. Ver plan organizado")
    print("4. Ver resumen del plan")
    print("0. Salir")


def main():
    plan = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            plan = ejecutar_constructor(plan)
        elif opcion == "2":
            ejecutar_busqueda(plan)
        elif opcion == "3":
            ejecutar_organizador(plan)
        elif opcion == "4":
            mostrar_resumen(plan)
        elif opcion == "0":
            print("\nPrograma finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
