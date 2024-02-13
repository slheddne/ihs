import logging

import pandas as pd
import requests
from PyQt5.QtGui import QPixmap

from config.categories import CATEGORIES
from config.paths import MALE_PLAYERS_SORTED_CSV
from config.player_blocks import BLOCS
from config.tactics import TACTIC_POSITIONS, POSITION_BLOCK_MAPPING


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
    # Charger les données depuis le fichier CSV
    data = pd.read_csv(MALE_PLAYERS_SORTED_CSV)

    # Récupérer les coordonnées (x, y) de la position du joueur sur le terrain
    position_x, position_y = get_player_position(tactic, position)

    if position_x is not None and position_y is not None:
        # Récupérer les données du joueur pour la position spécifiée
        player = get_player(data, position)

        if not player.empty:
            # Télécharger l'image depuis l'URL
            image_data = download_image(player['URL'].values[0])
            if image_data:
                # Convertir l'image téléchargée en QPixmap
                image = QPixmap()
                image.loadFromData(image_data)

                # Dessiner l'image à l'emplacement spécifié
                painter.drawPixmap(position_x, position_y, image)


def filter_players(block, category):
    data = pd.read_csv(MALE_PLAYERS_SORTED_CSV)
    if block not in BLOCS or category not in CATEGORIES:
        logging.error("Exception -> Bloc ou catégorie invalide.")
        return pd.DataFrame()
    return data[(data['Bloc'] == block) & (data['Catégorie'] == category)]


def get_random_player(block, category):
    filtered_players = filter_players(block, category)
    if not filtered_players.empty:
        return filtered_players.sample(n=1)
    else:
        logging.error("Exception -> Aucun joueur éligible trouvé.")
        return None


def generate_team(tactic, difficulty):
    if tactic not in TACTIC_POSITIONS:
        logging.error("Exception -> Tactique invalide.")
        return None

    team = []
    for position, (x, y) in TACTIC_POSITIONS[tactic].items():
        position_type = position.split()[0]  # Récupérer le type de position
        block = POSITION_BLOCK_MAPPING.get(position_type)
        if block:
            player = get_random_player(block, difficulty)
            if player is not None:
                team.append(player)
    return team
