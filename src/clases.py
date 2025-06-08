"""
Módulo con las clases del proyecto de la app bancaria
"""


from datetime import datetime


# Clase que representa a una persona
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Clase que representa a un cliente, que a su vez es un objeto Persona
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)

        # Datos de la cuenta
        self.numero_cuenta = numero_cuenta
        self.balance = balance

        # Lista con el historial de movimientos
        self.historial = []

    # Metodo que carga un saludo inicial y los datos del cliente
    def imprimir(self):
        print('*'*18 + ' BANCO PLUTÓN ' + '*'*18)
        print('-'*50)
        print(f'Bienvenido {self.nombre} {self.apellido}')
        print(f'Tu número de cuenta es: {self.numero_cuenta}')
        print(f'El saldo de tu cuenta es: {self.balance}')

    # Metodo para depositar fondos
    def depositar(self, cantidad):
        if cantidad <= 0:
            return
        self.balance += cantidad
        self.historial.append((datetime.now(), 'Depósito', cantidad))
        print('Depósito aceptado')

    # Metodo para retirar fondos
    def retirar(self, cantidad):
        if cantidad <= 0:
            return False
        if cantidad <= self.balance:
            self.balance -= cantidad
            self.historial.append((datetime.now(), 'Retiro', cantidad))
            print('Por favor, recoja su dinero')
            return True
        else:
            print('No tiene saldo suficiente')
            return False

    # Metodo para mostrar el historial de movimientos
    def mostrar_historial(self):
        print(f'Historial de movimientos de la cuenta {self.numero_cuenta}:')
        for fecha, tipo, monto in self.historial:
            print(f'{fecha.strftime("%d-%m-%Y %H:%M:%S")} - {tipo}: {monto} €')

