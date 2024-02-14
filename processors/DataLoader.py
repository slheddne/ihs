import pandas as pd

from config.logging_config import logger


class DataLoader:
    @staticmethod
    def load_data(file_path):
        """
        Charge les données à partir d'un fichier CSV.

        Args:
            file_path (str): Chemin vers le fichier CSV contenant les données.

        Returns:
            DataFrame: Les données chargées depuis le fichier CSV, ou None en cas d'erreur.
        """
        try:
            # Log pour indiquer le début du chargement des données
            logger.info(f"Chargement des données depuis le fichier '{file_path}'.")
            # Chargement des données depuis le fichier CSV
            return pd.read_csv(file_path)
        except FileNotFoundError:
            # Log en cas d'erreur FileNotFoundError
            logger.error("Exception -> Le fichier spécifié n'existe pas.")
            return None
        except pd.errors.ParserError:
            # Log en cas d'erreur ParserError (mauvais format de fichier CSV)
            logger.error("Exception -> Le format du fichier CSV est incorrect.")
            return None

    @staticmethod
    def save_data(data, file_path):
        """
        Enregistre les données dans un fichier CSV.

        Args:
            data (DataFrame): DataFrame contenant les données à enregistrer.
            file_path (str): Chemin vers le fichier CSV de destination.
        """
        try:
            data.to_csv(file_path, index=False)
        except Exception as e:
            logger.error(f"Exception -> Erreur lors de l'enregistrement des données : {e}")
