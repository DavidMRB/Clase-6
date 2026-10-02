def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El valor no puede estar vacío.")


def pedir_entero(mensaje, minimo=1):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) >= minimo:
            return int(valor)
        print(f"Debe ingresar un número entero mayor o igual a {minimo}.")


def ejecutar_constructor(plan_actual=None):
    """
    Actividad principal: construcción de un plan personalizado.

    El while permite solicitar información varias veces porque no se
    conoce de antemano cuántos días desea registrar el usuario.
    """
    plan = list(plan_actual or [])

    print("\n--- CONSTRUCTOR DE PLAN ---")
    print("Agregue días y actividades. Puede detenerse cuando quiera.")

    while True:
        dia = pedir_texto(
            "\nNombre del día (ej. Sábado) o 'fin' para terminar: "
        )

        if dia.lower() == "fin":
            break

        actividades = []
        cantidad = pedir_entero(
            "¿Cuántas actividades desea agregar a este día?: "
        )

        for numero in range(cantidad):
            nombre = pedir_texto(f"Actividad {numero + 1}: ")
            tipo = pedir_texto("Tipo de actividad: ")
            lugar = pedir_texto("Establecimiento/lugar: ")

            actividades.append({
                "nombre": nombre,
                "tipo": tipo,
                "lugar": lugar
            })

        plan.append({
            "dia": dia,
            "actividades": actividades
        })

        continuar = input(
            "\n¿Desea agregar otro día? (s/n): "
        ).strip().lower()

        if continuar == "n":
            break

    print(f"\nPlan actualizado. Días registrados: {len(plan)}")
    return plan
