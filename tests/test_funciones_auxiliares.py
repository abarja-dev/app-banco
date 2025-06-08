"""
Tests de las funciones auxiliares usando unittest y mock
"""


import unittest
from unittest.mock import patch
from src.funciones import pedir_cantidad


# Clase que testea las funciones auxiliares con unittest y mock
class TestFuncionesAuxiliares(unittest.TestCase):

    @patch('builtins.input', return_value='100.5')
    # Metodo que debe devolver correctamente un número positivo ingresado
    def test_pedir_cantidad_valida(self, mock_input):
        resultado = pedir_cantidad('Ingresa una cantidad: ')
        self.assertEqual(resultado, 100.5)

    @patch('builtins.input', side_effect=['-50', 'abc', '0', '200'])
    # Metodo que debe rechazar las entradas inválidas como números negativos, texto o cero, y aceptar finalmente un
    # número válido
    def test_pedir_cantidad_entrada_invalida(self, mock_input):
        resultado = pedir_cantidad('Ingresa una cantidad válida: ')
        self.assertEqual(resultado, 200)

if __name__ == '__main__':
    unittest.main()

