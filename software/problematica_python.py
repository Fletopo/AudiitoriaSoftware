import os
import time
import sys
import tkinter as tk
from tkinter import messagebox

clientes = {}
usuarios = {
    'admin': [1, 'admin', 'Admin', 'User', '1234567890', 'admin@empresa.com', 'admin_password', 'admin']
}
idcliente = 0
idusuario = 1

def alerta(mensaje):
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)
    messagebox.showinfo("Advertencia", mensaje)
    root.destroy()

def carga_i(iteraciones, espera=0.1):
    for i in range(iteraciones):
        relleno = chr(9608) * (i + 1)  
        sys.stdout.write(f'\r[{relleno.ljust(iteraciones)}]')
        sys.stdout.flush()
        time.sleep(espera)
    print()  

def carga_e():
    mensajes = ["Cargando.", "Cargando..", "Cargando..."]
    for _ in range(1):
        for msg in mensajes:
            limpiarPantalla()
            print(msg)
            time.sleep(1)

def limpiarPantalla():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

def menuprincipal(tipo_usuario):
    limpiarPantalla()
    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")
    if tipo_usuario[0] == "admin":
        print("       1.- REGISTRAR USUARIO    ")
        print("       2.- ELIMINAR USUARIO     ")
        print("       3.- SALIR DE LA SESIÓN   ")
    elif tipo_usuario[0] == "trabajador":
        print("       1.- PERFIL               ")
        print("================================")
        print("       2.- INGRESAR CLIENTE     ")
        print("       3.- MOSTRAR CLIENTES     ")
        print("       4.- MODIFICAR CLIENTE    ")
        print("       5.- ELIMINAR CLIENTE     ")
        print("       6.- SALIR DE LA SESIÓN   ")
    print("================================")

def ingresardatos():
    limpiarPantalla()
    global clientes, idcliente
    print("=================================")
    print("     INGRESAR DATOS CLIENTE      ")
    print("=================================")
    run = input("INGRESE RUN : ").strip()
    nombre = input("INGRESE NOMBRE : ").lower()
    apellido = input("INGRESE APELLIDO : ").lower()
    direccion = input("INGRESE DIRECCION : ").title()
    telefono = input("INGRESE TELEFONO : ").strip()
    correo = input("INGRESE CORREO : ").strip()
    tipos = [[101, "Plata"], [102, "Oro"], [103, "Platino"]]
    print("TIPO DE CLIENTE")
    for tipo in tipos:
        print(" CODIGO : {} - {}.".format(tipo[0], tipo[1]))
    tipo_codigo = input("Ingrese el codigo del Tipo de Cliente: ").strip()
    
    tipo_map = {str(codigo): tipo for codigo, tipo in tipos}
    tipo = tipo_map.get(tipo_codigo)

    monto = input("INGRESE MONTO CREDITO : ").strip()
    
    if not (run and nombre and apellido and direccion and telefono and correo and tipo and monto):
        alerta("Todos los campos son obligatorios.")
        return
    
    try:
        monto = int(monto)
    except ValueError:
        alerta("Monto de crédito debe ser un número entero.")
        return

    if run in clientes:
        alerta("El RUN ya está registrado.")
        return

    carga_e()
    idcliente += 1
    cliente = [idcliente, run, nombre, apellido, direccion, telefono, correo, tipo, monto, 0]
    clientes[run] = cliente
    alerta("cliente ingresado exitosamente")

def mostrar():
    while True:
        limpiarPantalla()
        print("================================")
        print("     M E N Ú  M O S T R A R     ")
        print("================================")
        print("       1.- MOSTRAR TODO         ")
        print("       2.- MOSTRAR UNO          ")
        print("       3.- MOSTRAR PARCIAL      ")
        print("       4.- VOLVER               ")
        print("================================")
        opm = int(input("  INGRESE OPCIÓN : "))
        if opm == 1:
            mostrartodo()
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
        elif opm == 2:
            mostraruno()
        elif opm == 3:
            mostrarparcial()
        elif opm == 4:
            break
        else:
            pass

def mostrartodo():
    limpiarPantalla()
    print("=================================")
    print("  MUESTRA DE TODOS LOS CLIENTES  ")
    print("=================================")
    for cliente, dato in clientes.items():
        print(" ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO DE CLIENTE : {} ".format(
            dato[0], cliente, dato[2], dato[3], dato[4], dato[5], dato[6], dato[8], dato[9], dato[7]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def mostraruno():
    limpiarPantalla()
    print("=================================")
    print("   MUESTRA DE DATOS PARTICULAR   ")
    print("=================================")
    try:
        op = input("\n Ingrese valor del Run del Cliente que desea Mostrar los Datos : ").strip()
        if op in clientes:
            datos = clientes.get(op)
            limpiarPantalla()
            print(datos)
            print("\n=======================================")
            print("    MUESTRA  DE  DATOS  DEL   CLIENTE   ")
            print("=======================================")
            print(" ID               : {} ".format(datos[0]))
            print(" RUN              : {} ".format(datos[1]))
            print(" NOMBRE           : {} ".format(datos[2]))
            print(" APELLIDO         : {} ".format(datos[3]))
            print(" DIRECCION        : {} ".format(datos[4]))
            print(" FONO             : {} ".format(datos[5]))
            print(" CORREO           : {} ".format(datos[6]))
            print(" TIPO DE CLIENTE  : {} ".format(datos[7]))
            print(" MONTO CREDITO    : {} ".format(datos[8]))
            print(" DEUDA            : {} ".format(datos[9]))
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
            for cliente, dato in datos:
                print(" ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO DE CLIENTE : {} ".format(
                    dato[0], cliente, dato[2], dato[3], dato[4], dato[5], dato[6], dato[9], dato[7], dato[8]))
                print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
    except ValueError:
        pass

def modificardatos():
    tipos = [[101, "Plata"], [102, "Oro"], [103, "Platino"]]
    tipo_map = {str(codigo): tipo for codigo, tipo in tipos}

    listanuevos = []
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
    listanuevos.append(datos[0])
    listanuevos.append(datos[1])
    for i in range(2, 10):
        nuevo_valor = input(f"DESEA MODIFICAR {['NOMBRE', 'APELLIDO', 'DIRECCION', 'FONO', 'CORREO', 'TIPO', 'MONTO CREDITO', 'DEUDA'][i-2]} : {datos[i]} - [SI/NO] ").strip().lower()
        if nuevo_valor == "si":
            valor = input(f"INGRESE NUEVO {['NOMBRE', 'APELLIDO', 'DIRECCION', 'FONO', 'CORREO', 'TIPO', 'MONTO CREDITO', 'DEUDA'][i-2]} : ").strip()
            if valor:
                if i == 7: 
                    if valor not in tipo_map:
                        alerta("Tipo de cliente no válido.")
                        return
                    else:
                        valor = tipo_map.get(valor)
                if i == 8:  # Si es el monto de crédito
                    try:
                        valor = int(valor)
                    except ValueError:
                        alerta("Monto de crédito debe ser un número entero.")
                        return
                listanuevos.append(valor)
            else:
                listanuevos.append(datos[i])
        else:
            listanuevos.append(datos[i])
    clientes[mod] = listanuevos
    carga_e()
    time.sleep(2)
    alerta("Datos modificados correctamente")

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
            carga_e()
            time.sleep(2)
            alerta("Cliente eliminado exitosamente.")
        else:
            alerta("El cliente no ha sido encontrado")
    except ValueError:
        pass

def crear_username(nombre, apellido):
    b_username = (nombre + apellido[0]).lower()
    suffix = 1
    username = b_username
    while username in usuarios:
        username = f"{b_username}{suffix}"
        suffix += 1
    return username

def crear_correo(nombre, apellido):
    b_correo = f"{nombre}.{apellido}"
    suffix = 1
    correo = f"{b_correo}@empresa.com"
    while correo in usuarios:
        correo = f"{b_correo}{suffix}@empresa.com"
        suffix += 1
    return correo

def registrardatosusuario():
    limpiarPantalla()
    global usuarios, idusuario
    print("=================================")
    print("     REGISTRAR DATOS USUARIO     ")
    print("=================================")
    nombre = input("INGRESE NOMBRE : ").strip().lower()
    apellido = input("INGRESE APELLIDO : ").strip().lower()
    telefono = input("INGRESE FONO : ").strip()
    password = input("INGRESE PASSWORD : ").strip()
    while True:
        print("\n[1] - TRABAJADOR")
        print("[2] - ADMINISTRADOR")
        tipo = input("INGRESE TIPO DE USUARIO : ").strip()
        if tipo in ["1", "2"]:
            tipo = "trabajador" if tipo == "1" else "admin"
            break
        else:
            print("Tipo de usuario no válido. Intente nuevamente.")

    if not (nombre or apellido or telefono or password ):
        alerta("Todos los campos son obligatorios.")
        return
    
    username = crear_username(nombre, apellido)
    correo = crear_correo(nombre, apellido)

    idusuario += 1
    usuario = [idusuario, username, nombre, apellido, telefono, correo, password, tipo]
    usuarios[username] = usuario
    carga_e()
    time.sleep(2)
    alerta(f"Usuario registrado exitosamente. \nNombre de Usuario: {username}. \ncorreo: {correo}")

def eliminarusuario():
    limpiarPantalla()
    print("===================================")
    print("      MODULO ELIMINAR USUARIO      ")
    print("===================================")
    for username, usuario in usuarios.items():
        print(f"USERNAME : {username} - NOMBRE : {usuario[2]} - APELLIDO : {usuario[3]}")
    try:
        elim = input("\nIngrese el nombre de usuario que desea Eliminar : ").strip().lower()
        if elim in usuarios:
            del usuarios[elim]
            carga_e()
            time.sleep(2)
            alerta("Usuario eliminado exitosamente.")
        else:
            alerta("El usuario no ha sido encontrado")
    except ValueError:
        pass

def iniciar_sesion():
    print("===================================")
    print("          INICIO DE SESION         ")
    print("===================================")
    username = input("INGRESE USERNAME : ").strip().lower()
    password = input("INGRESE PASSWORD : ").strip()
    carga_e()
    if username in usuarios and usuarios[username][6] == password:
        carga_e()
        time.sleep(2)
        limpiarPantalla()
        print(f"Bienvenido {usuarios[username][2]} {usuarios[username][3]} ({usuarios[username][7]})")
        time.sleep(2)
        return [usuarios[username][7], username]
    else:
        alerta("Nombre de Usuario o Contraseña Incorrectos.")
        return None

def perfil(username):
    usuario = usuarios.get(username)
    if usuario:
        print(f"\nID: {usuario[0]}")
        print(f"Nombre: {usuario[2]} {usuario[3]}")
        print(f"Telefono: {usuario[4]}")
        print(f"Correo: {usuario[5]}")
        print(f"Tipo: {usuario[7]}")
        input("\n\n PRESIONE ENTER PARA CONTINUAR")

def main():
    carga_i(80)
    while True:
        limpiarPantalla()
        sesion = iniciar_sesion()
        if not sesion:
            continue
        while True:
            menuprincipal(sesion)
            opcion = input("\nINGRESE OPCIÓN : ").strip()
            if sesion[0] == "admin":
                if opcion == "1":
                    registrardatosusuario()
                elif opcion == "2":
                    eliminarusuario()
                elif opcion == "3":
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            elif sesion[0] == "trabajador":
                if opcion == "1":
                    perfil(sesion[1])
                elif opcion == "2":
                    ingresardatos()
                elif opcion == "3":
                    if len(clientes) > 0:
                        mostrar()            
                    else:
                        onc = input("Todavia no hay clientes ingresados\n Desea Ingresar uno? [SI/NO]: ")                
                        if onc.lower() == "si":          
                            ingresardatos()            
                        else:
                            pass
                elif opcion == "4":
                    if len(clientes) > 0:
                        modificardatos()
                    else:
                        onc = input("Todavia no hay clientes ingresados\n Desea Ingresar uno? [SI/NO]: ")
                        if onc.lower() == "si":
                            ingresardatos()
                        else:
                            pass
                elif opcion == "5":
                    if len(clientes) > 0:                  
                        eliminardatos()
                    else:
                        onc = input("Todavia no hay clientes ingresados\n Desea Ingresar uno? [SI/NO]: ")               
                        if onc.lower() == "si":                
                            ingresardatos()                 
                        else:
                            pass
                elif opcion == "6":
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
