from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout

from config import config as cfg
from src.components.DemiTerrain import DemiTerrain
from src.components.PageQuestions import PageQuestions

"""
Classe pour la fenêtre principale :
- Cette classe hérite de la classe QWidget
- Elle contient le dessin du terrain et les questions
- Elle permet de gérer la mise en page de la fenêtre
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Créer une mise en page horizontale pour organiser le dessin du terrain et les questions
        layout_principal = QHBoxLayout()

        # Ajouter le dessin du terrain
        self.dessin_demi_terrain = DemiTerrain()
        layout_principal.addWidget(self.dessin_demi_terrain)

        # Ajouter les questions à coté du dessin du terrain
        self.page_questions = PageQuestions()
        layout_principal.addWidget(self.page_questions)

        # Ajouter le logo
        logo_label = QLabel()
        layout_logo = QVBoxLayout()
        pixmap = QPixmap(cfg.LOGO_PATH)

        if pixmap.isNull():
            print("Exception -> Erreur lors du chargement de l'image.")
        else:
            scaled_pixmap = pixmap.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)
            logo_label.setPixmap(scaled_pixmap)
            layout_logo.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignRight)
            layout_principal.addLayout(layout_logo)

        self.setLayout(layout_principal)
        self.setWindowTitle(cfg.MAIN_WINDOW_TITLE)
        self.setGeometry(100, 100, *cfg.MAIN_WINDOW_SIZE)
        self.setFixedSize(*cfg.MAIN_WINDOW_SIZE)
