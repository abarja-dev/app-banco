"""
Funciones auxiliares de la app bancaria
"""


from src.clases import Cliente


# Función que pide datos al usuario por la consola y devuelve un objeto Cliente
def crear_cliente():
    nombre = input('Por favor, ingrese su nombre: ')
    apellido = input('Por favor, ingrese su apellido: ')
    numero_cuenta = input('Por favor, ingrese su número de cuenta: ')
    balance_inicial = 5000

    cliente = Cliente(nombre, apellido, numero_cuenta, balance_inicial)
    return cliente


# Función para pedir un número float al usuario como cantidad, con validación.
def pedir_cantidad(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            cantidad = float(entrada)
            if cantidad <= 0:
                print('Por favor, ingrese un número positivo')
                continue
            return cantidad
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

# Función que simula una limpieza de pantalla, para evitar problemas de incompatibilidades de SO
def limpiar_pantalla_simulada():
    print('\n' + '-'*58 + '\n')

