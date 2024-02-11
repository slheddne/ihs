import os

# Chemin du répertoire principal du projet
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Chemin du répertoire des données
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Chemin du fichier CSV des joueurs
MALE_PLAYERS_CSV = os.path.join(DATA_DIR, 'male_players.csv')

# Chemin du fichier CSV trié des joueurs
MALE_PLAYERS_SORTED_CSV = os.path.join(DATA_DIR, 'male_players_sorted.csv')

# Chemin du fichier CSV des équipes
FOOTBALL_TEAMS = os.path.join(DATA_DIR, 'Football_teams.csv')

# Chemin du fichier CSV des équipes triées
FOOTBALL_TEAMS_SORTED = os.path.join(DATA_DIR, 'Football_teams_sorted.csv')