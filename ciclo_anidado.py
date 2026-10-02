def ejecutar_organizador(plan):
    """
    Muestra la estructura jerárquica del plan.

    Ciclo externo: recorre los días.
    Ciclo interno: recorre las actividades de cada día.
    """
    print("\n--- PLAN ORGANIZADO ---")

    if not plan:
        print("El plan está vacío. Cree primero un plan.")
        return

    for dia in plan:
        print(f"\n{dia['dia']}")
        print("-" * 40)

        if not dia["actividades"]:
            print("  Sin actividades.")

            # El día no tiene registros que mostrar.
            # Se pasa directamente al siguiente día.
            continue

        for numero, actividad in enumerate(
            dia["actividades"], start=1
        ):
            print(
                f"  {numero}. {actividad['nombre']} | "
                f"{actividad['tipo']} | {actividad['lugar']}"
            )
