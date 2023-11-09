import pickle
from globales import ALUMNOS, MATERIAS, INSCRIPCIONES
from Inscripcion import Inscripcion
from Fecha import Fecha
from Materia import Materia
from Alumno import Alumno
from os import path

ALUMNOS_CSV_FILENAME = "alumnos.tsv"
MATERIAS_CSV_FILENAME = "materias.tsv"
INSCRIPCIONES_CSV_FILENAME = "inscripciones.tsv"

ALUMNOS_BIN_FILENAME = "alumnos.bin"
MATERIAS_BIN_FILENAME = "materias.bin"
INSCRIPCIONES_BIN_FILENAME = "inscripciones.bin"


def read_positive_int(msg='Ingrese un número entero positivo: '):
    integer = ''
    while not integer.isdecimal():
        integer = input(msg)
        if not integer.isdecimal():
            print('¡Debe ingresar un número entero positivo!')
    return int(integer)

def escribir_binario_alumnos():
    with open(ALUMNOS_BIN_FILENAME, 'wb') as archivo_binario:
        pickle.dump(ALUMNOS, archivo_binario)

def escribir_binario_materias():
    with open(MATERIAS_BIN_FILENAME, 'wb') as archivo_binario:
        pickle.dump(MATERIAS, archivo_binario)

def escribir_binario_inscripciones():
    with open(INSCRIPCIONES_BIN_FILENAME, 'wb') as archivo_binario:
        pickle.dump(INSCRIPCIONES, archivo_binario)

def buscar_alumno_por_codigo_identificador(codigo_identificador):
    """
    Búsqueda binaria
        Precondición: lista de alumnos ordenada por código identificador
        Devuelve None si no existe un alumno con ese codigo_identificador.
        Devuelve la instancia del alumno cuyo codigo_identificador coincida.
    """
    izq = 0  # izq guarda el índice inicio del segmento
    der = len(ALUMNOS) - 1  # der guarda el índice fin del segmento
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        medio = round((izq + der) / 2)  # el punto medio del segmento
        if ALUMNOS[medio].obtener_codigo_identificador() == int(codigo_identificador):
            # si el codigo_identificador del alumno en la posición medio es igual al valor buscado,
            # devuelve el objeto alumno en la posición medio.
            return ALUMNOS[medio]
        elif ALUMNOS[medio].obtener_codigo_identificador() > int(codigo_identificador):
            der = medio - 1
        else:
            izq = medio + 1
    return None

def buscar_materia_por_codigo_identificador(codigo_identificador):
    """
        Búsqueda binaria
            Precondición: lista de materias ordenada por código identificador
            Devuelve None si no existe una materia con ese codigo_identificador.
            Devuelve la instancia de la materia cuyo codigo_identificador coincida.
        """
    izq = 0  # izq guarda el índice inicio del segmento
    der = len(MATERIAS) - 1  # der guarda el índice fin del segmento

    while izq <= der:
        medio = round((izq + der) / 2)  # el punto medio del segmento
        if MATERIAS[medio].obtener_codigo_identificador() == int(codigo_identificador):
            # si el codigo_identificador de la materia en la posición medio es igual al valor buscado,
            # devuelve el objeto materia en la posición medio.
            return MATERIAS[medio]
        elif MATERIAS[medio].obtener_codigo_identificador() > int(codigo_identificador):
            der = medio - 1
        else:
            izq = medio + 1
    return None

def inicializar_alumnos():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(ALUMNOS_CSV_FILENAME) and path.isfile(ALUMNOS_CSV_FILENAME):
        with open(ALUMNOS_CSV_FILENAME, encoding='utf-8') as archivo_tsv:
            todas_las_lineas = archivo_tsv.readlines()
            for linea in todas_las_lineas[1:]:
                columnas = linea[:-1].split('\t')
                p_id_alumno = int(columnas[0])
                p_nombre = columnas[1]
                p_apellido = columnas[2]
                p_genero = columnas[3]
                alumno = Alumno(p_id_alumno, p_nombre, p_apellido, p_genero)
                ALUMNOS.append(alumno)
        escribir_binario_alumnos()

def ordenamiento(constante, inicio, fin):
    if inicio > fin:
        return
    anterior = inicio
    posterior = fin
    pivot = constante[inicio]
    while anterior < posterior:
        while anterior < posterior and constante[posterior].obtener_codigo_identificador() > pivot.obtener_codigo_identificador():
            posterior = posterior - 1
        if anterior < posterior:
            constante[anterior] = constante[posterior]
            anterior = anterior + 1
        while anterior < posterior and constante[anterior].obtener_codigo_identificador() <= pivot.obtener_codigo_identificador():
            anterior = anterior + 1
        if anterior < posterior:
            constante[posterior] = constante[anterior]
            posterior = posterior - 1
        constante[anterior] = pivot
    ordenamiento(constante, inicio, anterior - 1)
    ordenamiento(constante, anterior + 1, fin)

def inicializar_materias():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(MATERIAS_CSV_FILENAME) and path.isfile(MATERIAS_CSV_FILENAME):
        with open(MATERIAS_CSV_FILENAME, encoding='utf-8') as archivo_tsv:
            todas_las_lineas = archivo_tsv.readlines()
            for linea in todas_las_lineas[1:]:
                columnas = linea[:-1].split('\t')
                p_id_materia = int(columnas[0])
                p_nombre = columnas[1]
                p_correlativas = columnas[2]
                materia = Materia(p_id_materia, p_nombre, p_correlativas)
                MATERIAS.append(materia)
        escribir_binario_materias()

def inicializar_inscripciones():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(MATERIAS_CSV_FILENAME) and path.isfile(MATERIAS_CSV_FILENAME):
        with open(INSCRIPCIONES_CSV_FILENAME, encoding='utf-8') as archivo_tsv:
            todas_las_lineas = archivo_tsv.readlines()
            for linea in todas_las_lineas[1:]:
                columnas = linea[:-1].split('\t')
                id_alumno = columnas[0]
                id_materia = columnas[1]
                fecha_desde_separado = columnas[2].split('/')
                fecha_desde = Fecha(int(fecha_desde_separado[0]), int(fecha_desde_separado[1]),
                                    int(fecha_desde_separado[2]))
                fecha_hasta_separado = columnas[3].split('/')
                fecha_hasta = Fecha(int(fecha_hasta_separado[0]), int(fecha_hasta_separado[1]),
                                    int(fecha_hasta_separado[2]))
                aprobado = True if columnas[4] == 'TRUE' else False
                inscripcion = Inscripcion(id_alumno, id_materia, fecha_desde, fecha_hasta, aprobado)
                INSCRIPCIONES.append(inscripcion)
        escribir_binario_inscripciones()

def menu_alumnos():
    print("*---- MENU ALUMNOS ----*")
    print()
    print("1- Añadir alumno")
    print("2- Mostrar alumnos")
    print("3- Actualizar alumno")
    print("4- Eliminar alumno")
    print("5- Volver a menu principal")

def menu_materias():
    print("*---- MENU MATERIAS ----*")
    print()
    print("1- Añadir materia")
    print("2- Mostrar materias")
    print("3- Actualizar materia")
    print("4- Eliminar materia")
    print("5- Volver a menu principal")

def menu_inscripciones():
    print("*---- MENU INSCRIPCIONES ----*")
    print()
    print("'1- Crear inscripción")
    print("2- Mostrar inscripción")
    print("3- Actualizar inscripción")
    print("4- Eliminar inscripción")
    print("5- Volver a menu principal")

def crear_alumno():
    p_id_alumno = read_positive_int("Ingrese el código del nuevo alumno: ")
    found=buscar_alumno_por_codigo_identificador(p_id_alumno)
    if found is None:
        p_nombre = input("Ingrese el nombre del nuevo alumno: ")
        while len(p_nombre) > 50:
            print("El nombre del alumno superó la cantidad máxima de caracteres")
            p_nombre = input("Ingrese el nombre del nuevo alumno nuevamente: ")

        p_apellido = input("Ingrese el apellido del nuevo alumno: ")
        while len(p_apellido) > 50:
            print("El nombre del alumno superó la cantidad máxima de caracteres (50)")
            p_apellido = input("Ingrese el nombre del nuevo alumno nuevamente: ")

        p_genero = ''
        while not (p_genero == 'M' or p_genero == 'F' or p_genero == 'O'):
            p_genero = input("Ingrese el genero del nuevo alumno: ").upper()
            if not (p_genero == 'M' or p_genero == 'F' or p_genero == 'O'):
                print("Debe ingresar un genero que contenga \"M\", \"F\" o \"O\" (M: Masculino, F: Femenino, O: Otro)")

        nuevo_alumno = Alumno(p_id_alumno, p_nombre, p_apellido, p_genero)
        ALUMNOS.append(nuevo_alumno)
        ordenamiento(ALUMNOS, 0, len(ALUMNOS) - 1)
        escribir_binario_alumnos()

        print(f"Se ha creado el alumno {nuevo_alumno}")
    else:
        print(f"Ya existe un alumno con el código {p_id_alumno}: {found}")

def actualizar_alumno():
    codigo_identificador = read_positive_int("Ingrese el codigo del alumno a actualizar: ")
    alumno = buscar_alumno_por_codigo_identificador(codigo_identificador)
    if alumno is not None:
        print(f"Actualizando alumno {alumno} ...")
        nombre = input("ingrese el nuevo nombre del Alumno (vacio para mantener el anterior): ")
        while len(nombre) > 50:
            print("El nuevo nombre del alumno superó la cantidad máxima de caracteres")
            nombre = input("Ingrese el nuevo nombre del alumno nuevamente: ")

        apellido = input("ingrese el nuevo apellido del Alumno (vacio para mantener el anterior): ")
        while len(apellido) > 50:
            print("El nuevo nombre del alumno superó la cantidad máxima de caracteres (50)")
            apellido = input("Ingrese el nuevo nombre del alumno nuevamente: ")

        genero = ''
        while not (genero == 'M' or genero == 'F' or genero == 'O'):
            genero = input("Ingrese el nuevo genero del alumno 'M' (Masculino), 'F' (Femenino), 'O' (Otro): ").upper()
            if not (genero == 'M' or genero == 'F' or genero == 'O'):
                print("Debe ingresar un genero que contenga \"M\", \"F\" o \"O\" (M: Masculino, F: Femenino, O: Otro)")
        alumno.actualizar(nombre, apellido, genero)

        print(f"El Alumno se actualizó correctamente {alumno}")
    else:
        print(f"No existe un alumno con código {codigo_identificador}")
    escribir_binario_alumnos()

def eliminar_alumno():
    codigo_identificador = read_positive_int("Ingrese el codigo del alumno a eliminar: ")
    alumno = buscar_alumno_por_codigo_identificador(codigo_identificador)
    if alumno is not None:
        print(f"Eliminando alumno {alumno} ...")
        ALUMNOS.remove(alumno)
    else:
        print(f"No existe un alumno con código {codigo_identificador}")
    escribir_binario_alumnos()

def crear_materia():
    p_id_materia = read_positive_int("Ingrese el código de la nueva materia: ")
    found=buscar_materia_por_codigo_identificador(p_id_materia)
    if found is None:
        p_nombre = input("Ingrese el nombre de la nueva materia: ")
        while len(p_nombre) > 100:
            print("El nombre de la materia superó la cantidad máxima de caracteres (100)")
            p_nombre = input("Ingrese el nombre del nuevo alumno nuevamente: ")

        correlativas = input("Ingrese las correlativas que tendrá la nueva materia: ")
        p_correlativas = int(correlativas) if correlativas != '' else ''

        nueva_materia = Materia(p_id_materia, p_nombre, p_correlativas)
        MATERIAS.append(nueva_materia)
        ordenamiento(MATERIAS, 0, len(MATERIAS) - 1)
        escribir_binario_materias()

        print(f"Se ha creado el alumno {nueva_materia}")
    else:
        print(f"Ya existe una materia con el código {p_id_materia}: {found}")

def actualizar_materia():
    codigo_identificador = read_positive_int("Ingrese el codigo de la materia a actualizar: ")
    materia = buscar_materia_por_codigo_identificador(codigo_identificador)
    if materia is not None:
        print(f"Actualizando materia {materia} ...")
        nombre = input("ingrese el nuevo nombre de la materia (vacio para mantener el anterior): ")
        while len(nombre) > 100:
            print("El nuevo nombre de la materia superó la cantidad máxima de caracteres (100)")
            nombre = input("Ingrese el nuevo nombre de la materia nuevamente: ")

        p_correlativas = input("Ingrese las correlativas que tendrá la nueva materia: ")
        correlativas = int(p_correlativas) if p_correlativas != '' else ''

        materia.actualizar(nombre, correlativas)
        print(f"La materia se actualizó correctamente {materia}")
    else:
        print(f"No existe una materia con código {codigo_identificador}")
    escribir_binario_materias()

def eliminar_materia():
    codigo_identificador = read_positive_int("Ingrese el codigo de la materia a eliminar: ")
    materia = buscar_materia_por_codigo_identificador(codigo_identificador)
    if materia is not None:
        print(f"Eliminando materia {materia} ...")
        MATERIAS.remove(materia)
    else:
        print(f"No existe una materia con código {codigo_identificador}")
    escribir_binario_materias()

def menu_principal():
    op = ''
    while op != '4':
        print("*---- MENU PRINCIPAL ----*")
        print()
        print("1- Gestión de alumnos")
        print("2- Gestión de materias")
        print("3- Gestión de inscripciones")
        print("4- Salir")
        print()
        op = input("Seleccione la opcion deseada: ")
        if op == '1':
            submenu_gestion_alumnos()
        elif op == '2':
            submenu_gestion_materias()
        elif op == '3':
            submenu_gestion_inscripciones()
        else:
            print("Saliendo del programa.../*")

def submenu_gestion_alumnos():
    OPCION_SALIR = '5'
    opcion = ''
    while opcion != OPCION_SALIR:
        menu_alumnos()
        print()
        opcion = input("Seleccione la opcion deseada: ")
        if opcion == '1':
            crear_alumno()
        elif opcion == '2':
            mostrar_todo_alumnos()
        elif opcion == '3':
            actualizar_alumno()
        elif opcion == '4':
            eliminar_alumno()
        elif opcion == '5':
            print("Saliendo del menu.../*")
            print()
        else:
            print("Opción invalida")

def submenu_gestion_materias():
    OPCION_SALIR = '5'
    opcion = ''
    while opcion != OPCION_SALIR:
        menu_materias()
        print()
        opcion = input("Seleccione la opcion deseada: ")
        if opcion == '1':
            crear_materia()
        elif opcion == '2':
            mostrar_todo_materias()
        elif opcion == '3':
            actualizar_materia()
        elif opcion == '4':
            eliminar_materia()
        elif opcion == '5':
            print("Saliendo del menu.../*")
            print()
        else:
            print("Opción invalida")

def submenu_gestion_inscripciones():
    OPCION_SALIR = '5'
    opcion = ''
    while opcion != OPCION_SALIR:
        menu_inscripciones()
        print()
        opcion = input("Seleccione la opcion deseada: ")
        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            print("Saliendo del menu.../*")
            print()
        else:
            print("Opción invalida")

def mostrar_todo_alumnos():
    for alumnos in ALUMNOS:
        print(alumnos)

def mostrar_todo_materias():
    for materias in MATERIAS:
        print(materias)

def mostrar_todo_inscripciones():
    for inscripcion in INSCRIPCIONES:
        print(inscripcion)

if path.exists(ALUMNOS_BIN_FILENAME) and path.isfile(ALUMNOS_BIN_FILENAME):
    with open(ALUMNOS_BIN_FILENAME, 'rb') as fd:
        ALUMNOS = pickle.load(fd)

if path.exists(MATERIAS_BIN_FILENAME) and path.isfile(MATERIAS_BIN_FILENAME):
    with open(MATERIAS_BIN_FILENAME, 'rb') as fd:
        MATERIAS = pickle.load(fd)

def inicializar():
    menu_principal()
    inicializar_inscripciones()


inicializar()
mostrar_todo_inscripciones()
