from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox

from config import config as cfg

"""
Classe pour la page des questions :
- Cette classe hérite de la classe QWidget
- Elle contient les questions et les menus déroulants
- Elle permet de gérer la mise en page de la page des questions
"""


class PageQuestions(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.nbDefenseurs = 0
        self.nbMilieux = 0
        self.nbAttaquants = 0

        self.error_label = QLabel()

        # Titre
        title_label = QLabel(cfg.TITLE_TEXT)
        title_label.setStyleSheet(cfg.TITLE_TEXT_STYLE)
        self.layout.addWidget(title_label)

        # Sous-titre
        subtitle_label = QLabel(cfg.SUBTITLE_TEXT)
        subtitle_label.setStyleSheet(cfg.SUBTITLE_TEXT_STYLE)
        self.layout.addWidget(subtitle_label)

        # Questions
        self.ajouter_question_menu_deroulant(cfg.QUESTION_TEXT, cfg.QUESTION_CHOICES)

        # Bouton pour soumettre les réponses
        submit_button = QPushButton(cfg.SUBMIT_BUTTON_TEXT)
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
        combo_box.currentIndexChanged.connect(self.selection_changed)  # Connect to selection change signal
        self.layout.addWidget(combo_box)

        # Utiliser un séparateur pour espacer les questions
        self.layout.addSpacing(10)

    def selection_changed(self, index):
        # Fonction pour gérer le changement de sélection dans les menus déroulants
        sender = self.sender()
        if sender.currentText() == cfg.QUESTION_CHOICES[0]:
            self.nbAttaquants = index + 1
        elif sender.currentText() == cfg.QUESTION_CHOICES[1]:
            self.nbMilieux = index + 1
        elif sender.currentText() == cfg.QUESTION_CHOICES[2]:
            self.nbDefenseurs = index + 1

    def soumettre_reponses(self):
        nbJoueurs = self.nbDefenseurs + self.nbMilieux + self.nbAttaquants
        print(nbJoueurs)
