def get_player_position(tactic, position):
    positions = {}
    if tactic == "433":
        positions = {
            'GK': (175, 460),  # Gardien
            'LB': (20, 360),  # Défenseur latéral gauche
            'CBL': (120, 380),  # Défenseur central gauche
            'CBR': (230, 380),  # Défenseur central droit
            'RB': (330, 360),  # Défenseur latéral droit
            'CML': (50, 200),  # Milieu central gauche
            'CAM': (175, 170),  # Milieu offensif central
            'CMR': (300, 200),  # Milieu central droit
            'LW': (20, 50),  # Ailier gauche
            'ST': (175, 20),  # Attaquant
            'RW': (330, 50),  # Ailier droit
        }
    elif tactic == "442":
        positions = {

        }
    else:
        print(f"Exception -> La tactique demandée '{tactic} 'n'est pas reconnue.")

    if position in positions:
        return positions[position]
    else:
        print(f"Exception -> La position demandée '{position}' n'est pas reconnue.")
        return None