def mostrar_resumen(plan):
    print("\n--- RESUMEN DEL PLAN ---")

    if not plan:
        print("No hay información para resumir.")
        return

    total_actividades = 0
    tipos = {}

    for dia in plan:
        for actividad in dia["actividades"]:
            total_actividades += 1

            tipo = actividad["tipo"].lower()
            tipos[tipo] = tipos.get(tipo, 0) + 1

    print(f"Días planificados: {len(plan)}")
    print(f"Total de actividades: {total_actividades}")

    if tipos:
        print("Actividades por tipo:")

        for tipo, cantidad in tipos.items():
            print(f"  - {tipo}: {cantidad}")
