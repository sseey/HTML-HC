import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_bmi_valid(self):
        response = self.app.post('/bmi', json={"height": 1.75, "weight": 70})
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.get_json()['bmi'], 22.86, places=2)

    def test_bmi_missing_data(self):
        response = self.app.post('/bmi', json={"weight": 70})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Veuillez fournir 'height' et 'weight'.", response.get_json()['error'])

    def test_bmr_valid(self):
        response = self.app.post('/bmr', json={"height": 175, "weight": 70, "age": 30, "gender": "male"})
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.get_json()['bmr'], 1695.67, places=2)

    def test_bmr_invalid_gender(self):
        response = self.app.post('/bmr', json={"height": 175, "weight": 70, "age": 30, "gender": "other"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Le genre doit être 'male' ou 'female'.", response.get_json()['error'])

    def test_bmr_missing_data(self):
        response = self.app.post('/bmr', json={"height": 175, "weight": 70, "age": 30})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Veuillez fournir 'height', 'weight', 'age', et 'gender'.", response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()
