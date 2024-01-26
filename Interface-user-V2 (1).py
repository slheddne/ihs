#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:25:36 2024

@author: sarah
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5.QtGui import QPainter, QPen, QColor, QLinearGradient, QPixmap
from PyQt5.QtCore import Qt


class PageQuestions(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # titre
        title_label = QLabel("Caracteristiques souhaitées de l'équipe")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(title_label)

        # sous-titre
        subtitle_label = QLabel("Répondez aux questions suivantes :")
        subtitle_label.setStyleSheet("font-size: 14px; font-style: italic;")
        self.layout.addWidget(subtitle_label)
        
        
        # Questions
        self.ajouter_question_menu_deroulant("Quel bloc souhaites-tu renforcer ?", ["Attaque", "Milieu","Défense"])
  

        # #bouton pour soumettre les réponses
        submit_button = QPushButton("Soumettre")
        submit_button.clicked.connect(self.soumettre_reponses)
        self.layout.addWidget(submit_button)

        self.layout.addStretch()

        self.setLayout(self.layout)
        
        
        
    
    def ajouter_question_menu_deroulant(self, question_text, choices):
        # Ajouter une étiquette pour la question avec menu déroulant
        question_label = QLabel(question_text)
        self.layout.addWidget(question_label)

        # Ajouter un menu déroulant (QComboBox) avec les choix
        combo_box = QComboBox()
        combo_box.addItems(choices)
        self.layout.addWidget(combo_box)

        # Utiliser un séparateur pour espacer les questions
        self.layout.addSpacing(10)

    # def ajouter_question_numerique(self, question_text):
    #     # Ajouter une étiquette pour la question numérique
    #     question_label = QLabel(question_text)
    #     self.layout.addWidget(question_label)

    #     # Ajouter un champ de réponse numérique avec QLineEdit
    #     numerique_input = QLineEdit()
    #     numerique_input.setPlaceholderText("Entrez un chiffre")
    #     self.layout.addWidget(numerique_input)

        # séparateur pour espacer les questions
        self.layout.addSpacing(10)
       # return numerique_input

    

    def soumettre_reponses(self):
        nbDefenseurs= self.nbDefenseurs.value()
        nbMilieux= self.nbDefenseurs.value()
        nbAttanquants= self.nbDefenseurs.value()
        nbJoueurs= nbDefenseurs + nbMilieux + nbAttanquants
        # Vérifier si la somme des réponses numériques dépasse 10
        if nbJoueurs != 10:
            self.error_label.setText("Le nombre total de joueurs doit être égale à 10.")
        else:
            # Réinitialiser le message d'erreur
            self.error_label.setText("")

            # Cette fonction pourrait être utilisée pour traiter les réponses
            print("Réponses soumises.")


class DemiTerrain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schéma tactique")
        self.setMinimumWidth(400)
        self.setMinimumHeight(500)

    def paintEvent(self, event):
        painter = QPainter(self)

        #fond vert dégradé
        self.dessiner_fond_vert_degrade(painter)

        # demi-terrain
        self.dessiner_demi_terrain(painter)

    def dessiner_fond_vert_degrade(self, painter):
        #dégradé vertical
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(0, 128, 0))  # Vert foncé en haut
        gradient.setColorAt(1, QColor(0, 255, 0))  # Vert clair en bas

        # Appliquer
        painter.setBrush(gradient)
        painter.drawRect(0, 0, self.width(), self.height())

    def dessiner_demi_terrain(self, painter):
        # stylo pour les lignes
        pen = QPen(QColor(255, 255, 255), 2)
        painter.setPen(pen)

        # rectangle du terrain
        painter.drawRect(10, 10, 380, 510)

        # cercle central
        painter.drawEllipse(170, 225, 70, 70)
        
        # trait du milieu
        painter.drawLine(10, 260, 390, 260)
        
        
        # cages
        painter.drawRect(135, 10, 130, 40)  # Cage du haut
        painter.drawRect(135, 480, 130, 40)  # Cage du bas

class FenetrePrincipale(QWidget):
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

        pixmap = QPixmap("/Users/sarah/Desktop/ea_sports_fifa-logo-brandlogos.net_.png")
        scaled_pixmap = pixmap.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio)
        logo_label.setPixmap(scaled_pixmap)
        layout_logo.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignRight)  # Set alignment
        layout_principal.addLayout(layout_logo)  # Add the logo layout to the main layout


        self.setLayout(layout_principal)
        self.setWindowTitle("Interface Utilisateur")
        self.setGeometry(100, 100, 800, 400)
        
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.show()
    sys.exit(app.exec_())
    