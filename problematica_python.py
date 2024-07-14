import os
import tkinter as tk
from tkinter import messagebox

clientes = {}
usuarios = {}
idcliente = 0
idusuario = 0

def alerta(mensaje):

    root = tk.Tk()
    root.withdraw()  
    root.lift()
    root.attributes('-topmost', True)
    messagebox.showinfo("Advertencia", mensaje)
    root.destroy()  

def limpiarPantalla():
    
    if os.name == "nt":
        
        os.system('cls')

    else:
        os.system("clear")

def menuprincipal():

    limpiarPantalla()

    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")
    print("       1.- (C) INGRESAR         ")
    print("       2.- (R) MOSTRAR          ")
    print("       3.- (U) MODIFICAR        ")
    print("       4.- (D) ELIMINAR         ")
    print("       5.- (E) Salir            ")
    print("================================")

def menumostrar():

    limpiarPantalla()

    print("================================")
    print("     M E N Ú  M O S T R A R     ")
    print("================================")
    print("       1.- MOSTRAR TODO         ")
    print("       2.- MOSTRAR UNO          ")
    print("       3.- MOSTRAR PARCIAL      ")
    print("       4.- VOLVER               ")
    print("================================")

def ingresardatos():

    limpiarPantalla()

    print("=================================")
    print("     INGRESAR DATOS CLIENTE      ")
    print("=================================")

    run = input("INGRESE RUN : ")
    nombre=input("INGRESE NOMBRE : ").lower()
    apellido=input("INGRESE APELLIDO : ").lower()
    direccion=input("INGRESE DIRECCION : ").title()
    fono=input("INGRESE TELEFONO : ")
    correo=input("INGRESE CORREO : ")
    tipos = [
        [101,"Plata"],[102,"Oro"],[103,"Platino"]
    ]

    print("--------------------------------------------")

    for tipo in tipos:

        print(
            " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
        
    print("--------------------------------------------")

    tipo = input("Ingrese el codigo del Tipo de Cliente: ")
    monto=input("INGRESE MONTO CREDITO : ")

    global idcliente    
    idcliente += 1
    codigo = idcliente
    deuda = 0
    cliente = [codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda]
    clientes[run]=cliente

def mostrar():

    while(True):

        menumostrar()
        op2 = int(input("  INGRESE OPCIÓN : "))

        if op2 == 1:

            mostrartodo()
            input("\n\n PRESIONE ENTER PARA CONTINUAR")

        elif op2 == 2:

            mostraruno()

        elif op2 == 3:

            mostrarparcial()

        if op2 == 4:

            break

        else:
            pass

def mostrartodo():

    limpiarPantalla()

    print("=================================")
    print("  MUESTRA DE TODOS LOS CLIENTES  ")
    print("=================================")

    for cliente,dato in clientes.items():

        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                dato[0], cliente, dato[2], dato[3], dato[4], dato[5], dato[6] , dato[8], dato[9], dato[7]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def mostraruno():

    limpiarPantalla()

    print("=================================")
    print("   MUESTRA DE DATOS PARTICULAR   ")
    print("=================================")

    try:

        op=input("\n Ingrese valor del Run del Cliente que desea Mostrar los Datos : ").strip()
    
        if op in clientes:

            datos = clientes.get(op)

            limpiarPantalla()

            print(datos)
            print("\n=======================================")
            print("    MUESTRA  DE  DATOS  DEL   CLIENTE   ")
            print("=======================================")
            print(" ID            : {} ".format(datos[0]))
            print(" RUN           : {} ".format(datos[1]))
            print(" NOMBRE        : {} ".format(datos[2]))
            print(" APELLIDO      : {} ".format(datos[3]))
            print(" DIRECCION     : {} ".format(datos[4]))
            print(" FONO          : {} ".format(datos[5]))
            print(" CORREO        : {} ".format(datos[6]))
            print(" TIPO          : {} ".format(datos[9]))
            print(" MONTO CREDITO : {} ".format(datos[7]))
            print(" DEUDA         : {} ".format(datos[8]))
            print("-----------------------------------------")
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
        
        else:
            alerta("El cliente no ha sido encontrado")

    except ValueError:
        pass

def mostrarparcial():

    limpiarPantalla()

    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")

    try:

        cant_cli = len(clientes)
        cant = int(input("\nIngrese la Cantidad de Clientes a Mostrar : "))
        
        if cant > cant_cli:
            
            alerta(f"La cantidad excede el numero de clientes. \n Clientes registrados: {cant_cli}")
        
        else:
            datos = list(clientes.items())[:cant]
            
            limpiarPantalla()
            
            for cliente,dato in datos:

                print(
                    " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                        dato[0], cliente, dato[2], dato[3], dato[4], dato[5], dato[6] , dato[9], dato[7], dato[8]))
                print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            
            input("\n\n PRESIONE ENTER PARA CONTINUAR")

    except ValueError:
        pass

def modificardatos():

    listanuevos=[]

    limpiarPantalla()

    print("===================================")
    print("      MODULO MODIFICAR CLIENTE     ")
    print("===================================")

    mostrartodo()
    mod = input("\n Ingrese valor del Run del Cliente que desea Modificar : ").strip()
    
    if mod not in clientes:
        alerta("El dato o run ingresado es invalido")
        return
    
    datos = clientes.get(mod)
    
    print(" ID         : {} ".format(datos[0]))
    listanuevos.append(datos[0])
    print(" RUN        : {} ".format(datos[1]))
    listanuevos.append(datos[1])

    opm=input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[2]))

    if opm.lower() == "si":

        nombrenuevo=input("INGRESE NOMBRE : ").lower()
        listanuevos.append(nombrenuevo)

    else:
        listanuevos.append(datos[2])

    opm = input("DESEA MODIFICAR EL APELLIDO : {} - [SI/NO] ".format(datos[3]))
    
    if opm.lower() == "si":

        apellidonuevo= input("INGRESE APELLIDO : ").lower()
        listanuevos.append(apellidonuevo)

    else:
        listanuevos.append(datos[3])

    opm = input("DESEA MODIFICAR LA DIRECCION : {} - [SI/NO] ".format(datos[4]))
    
    if opm.lower() == "si":

        direcnueva = input("INGRESE DIRECCION : ").title()
        listanuevos.append(direcnueva)

    else:
        listanuevos.append(datos[4])

    opm = input("DESEA MODIFICAR EL TELEFONO : {} - [SI/NO] ".format(datos[5]))
    
    if opm.lower() == "si":

        fononuevo= input("INGRESE TELEFONO : ")
        listanuevos.append(fononuevo)

    else:
        listanuevos.append(datos[5])

    opm = input("DESEA MODIFICAR EL CORREO : {} - [SI/NO] ".format(datos[6]))
    
    if opm.lower() == "si":

        correonuevo = input("INGRESE EL CORREO : ")
        listanuevos.append(correonuevo)

    else:
        listanuevos.append(datos[6])

    opm = input("DESEA MODIFICAR LA DEUDA : {} - [SI/NO] ".format(datos[9]))
    
    if opm.lower() == "si":

        deudanuevo= input("INGRESE DEUDA : ")
        listanuevos.append(deudanuevo)
    
    else:
        listanuevos.append(datos[9])
    
    opm = input("DESEA MODIFICAR EL MONTO DE CREDITO : {} - [SI/NO] ".format(datos[8]))
    
    if opm.lower() == "si":

        montonuevo= input("INGRESE MONTO DE CREDITO : ")
        listanuevos.append(montonuevo)

    else:
        listanuevos.append(datos[8])

    opm = input("DESEA MODIFICAR EL TIPO : {} - [SI/NO] ".format(datos[7]))
    
    if opm.lower() == "si":

        tipos = [
            [101,"Plata"],[102,"Oro"],[103,"Platino"]
        ]

        print("--------------------------------------------")
        
        for tipo in tipos:
            print(
                " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
        
        print("--------------------------------------------")
        
        tiponuevo = input("INGRESE EL TIPO : ")
        listanuevos.append(tiponuevo)

    else:
        listanuevos.append(datos[7])
    
    clientes[mod]=listanuevos


def eliminardatos():

    limpiarPantalla()

    print("===================================")
    print("      MODULO ELIMINAR CLIENTE      ")
    print("===================================")

    mostrartodo()

    try:

        elim = input("Ingrese valor del Run del Cliente que desea Eliminar : ").strip()     
        
        if elim in clientes:
            
            del clientes[elim]
            print("Cliente eliminado exitosamente.")
        
        else:
            alerta("El cliente no ha sido encontrado")

    except ValueError:
        pass

# --------------------------------------

def menuUsuarios():

    limpiarPantalla()

    print("================================")
    print("   M E N Ú  U S U A R I O S     ")
    print("================================")
    print("       1.-  INICIAR SESIÓN      ")
    print("       2.-  REGISTRAR USUARIO   ")
    print("       3.-  Salir               ")
    print("================================")

def ingresoUsuarios():

    limpiarPantalla()

    print("=======================================")
    print("        INGRESO DE USUARIO             ")
    print("=======================================")

    username = input( "INGRESE NOMBRE DE USUARIO:  ")
    clave = input( "INGRESE PASSWORD         : ")
    nombre = input(   "INGRESE NOMBRE           : ")
    apellidos = input("INGRESE APELLIDOS        : ")
    correo = input(   "INGRESE CORREO           : ")

    print("=======================================")

    global idusuario
    idusuario += 1
    codigo = idusuario
    usuario = [codigo,username,clave,nombre,apellidos,correo]
    usuarios[username] = usuario


while True:

    menuUsuarios()

    try:
        
        opUsu = int(input("INGRESE OPCIÓN: "))

        if opUsu == 1:

            limpiarPantalla()

            user = input("Ingrese nombre de usuario: ")

            limpiarPantalla()

            clave = input("Ingrese password: ")

            limpiarPantalla()

            if usuarios.get(user):

                usuario = usuarios.get(user)

                if usuario[2] == clave:

                    print(f"Bienvenido {usuario[3]} {usuario[4]} - {usuario[2]} - id: {usuario[0]}.")
                    input("Presiona ENTRAR para ingresar al Menú Principal.")

                    while True:  # Bucle para el Menú Principal
                        
                        menuprincipal()

                        try:

                            op = int(input("INGRESE OPCIÓN: "))
                            
                            if op == 1:
                            
                                ingresardatos()
                            
                            elif op == 2:
                                
                                if len(clientes) > 0:

                                    mostrar()
                                
                                else:
                                    onc = input("Todavia no hay clientes ingresados\n Desea Ingresar uno? [SI/NO]: ")
                                    
                                    if onc.lower() == "si":
                                    
                                        ingresardatos()
                                    
                                    else:
                                        pass
                            
                            elif op == 3:

                                if len(clientes) > 0:

                                    modificardatos()

                                else:
                                    onc = input("Todavia no hay clientes ingresados\n Desea Ingresar uno? [SI/NO]: ")
                                    
                                    if onc.lower() == "si":
                                    
                                        ingresardatos()
                                    
                                    else:
                                        pass

                            elif op == 4:
                                
                                if len(clientes) > 0:
                                    
                                    eliminardatos()

                                else:
                                    onc = input("Todavia no hay clientes ingresados\n Desea Ingresar uno? [SI/NO]: ")
                                    
                                    if onc.lower() == "si":
                                    
                                        ingresardatos()
                                    
                                    else:
                                        pass

                            elif op == 5:
                            
                                opSalir = input("¿DESEA SALIR [SI/NO]: ")
                            
                                if opSalir.lower() == "si":
                            
                                    break  # Salir del bucle del Menú Principal
                            else:
                                pass

                        except ValueError:
                            pass

                    break  # Salir del bucle del Menú de Usuarios
                else:
                    input("Contraseña incorrecta. Presiona ENTER para volver al Menú de Usuarios.")
            else:
                input("Usuario no registrado. Presiona ENTER para volver al Menú de Usuarios.")
    
        elif opUsu == 2:

            ingresoUsuarios()

        elif opUsu == 3:

            opSalir = input("¿DESEA SALIR [SI/NO]: ")

            if opSalir.lower() == "si":
                break
        else:
            pass

    except ValueError:
        
        pass