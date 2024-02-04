import logging

import pandas as pd
import requests
from PyQt5.QtGui import QPixmap

# Positions des joueurs pour différentes tactiques
TACTIC_POSITIONS = {
    "433": {
        'GK': (175, 460), 'LB': (20, 360), 'CBL': (120, 380),
        'CBR': (230, 380), 'RB': (330, 360), 'CML': (50, 200),
        'CAM': (175, 170), 'CMR': (300, 200), 'LW': (20, 50),
        'ST': (175, 20), 'RW': (330, 50),
    }
}

# Mappage des positions des joueurs, utile pour les noms de colonnes dans le fichier CSV
POSITION_MAPPING = {
    'GK': 'GK', 'LB': 'LB', 'CBL': 'CB', 'CBR': 'CB', 'RB': 'RB',
    'CML': 'CM', 'CAM': 'CAM', 'CMR': 'CM', 'LW': 'LW', 'ST': 'ST', 'RW': 'RW'
}


def get_player_position(tactic, position):
    """
    Récupère la position du joueur sur le terrain en fonction de la tactique.

    :param tactic: Tactique de jeu (par ex. "433").
    :param position: Position du joueur (par ex. "GK").
    :return: Coordonnées (x, y) de la position du joueur sur le terrain.
    """
    positions = TACTIC_POSITIONS.get(tactic)
    if positions is None:
        logging.error(f"Exception -> La tactique demandée '{tactic}' n'est pas reconnue.")
        return None
    if position in positions:
        return positions[position]
    else:
        logging.error(f"Exception -> La position demandée '{position}' n'est pas reconnue.")
        return None


def get_player(data, position):
    """
    Récupère les données du joueur pour une position donnée.

    :param data: Données des joueurs.
    :param position: Position du joueur.
    :return: Données du joueur pour la position donnée.
    """
    return data[data['Position'] == position]


def download_image(url):
    """
    Télécharge une image à partir de l'URL spécifiée.

    :param url: URL de l'image à télécharger.
    :return: Contenu de l'image téléchargée.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        logging.error("Exception -> Erreur lors du téléchargement de l'image : ", response.status_code)
        return None


def dessiner_image(painter, tactic, position):
    """
    Dessine l'image d'un joueur à une position spécifique sur le terrain.

    :param painter: Objet pour dessiner.
    :param tactic: Tactique de jeu.
    :param position: Position du joueur.
    """
    position_csv = POSITION_MAPPING.get(position, position)

    # Charger les données depuis le fichier CSV
    data = pd.read_csv("../data/male_players_sorted.csv")

    # Récupérer l'URL de l'image du joueur pour le poste spécifié
    player = get_player(data, position_csv)

    if not player.empty:
        # Télécharger l'image depuis l'URL
        image_data = download_image(player['URL'].values[0])
        if image_data:
            # Convertir l'image téléchargée en QPixmap
            image = QPixmap()
            image.loadFromData(image_data)

            # Dessiner l'image à l'emplacement spécifié
            position_x, position_y = get_player_position(tactic, position)
            if position_x is not None and position_y is not None:
                painter.drawPixmap(position_x, position_y, image)
