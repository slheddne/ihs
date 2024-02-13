from PyQt5.QtGui import QPainter, QLinearGradient, QColor, QPen
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QWidget


class DemiTerrain(QWidget):
    def __init__(self):
        """
        Initialisation de la classe DemiTerrain.
        """
        super().__init__()
        self.setMinimumSize(400, 500)

    def paintEvent(self, event):
        """
        Événement de peinture, appelé lorsque le widget a besoin d'être redessiné.
        """
        painter = QPainter(self)

        # Dessiner le fond vert dégradé
        self.dessiner_fond_vert_degrade(painter)

        # Dessiner le demi-terrain
        self.dessiner_demi_terrain(painter)

    def dessiner_fond_vert_degrade(self, painter):
        """
        Dessine un fond vert dégradé sur le widget.

        :param painter: Objet QPainter pour dessiner.
        """
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
        """
        Dessine le demi-terrain de football.

        :param painter: Objet QPainter pour dessiner.
        """
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

    def afficher_joueurs_equipe(self, equipe):
        """
        Affiche tous les joueurs de l'équipe sur le terrain.

        :param equipe: Liste des joueurs de l'équipe.
        """
        for joueur in equipe:
            position_x, position_y = joueur["position"]
            nom_joueur = joueur["nom"]

            # Créer un label pour afficher le nom du joueur
            joueur_label = QLabel(nom_joueur)
            joueur_label.setGeometry(position_x, position_y, 10, 10) # Ajuster la position du nom du joueur sur le terrain
            self.layout.addWidget(joueur_label)

