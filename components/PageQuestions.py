from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QComboBox

from utils.utils import generate_team


class PageQuestions(QWidget):
    def __init__(self, demi_terrain_widget):
        """
        Initialise la page de questions.
        :param demi_terrain_widget: Référence à l'instance de DemiTerrain pour mettre à jour l'équipe générée.
        """
        super().__init__()

        # Initialisation du layout vertical
        self.layout = QVBoxLayout()  # Layout vertical
        self.nbDefenseurs = 0  # Initialiser le nombre de défenseurs
        self.nbMilieux = 0  # Initialiser le nombre de milieux
        self.nbAttaquants = 0  # Initialiser le nombre d'attaquants

        # Garder une référence à l'équipe générée
        self.team = None

        # Garder une référence à DemiTerrain
        self.demi_terrain_widget = demi_terrain_widget

        self.tactic = ""
        self.reponse_question_1 = ""
        self.reponse_question_2 = ""

        # Initialisation du schéma tactique en fonction des réponses
        self.tactic_mapping = {
            ("Attaque", "Oui"): "4231",
            ("Attaque", "Non"): "433",
            ("Milieu", "Offensif"): "442 carré",
            ("Milieu", "Défensif"): "442 losange",
            ("Défense", "Oui"): "532",
            ("Défense", "Non"): "343"
        }

        # Titre
        title_label = QLabel("Caractéristiques souhaitées de l'équipe")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(title_label)

        # Sous-titre
        subtitle_label = QLabel("Répondez aux questions suivantes :")
        subtitle_label.setStyleSheet("font-size: 14px; font-style: italic;")
        self.layout.addWidget(subtitle_label)

        # Label pour la première question
        self.label_question_1 = QLabel("Quel bloc souhaites-tu renforcer ?")
        self.layout.addWidget(self.label_question_1)

        # Combobox pour poser la première question
        self.combo_question_1 = QComboBox()
        self.combo_question_1.addItems(["", "Attaque", "Milieu", "Défense"])
        self.combo_question_1.currentIndexChanged.connect(self.question_1_selectionnee)
        self.layout.addWidget(self.combo_question_1)

        # Label pour la deuxième question
        self.label_question_2 = QLabel("Veuillez répondre à la première question")
        self.layout.addWidget(self.label_question_2)

        # Combobox pour poser la deuxième question
        self.combo_question_2 = QComboBox()
        self.combo_question_2.addItems([""])  # Initialiser avec une option vide
        self.combo_question_2.setEnabled(False)  # Désactiver la combobox
        self.layout.addWidget(self.combo_question_2)

        # Bouton pour soumettre les réponses
        self.submit_button = QPushButton("Générer")
        self.submit_button.clicked.connect(self.soumettre_reponses)
        self.submit_button.setEnabled(False)  # Désactiver le bouton
        self.layout.addWidget(self.submit_button)

        # Étirement du layout
        self.layout.addStretch()

        # Ajout du layout à la fenêtre principale
        self.setLayout(self.layout)

    def question_1_selectionnee(self, index):
        """
        Gère la sélection de la première question.
        :param index: Index de la question sélectionnée.
        """
        if index == 0:  # Si rien n'est sélectionné
            self.reponse_question_1 = ""
            self.label_question_2.setText("Veuillez répondre à la première question")
            self.combo_question_2.clear()  # Effacer les anciens choix
            self.combo_question_2.setEnabled(False)  # Désactiver la combobox
            self.submit_button.setEnabled(False)  # Désactiver le bouton de soumission
        else:
            self.reponse_question_1 = self.combo_question_1.currentText()
            self.label_question_2.setText(self.label_question_suivante())
            self.combo_question_2.clear()  # Effacer les anciens choix
            self.combo_question_2.setEnabled(True)  # Activer la combobox
            if self.reponse_question_1 == "Attaque":
                self.combo_question_2.addItems(["", "Oui", "Non"])
            elif self.reponse_question_1 == "Milieu":
                self.combo_question_2.addItems(["", "Offensif", "Défensif"])
            elif self.reponse_question_1 == "Défense":
                self.combo_question_2.addItems(["", "Oui", "Non"])
            self.submit_button.setEnabled(True)  # Activer le bouton de soumission

    def label_question_suivante(self):
        """
        Retourne le libellé de la prochaine question en fonction de la réponse à la première question.
        """
        if self.reponse_question_1 == "Attaque":
            return "Veux-tu attaquer tout en étant prêt à défendre ?"
        elif self.reponse_question_1 == "Milieu":
            return "Veux-tu un milieu offensif ou défensif ?"
        elif self.reponse_question_1 == "Défense":
            return "Souhaites-tu un poste de libero (couverture de la défense) ?"

    def soumettre_reponses(self):
        """
        Soumettre les réponses aux questions.
        """
        # Récupérer la réponse à la deuxième question
        self.reponse_question_2 = self.combo_question_2.currentText()

        # Récupérer la tactique choisie
        self.tactic = self.tactic_mapping[(self.reponse_question_1, self.reponse_question_2)]

        # Générer l'équipe en fonction de la tactique
        self.team = generate_team(self.tactic, "Facile")

        # Mettre à jour l'équipe et la tactique du widget DemiTerrain
        self.demi_terrain_widget.set_team_and_tactic(self.team, self.tactic)
