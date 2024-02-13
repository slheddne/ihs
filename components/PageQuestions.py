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
        self.layout = QVBoxLayout()
        self.nbDefenseurs = 0
        self.nbMilieux = 0
        self.nbAttaquants = 0

        # Garder une référence à l'équipe générée
        self.team = None

        # Garder une référence à DemiTerrain
        self.demi_terrain_widget = demi_terrain_widget

        # Ajout d'un attribut pour suivre le nombre de questions posées
        self.compteurQuestions = 1

        self.tactic = ""
        self.bloc_a_ameliorer = ""
        self.systeme_jeu = ""
        self.niveau = ""

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
        self.combo_question_2.currentIndexChanged.connect(self.question_2_selectionnee)
        self.layout.addWidget(self.combo_question_2)

        # Label pour la troisième question
        self.label_question_3 = QLabel("Niveau")
        self.layout.addWidget(self.label_question_3)

        # Combobox pour choisir le niveau
        self.combo_niveau = QComboBox()
        self.combo_niveau.addItems(["", "Facile", "Moyen", "Difficile", "Expert"])
        self.combo_niveau.setEnabled(False)  # Désactiver la combobox
        self.layout.addWidget(self.combo_niveau)

        # Bouton pour soumettre les réponses
        self.submit_button = QPushButton("Générer")
        self.submit_button.clicked.connect(self.soumettre_reponses)
        self.submit_button.setEnabled(False)  # Désactiver le bouton de soumission
        self.layout.addWidget(self.submit_button)

        # Étirement du layout
        self.layout.addStretch()

        # Ajout du layout à la fenêtre principale
        self.setLayout(self.layout)

    def question_1_selectionnee(self, index):
        """
        Gère la sélection de la première question.
        """
        if index == 0:  # Si rien n'est sélectionné
            self.bloc_a_ameliorer = ""
            self.label_question_2.setText("Veuillez répondre à la première question")
            self.combo_question_2.clear()  # Effacer les anciens choix
            self.combo_question_2.setEnabled(False)  # Désactiver la combobox
            self.submit_button.setEnabled(False)  # Désactiver le bouton de soumission
        else:
            self.bloc_a_ameliorer = self.combo_question_1.currentText()
            self.label_question_2.setText(self.label_question_suivante())
            self.combo_question_2.clear()  # Effacer les anciens choix
            self.combo_question_2.setEnabled(True)  # Activer la combobox
            if self.bloc_a_ameliorer == "Attaque":
                self.combo_question_2.addItems(["", "Oui", "Non"])
            elif self.bloc_a_ameliorer == "Milieu":
                self.combo_question_2.addItems(["", "Offensif", "Défensif"])
            elif self.bloc_a_ameliorer == "Défense":
                self.combo_question_2.addItems(["", "Oui", "Non"])
            self.submit_button.setEnabled(False)  # Désactiver le bouton de soumission

    def label_question_suivante(self):
        """
        Retourne le libellé de la prochaine question en fonction de la réponse à la première question.
        """
        if self.bloc_a_ameliorer == "Attaque":
            return "Veux-tu attaquer tout en étant prêt à défendre ?"
        elif self.bloc_a_ameliorer == "Milieu":
            return "Veux-tu un milieu offensif ou défensif ?"
        elif self.bloc_a_ameliorer == "Défense":
            return "Souhaites-tu un poste de libero (couverture de la défense) ?"

    def question_2_selectionnee(self, index):
        """
        Gère la sélection de la deuxième question.
        """
        if index == 0:  # Si rien n'est sélectionné
            self.systeme_jeu = ""
            self.combo_niveau.setEnabled(False)  # Désactiver la combobox de niveau
            self.submit_button.setEnabled(False)  # Désactiver le bouton de soumission
        else:
            self.systeme_jeu = self.combo_question_2.currentText()
            self.combo_niveau.setEnabled(True)  # Activer la combobox de niveau
            self.submit_button.setEnabled(True)  # Activer le bouton de soumission

    def soumettre_reponses(self):
        """
        Soumettre les réponses aux questions.
        """
        # Récupérer la réponse à la deuxième question
        self.systeme_jeu = self.combo_question_2.currentText()

        # Récupérer la réponse au niveau
        self.niveau = self.combo_niveau.currentText()

        # Vérifier si toutes les réponses sont sélectionnées
        if self.bloc_a_ameliorer and self.systeme_jeu and self.niveau:
            # Récupérer la tactique choisie
            self.tactic = self.tactic_mapping[(self.bloc_a_ameliorer, self.systeme_jeu)]

            # Générer l'équipe en fonction de la tactique
            self.team = generate_team(self.tactic, self.niveau)

            # Mettre à jour l'équipe et la tactique du widget DemiTerrain
            self.demi_terrain_widget.set_team_and_tactic(self.team, self.tactic)
