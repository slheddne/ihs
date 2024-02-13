from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox

from utils.utils import generate_team


class PageQuestions(QWidget):
    def __init__(self):
        """
        Initialise la page de questions.
        """
        super().__init__()

        # Initialisation du layout vertical
        self.layout = QVBoxLayout()
        self.nbDefenseurs = 0
        self.nbMilieux = 0
        self.nbAttaquants = 0

        self.compteurQuestions = 1  # Ajout d'un attribut pour suivre le nombre de questions posées

        self.tactic = ""

        # Initialisation du schéma tactique en fonction des réponses
        self.tactic_mapping = {
            ("Attaque", "Oui"): "4231",
            ("Attaque", "Non"): "433",
            ("Milieu", "Offensif"): "442 carré",
            ("Milieu", "Défensif"): "442 losange",
            ("Défense", "Oui"): "532",
            ("Défense", "Non"): "343"
        }

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
        self.soumettre_reponses()


        # Niveau de jeu
        self.ajouter_question_menu_deroulant('Niveau de jeu', ["Facile", "Moyen", "Difficile", "Expert"])


        # Étirement du layout
        self.layout.addStretch()

        self.setLayout(self.layout)
# A REVOIR EN FONCTION DE L'ANCIENNE VERSION

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
            joueur_label.setGeometry(position_x, position_y, 10,
                                     10)  # Ajuster la position du nom du joueur sur le terrain
            self.layout.addWidget(joueur_label)

    def ajouter_question_menu_deroulant(self, question_text, choices):
        """
        Ajoute une question avec un menu déroulant à la page de questions.

        :param question_text: Texte de la question.
        :param choices: Choix disponibles dans le menu déroulant.
        """
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
        """
        Gère le changement de sélection dans les menus déroulants.

        :param index: Index de l'élément sélectionné dans le menu déroulant.
        """
        # Fonction pour gérer le changement de sélection dans les menus déroulants
        sender = self.sender()
        if sender.currentText() == "Attaque":
            print("Attaque")
        elif sender.currentText() == "Milieu":
            print("Milieu")
        elif sender.currentText() == "Défense":
            print("Défense")

    def ajouter_question_suivante(self, reponse_question_precedente):
        """
        Ajoute la question suivante sur l'interface en fonction de la réponse à la première question.

        :param reponse_question_precedente: Réponse à la première question.
        """
        # Vérifier si le nombre maximum de questions a été atteint
        if self.compteurQuestions >= 2:
            # Si oui, ne pas ajouter plus de questions
            print("Nombre maximum de questions atteint.")
            return

        if reponse_question_precedente == "Attaque":
            # self.layout.addSpacing(10)
            self.ajouter_question_menu_deroulant("Veux-tu attaquer tout en étant prêt à défendre?", ["Oui", "Non"])
        elif reponse_question_precedente == "Milieu":
            # self.layout.addSpacing(10)
            self.ajouter_question_menu_deroulant("Veux-tu un milieu offensif ou défensif?", ["Offensif", "Défensif"])

        elif reponse_question_precedente == "Défense":
            # self.layout.addSpacing(10)
            self.ajouter_question_menu_deroulant("Souhaites-tu un poste de libero (couverture de la défense)?", ["Oui", "Non"])

        # Bouton pour soumettre les réponses
       # submit_button = QPushButton("Soumettre")
       # submit_button.clicked.connect(self.soumettre_reponses)
       # self.layout.addWidget(submit_button)

        # Incrémenter le compteur de questions après avoir ajouté une question
        self.compteurQuestions += 1
        # Ajouter un bouton pour soumettre les réponses uniquement après la première question
        if self.compteurQuestions == 2:
            submit_button = QPushButton("Soumettre")
            submit_button.clicked.connect(self.soumettre_reponses)
            self.layout.addWidget(submit_button)

    def soumettre_reponses(self):
        """
        Fonction exécutée lorsque le bouton 'Soumettre' est cliqué.
        """

        # Récupérer la réponse à la première question
        combo_box_question_1 = self.findChild(QComboBox)
        if combo_box_question_1 is not None:
            selected_text = combo_box_question_1.currentText()


            # Ajouter la deuxième question en fonction de la réponse à la première question
            self.ajouter_question_suivante(selected_text)

            # Récupérer la réponse à la deuxième question
            combo_box_question_2 = self.findChild(QComboBox, "question2_combobox")
            if combo_box_question_2 is not None:
                selected_text_question_2 = combo_box_question_2.currentText()

                # Déterminer la tactique en fonction des réponses aux deux questions
                tactic = self.determiner_tactique(selected_text, selected_text_question_2)

                if tactic:
                    # Générer et afficher l'équipe sur le terrain
                    equipe = generate_team(tactic, "Facile")
                    self.afficher_joueurs_equipe(equipe)

        print("Bouton 'Soumettre' cliqué.")

    def determiner_tactique(self, reponse_question_precedente, reponse_question_suivante):
        """
        Détermine la tactique en fonction des réponses aux deux questions.

        :param reponse_question_precedente: Réponse à la première question.
        :param reponse_question_suivante: Réponse à la deuxième question.
        :return: Tactique à appliquer.
        """
        # Logique pour déterminer la tactique en fonction des réponses aux questions
        if reponse_question_precedente == "Attaque":
            if reponse_question_suivante == "Oui":
                return "4231"
            elif reponse_question_suivante == "Non":
                return "433"
        elif reponse_question_precedente == "Milieu":
            if reponse_question_suivante == "Offensif":
                return "442 carré"
            elif reponse_question_suivante == "Défensif":
                return "442 losange"
        elif reponse_question_precedente == "Défense":
            if reponse_question_suivante == "Oui":
                return "532"
            elif reponse_question_suivante == "Non":
                return "343"

        return None

    def desactiver_niveaux(self):
        """
        Désactiver les niveaux de jeu supérieurs à Facile jusqu'à ce que l'utilisateur gagne son match.
        """
        # Désactiver les niveaux de jeu supérieurs à Facile
        for i in range(1, self.niveau_combobox.count()):
            self.niveau_combobox.setItemData(i, False)
