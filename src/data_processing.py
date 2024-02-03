import os

import pandas as pd

# Constantes pour les catégories
CATEGORIES = {
    'Facile': 0.25,
    'Moyen': 0.5,
    'Difficile': 0.75,
    'Expert': 1.0
}


# Fonction pour charger les données depuis le fichier CSV
def charger_donnees(fichier):
    try:
        print(f"Chargement des données depuis le fichier '{fichier}'.")
        return pd.read_csv(fichier)
    except FileNotFoundError:
        print("Exception -> Le fichier spécifié n'existe pas.")
        return None
    except pd.errors.ParserError:
        print("Exception -> Le format du fichier CSV est incorrect.")
        return None


# Fonction pour catégoriser les joueurs en fonction de leur note
def categoriser_joueurs(data):
    overall_values = data['Overall']
    points_de_coupe = [0] + [overall_values.quantile(value) for value in CATEGORIES.values()]
    data['Catégorie'] = pd.cut(overall_values, bins=points_de_coupe, labels=CATEGORIES.keys(), right=False)
    return data


# Fonction pour convertir les URLs des joueurs et obtenir leur image
def convertir_urls(url):
    # Extraire l'ID FC 24 du lien
    player_id = url.split('/')[-1]

    # Construire le nouveau lien avec l'ID approprié
    player_url = f"https://media.contentapi.ea.com/content/dam/ea/easfc/fc-24/ratings/common/full/player-portraits/p{player_id}.png.adapt.50w.png"
    return player_url


# Fonction pour trier les positions en fonction des blocs
def trier_positions(data):
    blocs = {
        'Gardien': ['GK'],
        'Defense': ['LH', 'SW', 'RH', 'RB', 'LB', 'LCB', 'CB', 'CH', 'RCB', 'LWB', 'RWB', 'WB'],
        'Milieu': ['DM', 'CDM', 'LW', 'LM', 'CAM', 'CM', 'M', 'RM', 'RW', 'AMR', 'WF', 'AML', 'AMC', 'AM'],
        'Attaque': ['LS', 'RS', 'LF', 'SS', 'RF', 'ST', 'CF']
    }
    data['Blocs'] = data['Position'].apply(
        lambda pos: next((bloc for bloc, positions in blocs.items() if pos in positions), None))
    return data


# Fonction pour générer le nom d'un joueur aléatoire en fonction de la catégorie et du bloc
def generer_nom_joueur(data, categorie, bloc):
    try:
        if categorie not in CATEGORIES:
            raise ValueError("Catégorie invalide")

        if bloc not in data['Blocs'].unique():
            raise ValueError("Bloc invalide")

        joueurs_filtres = data[(data['Catégorie'] == categorie) & (data['Blocs'] == bloc)]

        if joueurs_filtres.empty:
            raise ValueError("Exception -> Aucun joueur trouvé pour cette catégorie et ce bloc.")

        joueur_choisi = joueurs_filtres.sample()
        return joueur_choisi['Name'].values[0]

    except ValueError as e:
        return f"Exception -> Erreur: {e}"
    except Exception as e:
        return f"Exception -> Une erreur inattendue s'est produite: {e}"


# Fonction pour enregistrer les données dans un fichier Excel
def sauvegarder_donnees(data, fichier):
    try:
        data.to_csv(fichier, index=False)
    except Exception as e:
        print(f"Exception -> Erreur lors de l'enregistrement des données : {e}")


# Fonction principale pour traiter les données
def traiter_donnes():
    fichier_csv = "../data/male_players.csv"

    # Charger et traiter les données
    data = charger_donnees(fichier_csv)

    if data is not None:
        # Vérifier si le fichier male_players_sorted.csv existe dans le dossier data
        if os.path.exists("../data/male_players_sorted.csv"):
            print("Le fichier male_players_sorted.csv existe déjà.")
        else:
            # Vérifier si les données ont déjà été traitées pour ne pas refaire le traitement à chaque fois
            if 'Catégorie' not in data.columns and 'Blocs' not in data.columns:
                # Catégoriser les joueurs
                data = categoriser_joueurs(data)

                # Trier les positions des joueurs
                data = trier_positions(data)

                # Convertir les URLs des joueurs
                data['URL'] = data['URL'].apply(convertir_urls)

                # Enregistrer les données traitées dans un nouveau fichier CSV
                nouveau_fichier_csv = "../data/male_players_sorted.csv"
                sauvegarder_donnees(data, nouveau_fichier_csv)
                print("Les données ont été traitées et enregistrées dans male_players_sorted.csv.")


def get_player(data, position):
    # Filtrer les données pour le poste spécifié
    filtered_data = data[data['Position'] == position]

    # Sélectionner une entrée aléatoire parmi les joueurs à ce poste
    player_entry = filtered_data.sample()

    return player_entry
