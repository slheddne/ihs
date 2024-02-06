import pandas as pd

from config.categories import CATEGORIES
from config.image_urls import BASE_PLAYER_IMAGE_URL, PLAYER_IMAGE_SIZE
from config.logging_config import logger
from config.paths import MALE_PLAYERS_CSV, MALE_PLAYERS_SORTED_CSV
from config.player_blocks import BLOCS


def charger_donnees():
    """
    Charge les données à partir du fichier CSV des joueurs.

    :return: DataFrame contenant les données si le chargement est réussi, sinon None.
    """
    try:
        logger.info(f"Chargement des données depuis le fichier '{MALE_PLAYERS_CSV}'.")
        return pd.read_csv(MALE_PLAYERS_CSV)
    except FileNotFoundError:
        logger.error("Exception -> Le fichier spécifié n'existe pas.")
        return None
    except pd.errors.ParserError:
        logger.error("Exception -> Le format du fichier CSV est incorrect.")
        return None


def categoriser_joueurs(data):
    """
    Catégorise les joueurs en fonction de leur note globale.

    :param data: DataFrame contenant les données des joueurs.
    :return: DataFrame avec une colonne supplémentaire 'Catégorie' indiquant la catégorie de chaque joueur.
    """
    overall_values = data['Overall']
    points_de_coupe = [0] + [overall_values.quantile(value) for value in CATEGORIES.values()]
    data['Catégorie'] = pd.cut(overall_values, bins=points_de_coupe, labels=CATEGORIES.keys(), right=False)
    return data


def convertir_urls(url):
    """
    Convertit l'URL d'un joueur pour obtenir son image.

    :param url: URL du joueur.
    :return: Nouvelle URL de l'image du joueur.
    """
    player_id = url.split('/')[-1]
    player_url = f"{BASE_PLAYER_IMAGE_URL}p{player_id}.png.adapt.{PLAYER_IMAGE_SIZE}w.png"
    return player_url


def trier_positions(data):
    """
    Trie les positions des joueurs en fonction des blocs de jeu.

    :param data: DataFrame contenant les données des joueurs.
    :return: DataFrame avec une colonne supplémentaire 'Bloc' indiquant le bloc de chaque joueur.
    """
    data['Bloc'] = data['Position'].apply(
        lambda pos: next((bloc for bloc, positions in BLOCS.items() if pos in positions), None))
    return data


def sauvegarder_donnees(data, fichier):
    """
    Enregistre les données dans un fichier CSV.

    :param data: DataFrame contenant les données à enregistrer.
    :param fichier: Chemin vers le fichier CSV de destination.
    """
    try:
        data.to_csv(fichier, index=False)
    except Exception as e:
        logger.error(f"Exception -> Erreur lors de l'enregistrement des données : {e}")


def traiter_donnes():
    """
    Fonction principale pour le traitement des données.
    """
    # Charger les données
    data = charger_donnees()

    if data is not None:
        # Vérifier si les données ont déjà été traitées pour ne pas refaire le traitement à chaque fois
        if 'Catégorie' not in data.columns and 'Bloc' not in data.columns:
            # Catégoriser les joueurs
            data = categoriser_joueurs(data)

            # Trier les positions des joueurs
            data = trier_positions(data)

            # Convertir les URLs des joueurs
            data['URL'] = data['URL'].apply(convertir_urls)

            # Enregistrer les données traitées dans un nouveau fichier CSV
            nouveau_fichier_csv = MALE_PLAYERS_SORTED_CSV
            sauvegarder_donnees(data, nouveau_fichier_csv)
            logger.info(f"Les données ont été traitées et enregistrées dans : {nouveau_fichier_csv}.")


def get_player(data, position):
    """
    Récupère un joueur aléatoire pour une position donnée.

    :param data: DataFrame contenant les données des joueurs.
    :param position: Position du joueur.
    :return: DataFrame contenant les données d'un joueur pour la position donnée.
    """
    filtered_data = data[data['Position'] == position]
    player_entry = filtered_data.sample()
    return player_entry
