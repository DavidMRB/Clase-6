def ejecutar_busqueda(plan):
    """
    Busca una actividad dentro del plan.

    Se utilizan dos for porque la información está organizada en dos
    niveles: días y actividades. Cuando se encuentra la actividad
    solicitada, break interrumpe ambos recorridos de forma controlada.
    """
    print("\n--- BUSCADOR DE ACTIVIDAD ---")

    if not plan:
        print("El plan está vacío. Cree primero un plan.")
        return

    termino = input(
        "Ingrese el nombre de la actividad que desea buscar: "
    ).strip().lower()

    if not termino:
        print("Debe ingresar un término de búsqueda.")
        return

    encontrada = False

    for dia in plan:
        for actividad in dia["actividades"]:
            if termino in actividad["nombre"].lower():
                print("\nActividad encontrada:")
                print(f"  Día: {dia['dia']}")
                print(f"  Nombre: {actividad['nombre']}")
                print(f"  Tipo: {actividad['tipo']}")
                print(f"  Lugar: {actividad['lugar']}")

                encontrada = True

                # Ya se encontró la actividad solicitada.
                # Continuar recorriendo no aporta información adicional.
                break

        if encontrada:
            # Interrumpe también el ciclo externo.
            break

    if not encontrada:
        print("No se encontró una actividad con ese nombre.")
