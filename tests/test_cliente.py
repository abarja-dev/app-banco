"""
Testeo de la clase cliente con unittest, verifica los métodos de depósito, retiro y manejo del historial de movimientos
"""

import unittest
from datetime import datetime
from src.clases import Cliente

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente('Licinus', 'Crasus', '12345', 1000)

    # Prueba que el metodo depositar actualiza balance e historial correctamente
    def test_depositar(self):
        self.cliente.depositar(500)
        self.assertEqual(self.cliente.balance, 1500)
        self.assertEqual(len(self.cliente.historial), 1)
        fecha, tipo,  monto = self.cliente.historial[-1]
        self.assertEqual(tipo, 'Depósito')
        self.assertEqual(monto, 500)

    # Prueba que el metodo retirar actualiza balance e historial correctamente cuando existe saldo suficiente
    def test_retirar_suficiente_saldo(self):
        exito = self.cliente.retirar(400)
        self.assertTrue(exito)
        self.assertEqual(self.cliente.balance, 600)
        self.assertEqual(len(self.cliente.historial), 1)
        fecha, tipo, monto = self.cliente.historial[-1]
        self.assertEqual(tipo, 'Retiro')
        self.assertEqual(monto, 400)

    # Prueba que el metodo retirar mantiene el balance y actualiza el historial correctamente cuando no existe saldo
    # suficiente
    def test_retirar_saldo_insuficiente(self):
        exito = self.cliente.retirar(2000)
        self.assertFalse(exito)
        self.assertEqual(self.cliente.balance, 1000)
        self.assertEqual(len(self.cliente.historial), 0)

    # Prueba de que al crear un cliente el historial esta vacio
    def test_historial_vacio_al_inicio(self):
        self.assertEqual(len(self.cliente.historial), 0)

    # Casos límite: validar que depositar cantidades no positivas no modifica el balance ni el historial
    def test_depositar_cantidad_no_positiva(self):
        saldo_inicial = self.cliente.balance
        self.cliente.depositar(0)
        self.assertEqual(self.cliente.balance, saldo_inicial)
        self.cliente.depositar(-100)
        self.assertEqual(self.cliente.balance, saldo_inicial)

    # Casos límite: validar que retirar cantidades no positivas no modifica el balance ni el historial
    def test_retirar_cantidad_no_positiva(self):
        saldo_inicial = self.cliente.balance
        exito = self.cliente.retirar(0)
        self.assertFalse(exito)
        self.assertEqual(self.cliente.balance, saldo_inicial)
        exito = self.cliente.retirar(-50)
        self.assertFalse(exito)
        self.assertEqual(self.cliente.balance, saldo_inicial)

if __name__ == '__main__':
    unittest.main()

