from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox


class PageQuestions(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.nbDefenseurs = 0
        self.nbMilieux = 0
        self.nbAttaquants = 0

        self.error_label = QLabel()

        # Titre
        title_label = QLabel("Caractéristiques souhaitées de l'équipe")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(title_label)

        # Sous-titre
        subtitle_label = QLabel("Répondez aux questions suivantes :")
        subtitle_label.setStyleSheet("font-size: 14px; font-style: italic;")
        self.layout.addWidget(subtitle_label)

        # Questions
        self.ajouter_question_menu_deroulant("Quel bloc souhaites-tu renforcer ?", ["Attaque", "Milieu", "Défense"])

        # Bouton pour soumettre les réponses
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
        combo_box.currentIndexChanged.connect(self.selection_changed)
        self.layout.addWidget(combo_box)

        # Utiliser un séparateur pour espacer les questions
        self.layout.addSpacing(10)

    def selection_changed(self, index):
        # Fonction pour gérer le changement de sélection dans les menus déroulants
        sender = self.sender()
        if sender.currentText() == "Attaque":
            print("Attaque")
        elif sender.currentText() == "Milieu":
            print("Milieu")
        elif sender.currentText() == "Défense":
            print("Défense")

    @staticmethod
    def soumettre_reponses(self):
        print("Bouton 'Soumettre' cliqué.")
