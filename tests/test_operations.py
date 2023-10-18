import unittest

from calculator.calculator import *


class TestOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 2), 3)

    def test_soustraction(self):
        self.assertEqual(soustraction(2, 3), -1)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_quotient(self):
        self.assertEqual(quotient(13, 2), 6)

    # def test_reste(self):
    #     self.assertEqual(reste(23, 8), 7)

    def test_valeur_absolue(self):
        self.assertEqual(valeur_absolue(-2), 2)

    def test_carre(self):
        self.assertEqual(carre(4), 16)

    def test_racine_carre(self):
        self.assertEqual(racine_carre(16), 4)

    def test_somme_liste(self):
        self.assertEqual(somme_liste([5, 6, 7]), 18)

    def test_puissance(self):
        self.assertEqual(puissance(4, 3), 64)

    def test_inverse(self):
        self.assertEqual(inverse(5), 1 / 5)

    # def test_tri(self):
    #     self.assertEqual(tri([4, 2, 8]), [2, 4, 8])

    def test_factoriel(self):
        self.assertEqual(factoriel(4), 24)
