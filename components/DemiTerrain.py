from PyQt5.QtGui import QPainter, QLinearGradient, QColor, QPen
from PyQt5.QtWidgets import QWidget

from utils.utils import dessiner_image


class DemiTerrain(QWidget):
    def __init__(self):
        """
        Initialisation de la classe DemiTerrain.
        """
        super().__init__()
        self.setMinimumSize(400, 600) #400,500
        self.team = None
        self.tactic = ""

    def paintEvent(self, event):
        """
        Événement de peinture, appelé lorsque le widget a besoin d'être redessiné.
        :param event: Événement de peinture.
        """
        painter = QPainter(self)
        self.dessiner_fond_vert_degrade(painter)
        self.dessiner_demi_terrain(painter)
        if self.team is not None and self.tactic:  # Vérifier si l'équipe et la tactique sont définies
            self.dessiner_joueurs(painter)

    def dessiner_fond_vert_degrade(self, painter):
        """
        Dessine le fond vert dégradé.
        :param painter: Objet pour dessiner.
        """
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(0, 150, 0))  # Vert foncé en haut
        gradient.setColorAt(1, QColor(0, 210, 0))  # Vert clair en bas
        painter.setBrush(gradient)
        painter.drawRect(0, 0, 420, 550)

    def dessiner_demi_terrain(self, painter):
        """
        Dessine le terrain de football.
        :param painter: Objet pour dessiner.
        """
        pen = QPen(QColor(255, 255, 255), 2)
        painter.setPen(pen)
        painter.drawRect(10, 10, 380, 510)
        painter.drawEllipse(165, 225, 70, 70)
        painter.drawLine(10, 260, 390, 260)
        painter.drawRect(135, 10, 130, 40)  # Cage du haut
        painter.drawRect(135, 480, 130, 40)  # Cage du bas

    def dessiner_joueurs(self, painter):
        """
        Dessine les joueurs sur le terrain un par un en fonction de la tactique.
        :param painter: Objet pour dessiner.
        """
        for player_index, player in enumerate(self.team):
            dessiner_image(painter, player_index, self.tactic, player)

    def set_team_and_tactic(self, team, tactic):
        """
        Met à jour l'équipe et la tactique à dessiner.
        :param team: Liste des joueurs de l'équipe.
        :param tactic: La tactique.
        """
        self.team = team
        self.tactic = tactic
        self.update()
