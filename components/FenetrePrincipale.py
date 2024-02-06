import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout

from components.DemiTerrain import DemiTerrain
from components.PageQuestions import PageQuestions
from config.logging_config import logger
from config.paths import MALE_PLAYERS_SORTED_CSV, LOGO_PATH
from utils.data_processing import traiter_donnes


class FenetrePrincipale(QWidget):
    def __init__(self):
        super().__init__()

        # Vérifier si le fichier traité existe déjà
        if not os.path.exists(MALE_PLAYERS_SORTED_CSV):
            # Traitement des données si le fichier n'existe pas
            traiter_donnes()
        else:
            logger.info(f"Le fichier {MALE_PLAYERS_SORTED_CSV} existe déjà. Le traitement n'est pas nécessaire.")

        self.setWindowTitle("EA Sports FC 24")
        self.setGeometry(100, 100, 900, 550)
        self.setFixedSize(900, 550)

        # Création de la mise en page principale
        self.layout_principal = QHBoxLayout(self)

        # Ajout du composant de dessin du terrain à gauche
        self.dessin_demi_terrain = DemiTerrain()
        self.layout_principal.addWidget(self.dessin_demi_terrain)

        # Ajout du composant de questions à droite
        self.page_questions = PageQuestions()
        self.layout_principal.addWidget(self.page_questions)

        # Ajout du logo en haut à droite
        self.logo_label = QLabel()
        layout_logo = QVBoxLayout()
        pixmap = QPixmap(LOGO_PATH)

        if pixmap.isNull():
            logger.error("Exception -> Erreur lors du chargement de l'image.")
        else:
            scaled_pixmap = pixmap.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)
            self.logo_label.setPixmap(scaled_pixmap)
            layout_logo.addWidget(self.logo_label, alignment=Qt.AlignTop | Qt.AlignRight)
            self.layout_principal.addLayout(layout_logo)

        # Affichage de la fenêtre principale
        self.show()
