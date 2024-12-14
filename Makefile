# Charger les variables d'environnement depuis .env
include .env
export $(shell sed 's/=.*//' .env)

# Variables
VENV = venv
PYTHON = python3
PIP = $(VENV)/bin/pip
ACTIVATE = source $(VENV)/bin/activate
DOCKER_IMAGE = health-calculator

# Initialiser le projet (création de venv + installation des dépendances)
init:
	@echo "initialization..."
	@echo "Creation d'un environnement virtuel"; \
	$(PYTHON) -m venv $(VENV); \
	. $(VENV)/bin/activate && \
	echo "Installer les librairies" && \
	$(PIP) install -r requirements.txt


# Lancer l'application Flask
run:
	. $(VENV)/bin/activate && python app.py

# Construire l'image Docker
build:
	docker build -t $(DOCKER_IMAGE) .

# Lancer le conteneur Docker
run-container:
	docker run -d -p $(PORT):5000 --name $(CONTAINER_NAME) $(DOCKER_IMAGE)
	@echo "Conteneur $(CONTAINER_NAME) lancé sur le port $(PORT)."

# Arrêter et supprimer le conteneur Docker
stop-container:
	@if docker ps -q -f name=$(CONTAINER_NAME); then \
		docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME); \
		echo "Conteneur $(CONTAINER_NAME) arrêté et supprimé."; \
	else \
		echo "Aucun conteneur $(CONTAINER_NAME) n'est en cours d'exécution."; \
	fi

# Lancer les tests unitaires
test:
	. $(VENV)/bin/activate && python -m unittest discover -s tests

# Lancer les tests de l'API
test-api:
	curl -X POST -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}' http://127.0.0.1:$(PORT)/bmi
	curl -X POST -H "Content-Type: application/json" -d '{"height": 175, "weight": 70, "age": 30, "gender": "male"}' http://127.0.0.1:$(PORT)/bmr

# Nettoyer le projet
clean:
	rm -rf $(VENV) __pycache__ */__pycache__ flask.pid
	@echo "Environnement virtuel, caches Python et fichier PID supprimés."

# Aide
help:
	@echo "Available commands:"
	@echo "  make init           - Créer un environnement virtuel et installer les dépendances."
	@echo "  make run            - Lancer l'application Flask."
	@echo "  make build          - Construire l'image Docker."
	@echo "  make run-container  - Lancer l'application dans un conteneur Docker."
	@echo "  make stop-container - Arrêter et supprimer le conteneur Docker."
	@echo "  make test           - Lancer les tests unitaires."
	@echo "  make test-api       - Tester l'API avec des requêtes curl."
	@echo "  make clean          - Nettoyer le projet (supprimer venv, caches, etc.)."