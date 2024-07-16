import pytest
from unittest.mock import patch
import sys
import time
import psutil

sys.path.append('C:\\Users\\cesar\\Desktop\\Proyecto_AuditoriaSoftware\\AudiitoriaSoftware')

from software import problematica_python as p

@pytest.fixture
def input_generator():
    def _input_generator(inputs):
        for item in inputs:
            yield item
        while True:
            yield ''
    return _input_generator

#Pruebas de ingreso e inicio de sesion de Usuarios
#Prueba de ingreso de Usuario
def test_ingresoUsuarios(input_generator):
    inputs = input_generator(["testuser", "password123", "John", "Doe", "john.doe@example.com"])
    with patch('builtins.input', lambda _: next(inputs)):
        p.ingresoUsuarios()
        assert "testuser" in p.usuarios
        assert p.usuarios["testuser"] == [1, "testuser", "password123", "John", "Doe", "john.doe@example.com"]

#Ingreso de Usuario con campo vacio
def test_ingreso_usuario_datos_invalidos(input_generator):
    inputs = input_generator(["", "password1234", "pepe", "Doe", "pepe.doe@example.com"])
    with patch('builtins.input', lambda _: next(inputs)):
        p.ingresoUsuarios()
        assert "" not in p.usuarios #cambiar a assert "" not in p.usuarios

def test_ingreso_usuario_duplicado(input_generator):
    inputs = input_generator(["testuser1", "password1234", "Janet", "Boe", "janet.boe@example.com"])
    with patch('builtins.input', lambda _: next(inputs)):
        p.ingresoUsuarios()

    inputs = input_generator(["testuser1", "password456", "Jane", "Smith", "jane.smith@example.com"])
    with patch('builtins.input', lambda _: next(inputs)):
        print(p.usuarios)
        p.ingresoUsuarios()
        print(p.usuarios)
        assert p.usuarios["testuser1"][2] == "password1234"
        assert p.usuarios["testuser1"][3] == "Jane"
 
#Prueba de Inicio de Sesion normal
def test_iniciar_sesion_exitoso(input_generator):
    inputs = input_generator(["testuser", "password123"])
    with patch('builtins.input', lambda _: next(inputs)):
        assert p.iniciar_sesion() == True

#Prueba de Inicio de Sesion con credenciales no validas
def test_iniciar_sesion_fallido(input_generator):
    inputs = input_generator(["testuser", "wrongpassword"])
    with patch('builtins.input', lambda _: next(inputs)):
        assert p.iniciar_sesion() == False #quizas cambiar a True pues ambos estan bien pues es falso ya que no puede iniciar sesion con credenciales invalidas

#Pruebas Unitarias de ingreso, modificacion, eliminacion de CLientes
#Prueba de Ingreso de Cliente
def test_ingresardatos(input_generator):
    inputs = input_generator(["12345678-9", "Jane", "Doe", "123 Main St", "555-1234", "jane.doe@example.com", "101", "10000"])
    with patch('builtins.input', lambda _: next(inputs)):
        p.ingresardatos()
        assert "12345678-9" in p.clientes
        assert p.clientes["12345678-9"] == [1, "12345678-9", "jane", "doe", "123 Main St", "555-1234", "jane.doe@example.com", "101", "10000", 0]

#Prueba de Ingreso de Cliente con campo vacio
def test_ingresodatos_invalido(input_generator):
    inputs = input_generator(["98765432-1", "", "Doe", "125 Main St", "44-12345", "pep.doe@example.com", "101", 2500])
    with patch('builtins.input', lambda _: next(inputs)):
        p.ingresardatos()
        assert "98765432-1" not in p.clientes 
        # assert p.clientes["98765432-1"] == [2, "98765432-1", "pepe", "doe", "125 Main St", "44-12345", "pep.doe@example.com", "101", "2500", 0]

#Mostrar Clientes
def test_mostrar_clientes(input_generator):
    with patch('builtins.print') as mock_print:
        p.mostrartodo()
        assert mock_print.called

#Mostrar un Cliente
def test_mostrar_cliente(input_generator):
    with patch('builtins.input', lambda _: "12345678-9"):
        with patch('builtins.print') as mock_print:
            p.mostraruno()
            assert mock_print.called

#Modificar Cliente
def test_modificardatos(input_generator):
    inputs = input_generator(["98765432-1", "si", "pepe", "no", "no", "no", "no", "no", "si", "2500", "no"])
    with patch('builtins.input', lambda _: next(inputs)):
        p.modificardatos()
        cliente = p.clientes["98765432-1"]
        assert cliente[2] == "pepe"
        assert cliente[8] == "2500"

#Eliminar Cliente
def test_eliminardatos(input_generator):
    with patch('builtins.input', lambda _: "98765432-1"):
        p.eliminardatos()
        assert "98765432-1" not in p.clientes


#Prueba de Integracion de Datos
def test_integracion_ingreso_modificacion_eliminacion(input_generator):
    # Ingresar Cliente
    inputs_in = input_generator(["98765432-1", "Jane", "Boe", "123 Main St", "554-321", "jane.boe@example.com", "101", "10000"])
    with patch('builtins.input', lambda _: next(inputs_in)):
        print(p.clientes)
        p.ingresardatos()
        print(p.clientes)
        assert "98765432-1" in p.clientes
    
    # Modificar Cliente
    inputs_mo = input_generator(["98765432-1", "si", "Janet", "no", "no", "no", "no", "no", "si", "20000", "no"])
    with patch('builtins.input', lambda _: next(inputs_mo)):
        p.modificardatos()
        assert p.clientes["98765432-1"][2] == "janet"
        assert p.clientes["98765432-1"][8] == "20000"
    
    # Eliminar Cliente
    with patch('builtins.input', lambda _: "98765432-1"):
        p.eliminardatos()
        assert "98765432-1" not in p.clientes


#Pruebas de tiempo
def test_tiempo_ingresar_datos(input_generator):
    start_time = time.time()
    inputs = input_generator(["11111111-1", "prueba", "de", "tiem", "555-1234", "prueba.tiempo@example.com", "101", "10000"])
    with patch('builtins.input', lambda _: next(inputs)):
        p.ingresardatos()
    end_time = time.time()
    assert end_time - start_time < 1  # Debe completarse en menos de 1 segundo

def test_tiempo_modificar_datos(input_generator):
    start_time = time.time()
    inputs = input_generator(["11111111-1", "no", "no", "si", "tiempo", "no", "no", "no", "no"])
    with patch('builtins.input', lambda _: next(inputs)):
        p.modificardatos()
    end_time = time.time()
    assert end_time - start_time < 1  

def test_tiempo_eliminar_datos(input_generator):
    start_time = time.time()
    with patch('builtins.input', lambda _: "11111111-1"):
        p.eliminardatos()
    end_time = time.time()
    assert end_time - start_time < 1  

def test_tiempo_integracion(input_generator):
    start_time = time.time()
    #Registro de cliente
    inputs_in = input_generator(["22222222-2", "prueba", "tiem", "po", "554-321", "prueba.tiempo@example.com", "101", "10000"])
    with patch('builtins.input', lambda _: next(inputs_in)):
        print(p.clientes)
        p.ingresardatos()
        print(p.clientes)
    
     # Modificar Cliente
    inputs_mo = input_generator(["22222222-2", "si", "Janet", "no", "no", "no", "no", "no", "si", "20000", "no"])
    with patch('builtins.input', lambda _: next(inputs_mo)):
        p.modificardatos()
    
    # Eliminar Cliente
    with patch('builtins.input', lambda _: "22222222-2"):
        p.eliminardatos()
        print(p.clientes)

    end_time = time.time()
    assert end_time - start_time < 1
    

def test_cpu_usage():
    process = psutil.Process()
    start_cpu = process.cpu_percent(interval=1)
    p.ingresardatos()
    end_cpu = process.cpu_percent(interval=1)
    assert end_cpu - start_cpu < 50  # Verificar que el uso de CPU esté por debajo del 50%