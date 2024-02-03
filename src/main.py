import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout

from src.components.DemiTerrain import DemiTerrain
from src.components.PageQuestions import PageQuestions
from src.data_processing import traiter_donnes

if __name__ == "__main__":
    traiter_donnes()

    app = QApplication(sys.argv)

    # Création de la fenêtre principale (QWidget)
    main_window = QWidget()
    main_window.setWindowTitle("EA Sports FC 24")
    main_window.setGeometry(100, 100, 900, 550)
    main_window.setFixedSize(900, 550)

    # Création de la mise en page horizontale pour organiser le dessin du terrain et les questions
    layout_principal = QHBoxLayout(main_window)

    # Ajouter le dessin du terrain
    dessin_demi_terrain = DemiTerrain()
    layout_principal.addWidget(dessin_demi_terrain)

    # Ajout des questions à côté du dessin du terrain
    page_questions = PageQuestions()
    layout_principal.addWidget(page_questions)

    # Ajout du logo
    logo_label = QLabel()
    layout_logo = QVBoxLayout()
    pixmap = QPixmap("../assets/logo.png")

    if pixmap.isNull():
        print("Exception -> Erreur lors du chargement de l'image.")
    else:
        scaled_pixmap = pixmap.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)
        logo_label.setPixmap(scaled_pixmap)
        layout_logo.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignRight)
        layout_principal.addLayout(layout_logo)

    main_window.show()
    sys.exit(app.exec_())
