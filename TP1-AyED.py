'''
ALGORITMOS Y ESTRUCTURAS DE DATOS
TRABAJO PRÁCTICO  Nº 1
COMISIÓN 108

INTEGRANTES:
- BERNARD, BRUNO ALAN
- 
- 
- 
'''
#____________________________________________________________
# IMPORTAR LIBRERIAS
import getpass
import os
import time
#____________________________________________________________

# FUNCIONES QUE IMPRIMEN EL MENU Y LOS SUBMENUS
def imprimir_menu():
    os.system("cls")
    print("----------------------------------------")
    print("1. Gestion de locales.")
    print("2. Crear cuentas de dueños de locales.")
    print("3. Aprobar / Denegar solicitud de descuento.")
    print("4. Gestion de novedades.")
    print("5. Reporte de utilización de descuentos.")
    print("0. Salir")
    print("----------------------------------------")

def impimir_submenu_locales():
    os.system("cls")
    print("----------------------------------------")
    print("Bievenido a la gestión de locales!")
    print("\n")
    print("1. Crear locales.")
    print("2. Modificar local.")
    print("3. Eliminar local.")
    print("0. Volver.")
    print("----------------------------------------")

def imprimir_submenu_novedades():
    os.system("cls")
    print("----------------------------------------")
    print("Bievenido a la gestión de novedades!")
    print("\n")
    print("a) Crear novedades.")
    print("b) Modificar novedad.")
    print("c) Eliminar novedad.")
    print("d) Ver reporte de novedades.")
    print("e) Volver.")
    print("----------------------------------------") 

#____________________________________________________________
# FUNCIONES PARA LA CREACIÓN DE LOCALES

def aux(func, mm,i, p, c):
    if func(i, p, c) == i:
        local, num = "indumentaria", i
    elif func(i, p, c) == p:
        local, num = "perfumería", p
    elif func(i, p, c) == c:
        local, num = "comida", c
    else:
        local, num = "", ""
    
    rubro = f"El rubro con {mm} cantidad de locales es {local} y tiene {num} locales."
    return(rubro)

def cant_locales(i, p, c):
    condicion = "SI"
    while condicion == "SI":
        nombre = input("Nombre del local: ")
        ubicacion = input("Ubicación del local: ")
        rubro = input("Rubro del local: ")
        if rubro == "indumentaria":
            i += 1
        elif rubro == "perfumería":
            p += 1
        elif rubro == "comida":
            c += 1
        else:
            print("Rubro incorrecto.")
        condicion = input("Desea agregar otro local (SI/NO): ")

    mayor = aux(max, "más", i, p, c)
    menor = aux(min, "menos", i, p, c)
    return(mayor, menor)


def nuevo_local():
    cant_i = 0
    cant_p = 0
    cant_c = 0
    mayor, menor = cant_locales(cant_i, cant_p, cant_c)
    print(mayor)
    time.sleep(2)
    print(menor)
    time.sleep(2)

#____________________________________________________________
# FUNCION QUE IMPRIME EN CONTRUCCIÓN

def en_construccion():
    for i in range(5):
        print("En construcción...")
    time.sleep(2.5)

#____________________________________________________________
# FUNCIÓN DEL MENU

def menu():
    opcion = 1
    while opcion != 0:
        imprimir_menu()
        opcion = int(input("Ingrese su opcion: "))
        while (opcion<0 or opcion>5):
            time.sleep(1)
            opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                submenu_locales()
            case 2:
                en_construccion()
            case 3:
                en_construccion()
            case 4:
                submenu_novedades()
            case 5:
                en_construccion()
            case 0:
                os.system("cls")
                print("¡Gracias por usar el menú!")
                print("¡Vuelva pronto!")
                time.sleep(3)
                os.system("cls")

#____________________________________________________________
# FUNCIONES DE LOS SUBMENU

def submenu_locales():
    opcion = 1
    while opcion != 0:
        impimir_submenu_locales()
        opcion = int(input("Ingrese su opcion: "))
        while (opcion<0 or opcion>3):
            opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                nuevo_local()
            case 2:
                en_construccion()
            case 3:
                en_construccion()

def submenu_novedades():
    opcion = 1
    while opcion != 0:
        imprimir_submenu_novedades()
        opcion = int(input("Ingrese su opcion: "))
        while (opcion<0 or opcion>3):
            opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                en_construccion()
            case 2:
                en_construccion()
            case 3:
                en_construccion()
            case 4:
                en_construccion()

#____________________________________________________________
# FUNCIONES PARA EL VERIFICADO DEL USUARIO Y EL INICIO DE SESION

def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    return(usuario, password)

def verificar(usuario, password):
    user_adm = "admin" #"admin@shopping.com"
    pass_adm = "12345"
    intentos = 0
    while intentos < 2:
        if usuario == user_adm and password == pass_adm:
            return True
        else:
            intentos += 1
            os.system("cls")
            print("---------------------------")
            print("Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
            iniciar_sesion()
    os.system("cls")
    print("Se ha intentado 3 veces erroneamente.")
    print("Cerrando el programa.")
    time.sleep(2)
    os.system("cls")
    return False

#____________________________________________________________
# FUNCIÓN PRINCIPAL

def main():
    usuario, contraseña = iniciar_sesion()
    verificado = verificar(usuario, contraseña)
    if verificado:
        menu()

main()