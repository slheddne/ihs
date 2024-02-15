import logging

import pandas as pd
import requests

from config.categories import CATEGORIES
from config.paths import MALE_PLAYERS_SORTED_CSV, FOOTBALL_TEAMS_SORTED
from config.player_blocks import BLOCS
from config.tactics import TACTIC_POSITIONS, POSITION_BLOCK_MAPPING
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPixmap, QFont, QFontMetrics


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
    Dessine l'image d'un joueur à sa position spécifique sur le terrain en fonction de la tactique et ajoute le nom du joueur.

    :param painter: Objet pour dessiner.
    :param player_index: Index du joueur dans l'équipe.
    :param tactic: Tactique de jeu.
    :param player: Joueur à dessiner.
    """
    taille_image = 60 #dimension de l'image
    marge_texte = 5  # écart entre l'image et le texte

    for position, (position_x, position_y) in TACTIC_POSITIONS[tactic].items():
        if player_index == 0:
            # Télécharge l'image depuis l'URL
            image_data = download_image(player['URL'])
            if image_data:
                try:
                    # Convertir l'image téléchargée en QPixmap
                    image = QPixmap()
                    image.loadFromData(image_data)

                    # Dessiner l'image à l'emplacement spécifié
                    painter.drawPixmap(position_x, position_y, taille_image, taille_image, image)

                    # Configurer la police pour le texte
                    font = QFont('Arial', 10)  # Commencer avec une taille de police plus grande
                    painter.setFont(font)

                    # Calculer la position du texte (en dessous de l'image)
                    texte_x = position_x
                    texte_y = position_y + taille_image + marge_texte

                    # Mesurer la largeur du texte avec la police actuelle
                    metrics = QFontMetrics(font)
                    nom_joueur = player['Name']
                    largeur_texte = metrics.width(nom_joueur)

                    # Ajuster la taille de la police si le texte est trop large
                    while largeur_texte > taille_image and font.pointSize() > 1:
                        font.setPointSize(font.pointSize() - 1)  # Réduire la taille de la police
                        painter.setFont(font)
                        metrics = QFontMetrics(font)
                        largeur_texte = metrics.width(nom_joueur)

                    # Dessiner le nom du joueur
                    painter.drawText(QRect(texte_x, texte_y, taille_image, 30), Qt.AlignCenter, nom_joueur)

                    break  # Arrêter la boucle une fois le joueur dessiné
                except Exception as e:
                    logging.error("Exception -> Le chargement de l'image a échoué : %s", e)
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
    #la fonction utilise la méthode sample(n=1) pour sélectionner aléatoirement un joueur parmi ceux filtrés
    # n=1 spécifie que seulement un joueur doit être sélectionné.
    # nous faisons cela car la fonction sample ne fonctionne qu'avec le iloc
    #donc même si nous avons qu'un joueurs selectionné, nous devons le préciser
    else:
        logging.error("Exception -> Aucun joueur éligible trouvé.")
        return None


def generate_team(tactic, category):
    if tactic not in TACTIC_POSITIONS:
        logging.error("Exception -> Tactique invalide.")
        return None
    if category not in CATEGORIES:
        logging.error("Exception -> Catégorie invalide.")
        return None

    team = []
    for position, (x, y) in TACTIC_POSITIONS[tactic].items():
        position_type = position.split()[0]  # Récupérer le type de position
        block = POSITION_BLOCK_MAPPING.get(position_type)
        if block:
            player = get_random_player(block, category)
            if player is not None:
                team.append(player)
    return team

def filter_team(category):
    data = pd.read_csv(FOOTBALL_TEAMS_SORTED)
    if category not in CATEGORIES:
        logging.error("Exception -> Catégorie invalide.")
        return pd.DataFrame()
    return data[(data['Catégorie'] == category)]

def get_random_team(category):
    filtered_team = filter_team(category)
    if not filtered_team.empty:
        return filtered_team.sample(n=1).iloc[0].to_dict()["Team"]
    else:
        logging.error("Exception -> Aucune équipe éligible trouvé.")
        return None

#petit test simple pour tester ces fonctions
#def main():
    # Appeler la fonction generer_equipe_adverse()
    #equipe_adverse = get_random_team("Facile")
    #return print("Vous allez jouer contre",equipe_adverse)

#if __name__ == "__main__":
    #main()