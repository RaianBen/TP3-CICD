# Utiliser une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code du projet dans le conteneur
COPY . .

# Commande pour exécuter les tests (par exemple pytest)
CMD ["pytest"]
