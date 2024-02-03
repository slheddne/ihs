import pandas as pd
import requests
from PyQt5.QtGui import QPainter, QLinearGradient, QColor, QPen, QPixmap
from PyQt5.QtWidgets import QWidget

from config.config import get_player_position
from src.data_processing import get_player


class DemiTerrain(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 500)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Dessiner le fond vert dégradé
        self.dessiner_fond_vert_degrade(painter)

        # Dessiner le demi-terrain
        self.dessiner_demi_terrain(painter)

        # Dessiner les images
        self.dessiner_image(painter, "433", "GK")
        self.dessiner_image(painter, "433", "LB")
        self.dessiner_image(painter, "433", "CBL")
        self.dessiner_image(painter, "433", "CBR")
        self.dessiner_image(painter, "433", "RB")
        self.dessiner_image(painter, "433", "CML")
        self.dessiner_image(painter, "433", "CAM")
        self.dessiner_image(painter, "433", "CMR")
        self.dessiner_image(painter, "433", "LW")
        self.dessiner_image(painter, "433", "ST")
        self.dessiner_image(painter, "433", "RW")

    def dessiner_fond_vert_degrade(self, painter):
        # Créer un dégradé vertical
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(0, 150, 0))  # Vert foncé en haut
        gradient.setColorAt(1, QColor(0, 210, 0))  # Vert clair en bas

        # Appliquer le dégradé comme brosse pour le peintre
        painter.setBrush(gradient)

        # Dessiner un rectangle rempli avec le dégradé
        painter.drawRect(0, 0, self.width(), self.height())

    @staticmethod
    def dessiner_demi_terrain(painter):
        # Stylo pour les lignes
        pen = QPen(QColor(255, 255, 255), 2)
        painter.setPen(pen)

        # Dessiner le rectangle du terrain
        painter.drawRect(10, 10, 380, 510)

        # Dessiner le cercle central
        painter.drawEllipse(165, 225, 70, 70)

        # Dessiner le trait du milieu
        painter.drawLine(10, 260, 390, 260)

        # Dessiner les cages
        painter.drawRect(135, 10, 130, 40)  # Cage du haut
        painter.drawRect(135, 480, 130, 40)  # Cage du bas

    @staticmethod
    def dessiner_image(painter, tactic, position):
        position_mapping = {
            'GK': 'GK', 'LB': 'LB', 'CBL': 'CB', 'CBR': 'CB', 'RB': 'RB',
            'CML': 'CM', 'CAM': 'CAM', 'CMR': 'CM', 'LW': 'LW', 'ST': 'ST', 'RW': 'RW'
        }
        position_csv = position_mapping.get(position, position)

        # Charger les données depuis le fichier CSV
        data = pd.read_csv("../data/male_players_sorted.csv")

        # Récupérer l'URL de l'image du joueur pour le poste spécifié
        player = get_player(data, position_csv)

        # Télécharger l'image depuis l'URL
        response = requests.get(player['URL'].values[0])
        if response.status_code == 200:
            # Convertir l'image téléchargée en QPixmap
            image_data = response.content
            image = QPixmap()
            image.loadFromData(image_data)

            # Dessiner l'image à l'emplacement spécifié
            painter.drawPixmap(get_player_position(tactic, position)[0],
                               get_player_position(tactic, position)[1], image)
        else:
            print("Exception -> Erreur lors du téléchargement de l'image :", response.status_code)
