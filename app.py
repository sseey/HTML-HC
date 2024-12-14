from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    Page d'accueil pour l'API.
    """
    return jsonify({
        "message": "Bienvenue sur l'API Health Calculator.",
        "endpoints": {
            "/bmi": "POST - Calcule le BMI avec 'height' (en m) et 'weight' (en kg).",
            "/bmr": "POST - Calcule le BMR avec 'height' (en cm), 'weight' (en kg), 'age', et 'gender'."
        }
    }), 200

@app.route('/bmi', methods=['POST'])
def bmi():
    """
    Endpoint pour calculer le BMI.
    Attend un JSON avec 'height' (en m) et 'weight' (en kg).
    """
    try:
        data = request.get_json()
        height = float(data['height'])
        weight = float(data['weight'])
        result = calculate_bmi(height, weight)
        return jsonify({"bmi": result}), 200
    except KeyError:
        return jsonify({"error": "Veuillez fournir 'height' et 'weight'."}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    """
    Endpoint pour calculer le BMR.
    Attend un JSON avec 'height' (en cm), 'weight' (en kg), 'age', et 'gender'.
    """
    try:
        data = request.get_json()
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = str(data['gender'])
        result = calculate_bmr(height, weight, age, gender)
        return jsonify({"bmr": result}), 200
    except KeyError:
        return jsonify({"error": "Veuillez fournir 'height', 'weight', 'age', et 'gender'."}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
