import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi_valid(self):
        # Teste un cas valide
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)

    def test_calculate_bmi_invalid(self):
        # Taille ou poids négatif
        with self.assertRaises(ValueError) as context:
            calculate_bmi(-1.75, 70)
        self.assertEqual(str(context.exception), "La taille et le poids doivent être supérieurs à 0.")

        with self.assertRaises(ValueError) as context:
            calculate_bmi(1.75, -70)
        self.assertEqual(str(context.exception), "La taille et le poids doivent être supérieurs à 0.")

    def test_calculate_bmr_valid(self):
        # Cas valides pour homme et femme
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'male'), 1695.67, places=2)
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'female'), 1507.13, places=2)

    def test_calculate_bmr_invalid(self):
        # Taille, poids ou âge négatifs
        with self.assertRaises(ValueError) as context:
            calculate_bmr(-175, 70, 30, 'male')
        self.assertEqual(str(context.exception), "La taille, le poids et l'âge doivent être supérieurs à 0.")

        # Genre invalide
        with self.assertRaises(ValueError) as context:
            calculate_bmr(175, 70, 30, 'other')
        self.assertEqual(str(context.exception), "Le genre doit être 'male' ou 'female'.")

if __name__ == '__main__':
    unittest.main()
