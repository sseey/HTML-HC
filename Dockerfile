# Utiliser une image de base Python compatible avec Python 3.12
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet
COPY . .

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python3", "app.py"]
