import pandas as pd

from config.categories import CATEGORIES
from config.logging_config import logger
from config.paths import FOOTBALL_TEAMS, FOOTBALL_TEAMS_SORTED
from processors.DataLoader import DataLoader


class TeamDataProcessor:
    @staticmethod
    def categorize_team(data):
        """
        Catégorise les équipes en fonction de leur note globale.

        Args:
            data (DataFrame): DataFrame contenant les données des équipes.

        Returns:
            DataFrame: DataFrame avec une colonne supplémentaire 'Catégorie' indiquant la catégorie de chaque équipe.
        """
        overall_values = data['Rating']
        points_de_coupe = [0] + [overall_values.quantile(value) for value in CATEGORIES.values()]
        data['Catégorie'] = pd.cut(overall_values, bins=points_de_coupe, labels=CATEGORIES.keys(), right=False)
        return data


def process_team_data():
    """
    Fonction pour traiter les données des équipes.
    """
    # Charger les données des équipes
    data = DataLoader.load_data(FOOTBALL_TEAMS)

    # Vérifier si les données sont chargées avec succès et si la colonne 'Catégorie' n'est pas déjà présente
    if data is not None and 'Catégorie' not in data.columns:
        # Catégoriser les équipes
        data = TeamDataProcessor.categorize_team(data)
        # Sauvegarder les données traitées dans un nouveau fichier CSV
        DataLoader.save_data(data, FOOTBALL_TEAMS_SORTED)
        logger.info(f"Les données des équipes ont été traitées et enregistrées dans : {FOOTBALL_TEAMS_SORTED}.")
