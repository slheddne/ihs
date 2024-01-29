import requests
from PyQt5.QtGui import QPainter, QLinearGradient, QColor, QPen, QPixmap
from PyQt5.QtWidgets import QWidget


class DemiTerrain(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 500)
        self.image_url = (
            "https://media.contentapi.ea.com/content/dam/ea/easfc/fc-24/ratings/common/full/player-portraits/p232656"
            ".png.adapt.50w.png")  # Pour tester, à ne pas utiliser le code final

    def paintEvent(self, event):
        painter = QPainter(self)

        # Dessiner le fond vert dégradé
        self.dessiner_fond_vert_degrade(painter)

        # Dessiner le demi-terrain
        self.dessiner_demi_terrain(painter)

        # Dessiner l'image à l'emplacement spécifié
        self.dessiner_image(painter, x=20, y=400)

    def dessiner_fond_vert_degrade(self, painter):
        # Créer un dégradé vertical
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(0, 128, 0))  # Vert foncé en haut
        gradient.setColorAt(1, QColor(0, 255, 0))  # Vert clair en bas

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
        painter.drawEllipse(170, 225, 70, 70)

        # Dessiner le trait du milieu
        painter.drawLine(10, 260, 390, 260)

        # Dessiner les cages
        painter.drawRect(135, 10, 130, 40)  # Cage du haut
        painter.drawRect(135, 480, 130, 40)  # Cage du bas

    def dessiner_image(self, painter, x, y):
        # Télécharger l'image depuis l'URL
        response = requests.get(self.image_url)
        if response.status_code == 200:
            # Convertir l'image téléchargée en QPixmap
            image_data = response.content
            image = QPixmap()
            image.loadFromData(image_data)

            # Dessiner l'image à l'emplacement spécifié
            painter.drawPixmap(x, y, image)
        else:
            print("Exception -> Erreur lors du téléchargement de l'image :", response.status_code)
