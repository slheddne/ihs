# Positions des joueurs pour différentes tactiques
TACTIC_POSITIONS = {
    "4231": { # Pour les réponses "Attaque" + "oui"
        'gardien': (175, 460),  # Gardien


        "defenseur 1": (20, 360),
        "defenseur 2": (115, 380),
        "defenseur 3": (230, 380),
        "defenseur 4": (330, 360),


         "milieu defensif 1": (120, 260),
         "milieu defensif 2": (230, 260),



         "milieu offensif 1": (80, 130),
         "milieu offensif 2": (175, 130),
         "milieu offensif 3": (270, 130),

         "attaquant 1": (175, 20),
    },
    "442 losange": { # Pour les réponses "Milieu" + "défensif"
        'gardien': (175, 460),  # Gardien

        "defenseur 1": (20, 360),
        "defenseur 2": (115, 380),
        "defenseur 3": (230, 380),
        "defenseur 4": (330, 360),


        "milieu 1": (180, 300),
        "milieu 2": (120, 235),
        "milieu 3": (225, 235),
        "milieu 4": (180, 175),


        "attaquant 1": (100, 100),
        "attaquant 2": (250, 100),
    },
    "442 carré": {# Pour les réponses "Milieu" + "offensif"
        'gardien': (175, 460),  # Gardien


        "defenseur 1": (20, 360),
        "defenseur 2": (115, 380),
        "defenseur 3": (230, 380),
        "defenseur 4": (330, 360),

        "milieu 1": (20, 220),
        "milieu 2": (120, 240),
        "milieu 3": (230, 240),
        "milieu 4": (330, 220),

        "attaquant 1": (100, 100),
        "attaquant 2": (250, 100),

    },
    "433": { # Pour les réponses "Attaque" + "non"
        'gardien': (175, 460),  # Gardien

        'defenseur 1': (20, 360),  # Défenseur latéral gauche
        'defenseur 2': (120, 380),  # Défenseur central gauche
        'defenseur 3': (230, 380),  # Défenseur central droit
        'defenseur 4': (330, 360),  # Défenseur latéral droit
        'milieu 1': (50, 200),  # Milieu central gauche
        'milieu 2': (175, 170),  # Milieu offensif central
        'milieu 3': (300, 200),  # Milieu central droit
        'attaquant 1': (20, 50),  # Ailier gauche
        'attaquant 2': (175, 20),  # Attaquant
        'attaquant 3': (330, 50),  # Ailier droit

    },
    "532": { # Pour les réponses "Défense" +"oui"
        'gardien': (175, 460),  # Gardien


        "defenseur 1": (10, 340),  # defenseur gauche
        "defenseur 2": (90, 360),
        "defenseur 3": (170, 380),
        "defenseur 4": (250, 360),
        "defenseur 5": (330, 340),


        'milieu 1': (50, 220),
        'milieu 2': (175, 220),
        'milieu 3': (300, 220),

        "attaquant 1": (100, 100),
        "attaquant 2": (250, 100),

    },
    "343": { # Pour les réponses "Défense" + "non"
        'gardien': (175, 460),  # Gardien

        "defenseur 1": (50, 350),  # defenseur gauche
        "defenseur 2": (175, 350),
        "defenseur 3": (300, 350),

        "milieu 1": (10, 220),
        "milieu 2": (115, 220),
        "milieu 3": (220, 220),
        "milieu 4": (330, 220),

        'attaquant 1': (20, 120),
        'attaquant 2': (175, 100),
        'attaquant 3': (330, 120),

    }
}

# Positions mappées pour savoir le bloc associé
# Une meilleure solution serait de revoir la structure des données pour éviter ce mapping
POSITION_BLOCK_MAPPING = {
    "gardien": "Gardien",
    "defenseur": "Defense",
    "milieu": "Milieu",
    "attaquant": "Attaque",
}
