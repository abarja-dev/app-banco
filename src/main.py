"""
Módulo main que representa el menú principal de la app bancaria, con un bucle que permite usar el programa hasta que el
usuario decida salir
"""

from clases import Cliente
from src.funciones import crear_cliente, pedir_cantidad, limpiar_pantalla_simulada


# Función principal de saludo y menú
def inicio():
    limpiar_pantalla_simulada()

    print('*' * 58)
    print('*' * 15 + ' Bienvenido al Banco Plutón ' + '*' * 15)
    print('*' * 58)

    cliente = crear_cliente()

    # Bucle principal del menú
    salir = False
    while not salir:
        cliente.imprimir()
        print('\n¿Qué desea hacer?')
        print('[1] Retirar dinero')
        print('[2] Ingresar dinero')
        print('[3] Mostrar historial')
        print('[4] Salir')

        opcion = input('Seleccione una opción [1 - 4]: ')

        if opcion == '1':
            cantidad = pedir_cantidad('¿Cuánto dinero desea retirar?: ')
            exito = cliente.retirar(cantidad)
            if not exito:
                print('Lo siento, no tiene saldo suficiente para la operación.')
        elif opcion == '2':
            cantidad = pedir_cantidad('¿Cuánto dinero desea ingresar?: ')
            cliente.depositar(cantidad)
        elif opcion == '3':
            cliente.mostrar_historial()
        elif opcion == '4':
            print('Gracias por usar Banco Plutón. ¡Hasta pronto!')
            salir = True
        else:
            print('Opción inválida, inténtelo de nuevo.')

        input('\nPresione ENTER para continuar...')
        limpiar_pantalla_simulada()

if __name__ == '__main__':
    inicio()

