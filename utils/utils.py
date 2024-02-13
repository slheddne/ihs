import logging

import pandas as pd
import requests
from PyQt5.QtGui import QPixmap

from config.categories import CATEGORIES
from config.paths import MALE_PLAYERS_SORTED_CSV
from config.player_blocks import BLOCS
from config.tactics import TACTIC_POSITIONS, POSITION_BLOCK_MAPPING


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


def dessiner_image(painter, player_index, tactic, player):
    """
    Dessine l'image d'un joueur à sa position spécifique sur le terrain en fonction de la tactique.

    :param painter: Objet pour dessiner.
    :param player_index: Index du joueur dans l'équipe.
    :param tactic: Tactique de jeu.
    :param player: Joueur à dessiner.
    """
    # Parcourir les positions et joueurs de la tactique
    for position, (position_x, position_y) in TACTIC_POSITIONS[tactic].items():
        if player_index == 0:
            # Télécharger l'image depuis l'URL
            image_data = download_image(player['URL'])
            if image_data:
                try:
                    # Convertir l'image téléchargée en QPixmap
                    image = QPixmap()
                    image.loadFromData(image_data)

                    # Dessiner l'image à l'emplacement spécifié
                    painter.drawPixmap(position_x, position_y, image)
                    break  # Arrêter la boucle une fois le joueur dessiné
                except Exception as e:
                    logging.error("Exception lors du chargement de l'image : %s", e)
        else:
            player_index -= 1  # Décrémenter l'index si ce n'est pas le joueur actuel


def filter_players(block, category):
    data = pd.read_csv(MALE_PLAYERS_SORTED_CSV)
    if block not in BLOCS or category not in CATEGORIES:
        logging.error("Exception -> Bloc ou catégorie invalide.")
        return pd.DataFrame()
    return data[(data['Bloc'] == block) & (data['Catégorie'] == category)]


def get_random_player(block, category):
    filtered_players = filter_players(block, category)
    if not filtered_players.empty:
        return filtered_players.sample(n=1).iloc[0].to_dict()
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
