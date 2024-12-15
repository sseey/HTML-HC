from flask import Flask, request, jsonify, render_template, send_from_directory
from health_utils import calculate_bmi, calculate_bmr
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__, template_folder="templates", static_folder="static")

# Ajouter un routeur pour les fichiers dans 'assets'
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    """
    Servir les fichiers du dossier 'assets'.
    """
    return send_from_directory('assets', filename)

@app.route('/')
def home():
    """
    Page d'accueil avec une interface utilisateur.
    """
    return render_template('index.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    """
    Endpoint pour calculer le BMI.
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
    # Charger le port depuis .env ou utiliser le port 5000 par défaut
    PORT = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
