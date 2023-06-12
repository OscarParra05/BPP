#Código Python

def obtener_longitud(cadena):
    return len(cadena)

def es_palindromo(cadena):
    return cadena == cadena[::-1]

def obtener_maximo(lista):
    return max(lista)

def sumar_lista(lista):
    return sum(lista)


#Comprobación utilizando unittest

import unittest

class TestFunciones(unittest.TestCase):
    def test_obtener_longitud(self):
        self.assertEqual(obtener_longitud("Hola"), 4)
        self.assertEqual(obtener_longitud("Bienvenido"), 10)
        self.assertEqual(obtener_longitud("A"), 1)
        self.assertEqual(obtener_longitud("Unittest"), 8)

    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("radar"))
        self.assertFalse(es_palindromo("python"))

    def test_obtener_maximo(self):
        self.assertEqual(obtener_maximo([1, 8, 3, 9, 2]), 9)
        self.assertEqual(obtener_maximo([-10, -5, -20]), -5)

    def test_sumar_lista(self):
        self.assertEqual(sumar_lista([1, 2, 3, 4, 5]), 18)
        self.assertEqual(sumar_lista([-1, 0, 1]), 0)

if __name__ == '__main__':
    unittest.main()


#Comprobación utilizando pytest

import pytest

def test_obtener_longitud():
    assert obtener_longitud("Hola") == 4
    assert obtener_longitud("Esto") == 4
    assert obtener_longitud("Es") == 2
    assert obtener_longitud("Pytest") == 6

def test_es_palindromo():
    assert es_palindromo("radar") is True
    assert es_palindromo("programacion") is False
    assert es_palindromo("salas") is False

def test_obtener_maximo():
    assert obtener_maximo([16, 2, 8, 13, 6]) == 13
    assert obtener_maximo([-3, 5, -17]) == 5

def test_sumar_lista():
    assert sumar_lista([5, 6, 7, 8, 9]) == 35
    assert sumar_lista([-1, 1, 4]) == 4

if __name__ == '__main__':
    pytest.main()
