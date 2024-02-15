import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout

from components.DemiTerrain import DemiTerrain
from components.PageQuestions import PageQuestions
from config.logging_config import logger
from config.paths import MALE_PLAYERS_SORTED_CSV, FOOTBALL_TEAMS_SORTED
from processors.PlayerDataProcessor import process_player_data
from processors.TeamDataProcessor import process_team_data

if __name__ == "__main__":
    # Vérifier si le fichier traité existe déjà
    if not os.path.exists(MALE_PLAYERS_SORTED_CSV):
        # Traitement des données si le fichier n'existe pas
        process_player_data()

    else:
        logger.info(f"Le fichier {MALE_PLAYERS_SORTED_CSV} existe déjà. Le traitement n'est pas nécessaire.")

    if not os.path.exists(FOOTBALL_TEAMS_SORTED):
        # Traitement des données si le fichier n'existe pas
        process_team_data()
    else:
        logger.info(f"Le fichier {FOOTBALL_TEAMS_SORTED} existe déjà. Le traitement n'est pas nécessaire.")

    # Initialisation de l'application Qt
    app = QApplication(sys.argv)

    # Création de la fenêtre principale
    main_window = QWidget()
    main_window.setWindowTitle("EA Sports FC 24")
    main_window.setGeometry(100, 100, 900, 550)
    main_window.setFixedSize(1000, 700) #(1200,550)

    # Création de la mise en page principale
    layout_principal = QHBoxLayout(main_window)

    # Création de l'instance de DemiTerrain
    demi_terrain = DemiTerrain()

    # Création de l'instance de PageQuestions avec demi_terrain comme argument
    page_questions = PageQuestions(demi_terrain)

    # Ajout du composant de dessin du terrain à gauche
    layout_principal.addWidget(demi_terrain)

    # Ajout du composant de questions à droite
    layout_principal.addWidget(page_questions)

    # Ajout du logo en haut à droite
    logo_label = QLabel()
    layout_logo = QVBoxLayout()
    pixmap = QPixmap("assets/logo.png")

    if pixmap.isNull():
        logger.error("Exception -> Erreur lors du chargement de l'image.")
    else:
        scaled_pixmap = pixmap.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)
        logo_label.setPixmap(scaled_pixmap)
        layout_logo.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignRight)
        layout_principal.addLayout(layout_logo)

    # Affichage de la fenêtre principale
    main_window.show()
    sys.exit(app.exec_())
