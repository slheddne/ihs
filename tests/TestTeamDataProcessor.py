import unittest
import pandas as pd
from processors.TeamDataProcessor import TeamDataProcessor


class TestTeamDataProcessor(unittest.TestCase):
    def setUp(self):
        # Créer un DataFrame de test avec l'exemple donné
        self.test_data = pd.DataFrame({'Team': ['Manchester City'],
                                       'Tournament': ['Premier League'],
                                       'Goals': [83],
                                       'Shots pg': [15.8],
                                       'yellow_cards': [46],
                                       'red_cards': [2],
                                       'Possession%': [60.8],
                                       'Pass%': [89.4],
                                       'AerialsWon': [12.8],
                                       'Rating': [7.01]})

    def test_categorize_team(self):
        # Appeler la méthode de catégorisation
        categorized_data = TeamDataProcessor.categorize_team(self.test_data)

        # Vérifier si une nouvelle colonne 'Catégorie' a été ajoutée
        self.assertIn('Catégorie', categorized_data.columns)

        # Vérifier si la catégorie assignée est correcte pour l'exemple donné
        self.assertEqual(categorized_data['Catégorie'].iloc[0], 'Moyenne')


if __name__ == '__main__':
    unittest.main()
