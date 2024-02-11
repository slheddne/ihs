from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox


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
        self.ajouter_question_menu_deroulant('Niveau de jeu',["Facile", "Moyen", "Difficile", "Expert"])
        self.soumettre_reponses()

        # Étirement du layout
        self.layout.addStretch()

        self.setLayout(self.layout)



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
        if reponse_question_precedente == "Attaque":
            #self.layout.addSpacing(10)
            self.ajouter_question_menu_deroulant("Veux-tu attaquer tout en étant prêt à défendre?", ["Oui", "Non"])
        elif reponse_question_precedente == "Milieu":
            #self.layout.addSpacing(10)
            self.ajouter_question_menu_deroulant("Veux-tu un milieu offensif ou défensif?", ["Offensif", "défensif"])

        elif reponse_question_precedente == "Défense":
            #self.layout.addSpacing(10)
            self.ajouter_question_menu_deroulant("Souhaites-tu un poste de libero (couverture de la défense)?", ["Oui", "Non"])

        # Bouton pour soumettre les réponses
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



        print("Bouton 'Soumettre' cliqué.")

    def desactiver_niveaux(self):
        """
        Désactiver les niveaux de jeu supérieurs à Facile jusqu'à ce que l'utilisateur gagne son match.
        """
        # Désactiver les niveaux de jeu supérieurs à Facile
        for i in range(1, self.niveau_combobox.count()):
            self.niveau_combobox.setItemData(i, False)


