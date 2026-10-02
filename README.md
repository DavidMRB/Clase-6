# PlanATi — Actividad de ciclos en consola

Este repositorio contiene una implementación de consola basada en el dominio del proyecto **PlanATi**. La aplicación permite construir un plan compuesto por días y actividades, buscar actividades y consultar el plan organizado.

> **Alcance de este repositorio:** se trabajan las actividades **1 a 10**, con especial desarrollo documental de las actividades **1 a 4** y **8 a 10**, tal como solicita la actividad.
>
> Las actividades 11, 13 y 14 se dejan fuera de este entregable.

---

# ACTIVIDAD 1. IDENTIFICACIÓN DE UNA NECESIDAD DEL PROYECTO

## NOMBRE DEL PROYECTO

**PlanATi**

## FUNCIONALIDAD QUE SE VA A DESARROLLAR

**Constructor y organización de un plan personalizado de actividades.**

La funcionalidad permite que el usuario construya un plan indicando diferentes días y, para cada día, las actividades que desea realizar y el establecimiento o lugar asociado.

La aplicación de consola es un prototipo funcional de esta posible extensión de PlanATi. Su propósito es trabajar con la misma clase de información del proyecto y demostrar la lógica que posteriormente podría adaptarse a la aplicación principal.

## PROBLEMA QUE RESUELVE

Un usuario puede necesitar organizar varias actividades dentro de un plan. Como el número de días y actividades puede variar, el programa debe permitir registrar información varias veces y conservarla organizada.

La funcionalidad evita que el usuario tenga que definir previamente una cantidad fija de días o actividades.

## ¿QUÉ INFORMACIÓN DEBE PROCESAR?

La funcionalidad procesa:

- Días del plan.
- Nombre de cada actividad.
- Tipo de actividad.
- Establecimiento o lugar donde se realizará.
- Cantidad de actividades que tendrá cada día.

La información se almacena en una estructura de listas y diccionarios:

```text
Plan
└── Día
    └── Actividades
        ├── Nombre
        ├── Tipo
        └── Lugar
```

## ¿QUÉ ACCIÓN DEBE REPETIRSE?

Debe repetirse la captura de información del plan:

1. Solicitar un día.
2. Solicitar la cantidad de actividades.
3. Registrar cada actividad.
4. Preguntar si el usuario desea agregar otro día.

También se repite la validación cuando el usuario introduce información vacía o una cantidad inválida.

## ¿CUÁNDO DEBE TERMINAR LA REPETICIÓN?

La construcción del plan termina cuando:

- el usuario escribe `fin` al solicitar un día; o
- el usuario responde `n` cuando se pregunta si desea agregar otro día.

La validación de datos termina cuando se recibe una entrada válida.

---

# ACTIVIDAD 2. ANÁLISIS DE LA SOLUCIÓN

## PROBLEMA

El usuario necesita construir un plan personalizado con una cantidad variable de días y actividades, manteniendo las actividades organizadas dentro de cada día.

## DATOS DE ENTRADA

| Dato | Tipo | Descripción |
|---|---|---|
| Día | `str` | Nombre del día que se agregará al plan |
| Cantidad de actividades | `int` | Número de actividades que tendrá el día |
| Nombre | `str` | Nombre de la actividad |
| Tipo | `str` | Categoría o tipo de actividad |
| Lugar | `str` | Establecimiento o lugar asociado |
| Continuar | `str` | Indica si el usuario desea agregar otro día |

## PROCESO

1. Iniciar con el plan existente o una lista vacía.
2. Solicitar el nombre del día.
3. Comprobar si el usuario desea terminar.
4. Solicitar la cantidad de actividades.
5. Recorrer esa cantidad y registrar cada actividad.
6. Guardar las actividades dentro del día.
7. Guardar el día dentro del plan.
8. Preguntar si se desea agregar otro día.
9. Repetir mientras el usuario quiera continuar.
10. Mostrar el número de días registrados.

## DATOS QUE DEBEN ALMACENARSE

Cada día se almacena como un diccionario:

```python
{
    "dia": "Sábado",
    "actividades": [
        {
            "nombre": "Cine",
            "tipo": "Entretenimiento",
            "lugar": "Cine Central"
        }
    ]
}
```

El conjunto de días se almacena en una lista denominada `plan`.

## ACCIÓN QUE DEBE REPETIRSE

La acción principal es **registrar nuevos días y sus actividades**.

## CONDICIÓN DE REPETICIÓN

La construcción continúa mientras el usuario no indique que desea terminar.

Además, las entradas se validan mediante `while` hasta recibir valores válidos.

## RESULTADO

Se obtiene un plan estructurado con sus días y actividades, que posteriormente puede ser utilizado por las funciones de búsqueda, organización y resumen.

## ¿QUÉ CICLO ES MÁS ADECUADO: `while` O `for`?

Para la construcción del plan, el ciclo más adecuado es **`while`**.

### ¿Por qué?

Porque no se conoce previamente cuántos días desea registrar el usuario. La repetición depende de una decisión que se toma durante la ejecución.

Por el contrario, el `for` resulta adecuado para recorrer una cantidad ya determinada, como las actividades que el usuario indicó para un día.

Por eso la solución utiliza ambos ciclos en situaciones diferentes:

- `while` → cantidad variable de días y validación.
- `for` → cantidad conocida de actividades de un día.

---

# ACTIVIDAD 3. CONSTRUCCIÓN DEL ALGORITMO

## Algoritmo: construcción de un plan personalizado

### Inicio

1. Iniciar el programa.
2. Crear o recibir la lista `plan`.

### Entrada de información

3. Solicitar al usuario el nombre de un día.
4. Si el usuario escribe `fin`, terminar la construcción.
5. Solicitar la cantidad de actividades del día.
6. Solicitar para cada actividad:
   - nombre;
   - tipo;
   - lugar.

### Procesamiento

7. Crear una lista vacía para las actividades del día.
8. Recorrer la cantidad de actividades indicada.
9. Crear un registro con los datos de cada actividad.
10. Agregar cada actividad a la lista del día.
11. Agregar el día y sus actividades al `plan`.

### Repetición

12. Preguntar al usuario si desea agregar otro día.
13. Si responde `s`, volver a solicitar un nuevo día.
14. Si responde `n`, finalizar la construcción.

### Condiciones

15. Si el día es `fin`, finalizar.
16. Si una entrada de texto está vacía, solicitarla nuevamente.
17. Si la cantidad no es un entero válido, solicitarla nuevamente.

### Resultado

18. Mostrar que el plan fue actualizado.
19. Mostrar la cantidad de días registrados.

### Finalización

20. Devolver el `plan` actualizado al programa principal.

---

# ACTIVIDAD 4. CONSTRUCCIÓN DEL PSEUDOCÓDIGO

## Pseudocódigo de la construcción del plan

```text
INICIO

    plan ← lista existente o lista vacía

    MIENTRAS VERDADERO HACER

        MOSTRAR "Ingrese el día o escriba 'fin' para terminar"
        LEER dia

        MIENTRAS dia esté vacío HACER
            MOSTRAR "El día no puede estar vacío"
            LEER dia
        FIN MIENTRAS

        SI dia = "fin" ENTONCES
            SALIR DEL CICLO
        FIN SI

        actividades ← lista vacía

        MIENTRAS cantidad de actividades no sea válida HACER
            MOSTRAR "¿Cuántas actividades desea agregar?"
            LEER cantidad
        FIN MIENTRAS

        PARA numero DESDE 1 HASTA cantidad HACER

            MOSTRAR "Ingrese el nombre de la actividad"
            LEER nombre

            MIENTRAS nombre esté vacío HACER
                MOSTRAR "El nombre no puede estar vacío"
                LEER nombre
            FIN MIENTRAS

            MOSTRAR "Ingrese el tipo de actividad"
            LEER tipo

            MIENTRAS tipo esté vacío HACER
                MOSTRAR "El tipo no puede estar vacío"
                LEER tipo
            FIN MIENTRAS

            MOSTRAR "Ingrese el establecimiento o lugar"
            LEER lugar

            MIENTRAS lugar esté vacío HACER
                MOSTRAR "El lugar no puede estar vacío"
                LEER lugar
            FIN MIENTRAS

            actividad ← crear registro con nombre, tipo y lugar
            AGREGAR actividad A actividades

        FIN PARA

        dia_plan ← crear registro con dia y actividades
        AGREGAR dia_plan A plan

        MOSTRAR "¿Desea agregar otro día? (s/n)"
        LEER continuar

        SI continuar = "n" ENTONCES
            SALIR DEL CICLO
        FIN SI

    FIN MIENTRAS

    MOSTRAR cantidad de días del plan
    DEVOLVER plan

FIN
```

## Correspondencia entre algoritmo y pseudocódigo

| Elemento solicitado | Representación |
|---|---|
| Inicio | `INICIO` |
| Entrada | `LEER` |
| Procesamiento | Crear y almacenar actividades |
| Repetición | `MIENTRAS` y `PARA` |
| Condiciones | `SI` |
| Resultado | Mostrar y devolver `plan` |
| Finalización | `SALIR DEL CICLO` / `FIN` |

---

# ACTIVIDAD 5. IMPLEMENTACIÓN DEL CICLO `FOR`

La aplicación utiliza `for` cuando debe recorrer una cantidad determinada de actividades.

En `constructor_plan.py`:

```python
for numero in range(cantidad):
    nombre = pedir_texto(...)
    tipo = pedir_texto(...)
    lugar = pedir_texto(...)
```

También se utilizan `for` para recorrer la información almacenada en el plan.

La estructura es adecuada porque en este caso la cantidad de iteraciones ya fue indicada por el usuario.

---

# ACTIVIDAD 6. IMPLEMENTACIÓN DEL CICLO `WHILE`

La construcción del plan utiliza `while` porque el programa debe continuar solicitando información mientras el usuario desee seguir agregando días.

También se usa para validar entradas:

```python
while True:
    valor = input(mensaje).strip()

    if valor:
        return valor
```

El ciclo termina cuando se recibe un valor válido.

---

# ACTIVIDAD 7. CONDICIONES DENTRO DE LOS CICLOS

Las condiciones tienen funciones concretas:

### Validación

```python
if valor:
    return valor
```

Comprueba que el usuario no haya dejado el dato vacío.

### Finalización

```python
if dia.lower() == "fin":
    break
```

Permite terminar la construcción.

### Búsqueda

```python
if termino in actividad["nombre"].lower():
```

Determina si la actividad corresponde con la búsqueda.

### Actividad sin registros

```python
if not dia["actividades"]:
    continue
```

Determina si un día no tiene actividades.

---

# ACTIVIDAD 8. USO DE `BREAK`

## ¿En qué momento se debe interrumpir el ciclo?

Durante la búsqueda de una actividad, el ciclo debe interrumpirse cuando se encuentra la actividad solicitada.

También se interrumpe la construcción cuando el usuario indica que desea finalizar.

## ¿Qué condición produce la interrupción?

En la búsqueda:

```python
if termino in actividad["nombre"].lower():
    ...
    break
```

La interrupción ocurre cuando el término introducido por el usuario coincide con el nombre de una actividad.

En la construcción:

```python
if dia.lower() == "fin":
    break
```

La interrupción ocurre cuando el usuario escribe `fin`.

## ¿Qué debe hacer el programa después de interrumpir el ciclo?

### En la búsqueda

Debe dejar de recorrer elementos porque ya encontró la actividad solicitada y mostrar sus datos.

Como existe un ciclo externo y otro interno, se utiliza una variable `encontrada` para que el ciclo externo también pueda detenerse:

```python
if encontrada:
    break
```

### En la construcción

Debe finalizar la captura de nuevos días y devolver el plan actualizado.

## Implementación

La búsqueda utiliza:

```python
for dia in plan:
    for actividad in dia["actividades"]:
        if termino in actividad["nombre"].lower():
            ...
            encontrada = True
            break

    if encontrada:
        break
```

El `break` evita continuar recorriendo registros después de encontrar el resultado solicitado.

---

# ACTIVIDAD 9. USO DE `CONTINUE`

## ¿Qué elemento o caso debe omitirse?

Debe omitirse un día que no tenga actividades para mostrar.

La condición es:

```python
if not dia["actividades"]:
```

## ¿Por qué debe omitirse?

Porque no existen registros dentro de ese día que puedan ser mostrados. No es necesario ejecutar el resto del procesamiento correspondiente a las actividades.

## ¿Qué debe hacer el ciclo después?

Debe continuar con el siguiente día del plan.

## Implementación

```python
for dia in plan:

    if not dia["actividades"]:
        print("  Sin actividades.")
        continue

    for actividad in dia["actividades"]:
        ...
```

Cuando se ejecuta `continue`, el programa no procesa el resto del bloque correspondiente al día actual y pasa a la siguiente iteración del ciclo externo.

Esto permite que un día vacío no impida mostrar los demás días.

---

# ACTIVIDAD 10. CICLOS ANIDADOS

La información de PlanATi utilizada en este prototipo está organizada en diferentes niveles:

```text
PLAN
│
├── DÍA 1
│   ├── ACTIVIDAD 1
│   ├── ACTIVIDAD 2
│   └── ACTIVIDAD 3
│
├── DÍA 2
│   ├── ACTIVIDAD 1
│   └── ACTIVIDAD 2
│
└── DÍA 3
    └── ACTIVIDAD 1
```

Por esta organización es necesario recorrer primero los días y después las actividades pertenecientes a cada día.

## CICLO EXTERNO: ¿QUÉ INFORMACIÓN RECORRE?

El ciclo externo recorre los **días del plan**:

```python
for dia in plan:
```

Cada iteración obtiene un día diferente.

## CICLO INTERNO: ¿QUÉ INFORMACIÓN RECORRE?

El ciclo interno recorre las **actividades del día actual**:

```python
for actividad in dia["actividades"]:
```

Cada iteración obtiene una actividad perteneciente al día que está procesando el ciclo externo.

## ¿POR QUÉ ES NECESARIO UTILIZAR DOS CICLOS?

Porque la información está organizada en dos niveles.

Un único ciclo permitiría recorrer los días o las actividades, pero no permitiría procesar directamente todas las actividades pertenecientes a cada día.

Los dos ciclos permiten realizar el recorrido completo:

```text
Ciclo externo
    Día 1
        Ciclo interno
            Actividad 1
            Actividad 2
            Actividad 3

    Día 2
        Ciclo interno
            Actividad 1
            Actividad 2
```

## Implementación

```python
for dia in plan:

    if not dia["actividades"]:
        continue

    for numero, actividad in enumerate(
        dia["actividades"], start=1
    ):
        print(
            f"{numero}. {actividad['nombre']} | "
            f"{actividad['tipo']} | {actividad['lugar']}"
        )
```

La estructura responde directamente a la organización de los datos del plan.

---

# ESTRUCTURA DEL PROGRAMA

```text
Clase-6/
│
├── README.md
├── main.py
├── constructor_plan.py
├── buscar_actividad.py
├── ciclo_anidado.py
└── resumen_plan.py
```

## Ejecución

Requiere Python 3 y no necesita librerías externas.

Desde la carpeta del proyecto:

```bash
python main.py
```

El menú permite ejecutar las funcionalidades sobre el mismo `plan`:

```text
1. Crear / modificar plan
2. Buscar actividad en el plan
3. Ver plan organizado
4. Ver resumen del plan
0. Salir
```

## Relación de las funcionalidades con las actividades

| Funcionalidad | Estructura principal |
|---|---|
| Construcción del plan | `while` + `for` + condiciones |
| Validación de datos | `while` + `if` |
| Búsqueda de actividad | `for` anidado + `if` + `break` |
| Organización del plan | `for` anidado + `continue` |
| Resumen | `for` anidado + condiciones |

El código utiliza las estructuras únicamente donde tienen una función concreta dentro de la solución.
