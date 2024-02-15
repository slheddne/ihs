import unittest
from unittest.mock import patch

from utils.utils import generate_team

#tests poyr tester category et tactiques
class TestGenerateTeam(unittest.TestCase):
    @patch('utils.utils.get_random_player')
    def test_generate_team_success(self, mock_get_random_player):
        # Comportement attendu du mock pour un joueur valide
        mock_get_random_player.return_value = {'Nom': 'Kylian Mbappe', 'Position': 'ST'}
        #mock pour générer une team virtuelle

        # On génère une équipe avec une tactique et une difficulté valides
        result = generate_team('433', 'Facile')

        # Vérifications
        # 1) Vérifier si la fonction retourne une équipe non vide
        self.assertNotEqual(result, None)
        # 2) Vérifier si la longueur de l'équipe générée est égale à la longueur attendue
        self.assertEqual(len(result), 11)

    @patch('utils.utils.get_random_player')
    def test_generate_team_invalid_tactic(self, mock_get_random_player):
        # Comportement attendu du mock pour un joueur valide
        mock_get_random_player.return_value = {'Nom': 'Kylian Mbappe', 'Position': 'ST'}

        # On génère une équipe avec une tactique invalide et une difficulté valide
        result = generate_team('459', 'Facile')

        # Vérification
        # 1) Vérifier si la fonction retourne None pour une tactique invalide
        self.assertEqual(result, None)

    @patch('utils.utils.get_random_player')
    def test_generate_team_invalid_difficulty(self, mock_get_random_player):
        # Comportement attendu du mock pour un joueur valide
        mock_get_random_player.return_value = {'Nom': 'Kylian Mbappe', 'Position': 'ST'}

        # On génère une équipe avec une tactique valide et une difficulté invalide
        result = generate_team('433', 'Python')

        # Vérification
        # 1) Vérifier si la fonction retourne None pour une difficulté invalide
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
