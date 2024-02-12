# Positions des joueurs pour différentes tactiques
TACTIC_POSITIONS = {
    "4231": {
        "defenseur 1": (20, 400),  # defenseur gauche
        "defenseur 2": (140, 400),
        "defenseur 3": (260, 400),
        "defenseur 4": (380, 400),

        "milieu defensif 1": (140, 300),
        "milieu defensif 2": (260, 300),

        "milieu offensif 1": (105, 200),
        "milieu offensif 2": (200, 200),
        "milieu offensif 3": (295, 200),

        "attaquant 1": (200, 100),
    },
    "442 losange": {
        "defenseur 1": (20, 400),  # defenseur gauche
        "defenseur 2": (140, 400),
        "defenseur 3": (260, 400),
        "defenseur 4": (380, 400),

        "milieu 1": (200, 325),
        "milieu 2": (140, 260),
        "milieu 3": (260, 260),
        "milieu 4": (200, 200),

        "attaquant 1": (140, 125),
        "attaquant 2": (260, 125),
    },
    "442 carré": {
        "defenseur 1": (20, 400),  # defenseur gauche
        "defenseur 2": (140, 400),
        "defenseur 3": (260, 400),
        "defenseur 4": (380, 400),

        "milieu 1": (20, 220),
        "milieu 2": (140, 280),
        "milieu 3": (260, 280),
        "milieu 4": (380, 220),

        "attaquant 1": (140, 125),
        "attaquant 2": (260, 125),

    },
    "433": {
        "defenseur 1": (20, 400),  # defenseur gauche
        "defenseur 2": (140, 400),
        "defenseur 3": (260, 400),
        "defenseur 4": (380, 400),

        "milieu 1": (105, 260),
        "milieu 2": (200, 260),
        "milieu 3": (295, 260),

        "attaquant 1": (105, 150),
        "attaquant 2": (200, 150),
        "attaquant 3": (295, 150)

    },
    "532": {
        "defenseur 1": (20, 400),  # defenseur gauche
        "defenseur 2": (110, 400),
        "defenseur 3": (200, 400),
        "defenseur 4": (290, 400),
        "defenseur 5": (380, 400),

        "milieu 1": (105, 250),
        "milieu 2": (200, 250),
        "milieu 3": (295, 250),

        "attaquant 1": (140, 150),
        "attaquant 2": (260, 150)

    },
    "343": {
        "defenseur 1": (20, 400),  # defenseur gauche
        "defenseur 2": (200, 400),
        "defenseur 3": (380, 400),

        "milieu 1": (20, 220),
        "milieu 2": (140, 280),
        "milieu 3": (260, 280),
        "milieu 4": (380, 220),

        "attaquant 1": (105, 150),
        "attaquant 2": (200, 150),
        "attaquant 3": (295, 150)

    }
}

# Positions mappées pour savoir le bloc associé
# Une meilleure solution serait de revoir la structure des données pour éviter ce mapping
POSITION_BLOCK_MAPPING = {
    "defenseur": "Defense",
    "milieu": "Milieu",
    "attaquant": "Attaque",
}
