import pandas as pd

from config.categories import CATEGORIES
from config.image_urls import PLAYER_IMAGE_SIZE, BASE_PLAYER_IMAGE_URL
from config.logging_config import logger
from config.paths import MALE_PLAYERS_CSV, MALE_PLAYERS_SORTED_CSV
from config.player_blocks import BLOCS
from config.players_features import FEATURES_BLOCKS
from processors.DataLoader import DataLoader


class PlayerDataProcessor:
    @staticmethod
    def categorize_players(data):
        """
        Catégorise les joueurs en fonction de leur note globale.

        Args:
            data (DataFrame): DataFrame contenant les données des joueurs.

        Returns:
            DataFrame: DataFrame avec une colonne supplémentaire 'Catégorie' indiquant la catégorie de chaque joueur.
        """
        overall_values = data['Overall']
        points_de_coupe = [0] + [overall_values.quantile(value) for value in CATEGORIES.values()]
        data['Catégorie'] = pd.cut(overall_values, bins=points_de_coupe, labels=CATEGORIES.keys(), right=False)
        return data

    @staticmethod
    def categorize_positions(data):
        """
        Trie les positions des joueurs en fonction des blocs de jeu.

        Args:
            data (DataFrame): DataFrame contenant les données des joueurs.

        Returns:
            DataFrame: DataFrame avec une colonne supplémentaire 'Bloc' indiquant le bloc de chaque joueur.
        """
        data['Bloc'] = data['Position'].apply(
            lambda pos: next((bloc for bloc, positions in BLOCS.items() if pos in positions), None))
        return data

    @staticmethod
    def categorize_features(data):
        """
        Catégorise les joueurs en fonction de leur note globale en leur attribuant un score qui est la somme de leurs caractéristiques.

        Args:
            data (DataFrame): DataFrame contenant les données des joueurs.

        Returns:
            DataFrame: DataFrame avec une colonne supplémentaire 'Score' indiquant le score du joueur.
        """
        data['Score'] = data.apply(lambda row: sum(row[FEATURES_BLOCKS[row['Bloc']]]), axis=1)
        return data

    @staticmethod
    def convert_urls(url):
        """
        Convertit l'URL d'un joueur pour obtenir son image.

        Args:
            url (str): URL du joueur.

        Returns:
            str: Nouvelle URL de l'image du joueur.
        """
        player_id = url.split('/')[-1]
        player_url = f"{BASE_PLAYER_IMAGE_URL}p{player_id}.png.adapt.{PLAYER_IMAGE_SIZE}w.png"
        return player_url


def process_player_data():
    """
    Fonction pour traiter les données des joueurs.
    """
    # Charger les données des joueurs
    data = DataLoader.load_data(MALE_PLAYERS_CSV)

    # Vérifier si les données sont chargées avec succès et si les colonnes 'Catégorie', 'Bloc' et 'Score' ne sont pas déjà présentes
    if data is not None and {'Catégorie', 'Bloc', 'Score'}.isdisjoint(data.columns):
        # Catégoriser les joueurs
        data = PlayerDataProcessor.categorize_players(data)
        # Catégoriser les positions des joueurs
        data = PlayerDataProcessor.categorize_positions(data)
        # Catégoriser les caractéristiques des joueurs
        data = PlayerDataProcessor.categorize_features(data)
        # Convertir les URLs des joueurs
        data['URL'] = data['URL'].apply(PlayerDataProcessor.convert_urls)
        # Sauvegarder les données traitées dans un nouveau fichier CSV
        DataLoader.save_data(data, MALE_PLAYERS_SORTED_CSV)
        logger.info(f"Les données des joueurs ont été traitées et enregistrées dans : {MALE_PLAYERS_SORTED_CSV}.")
