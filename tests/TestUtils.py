import unittest
from unittest.mock import patch, MagicMock

from utils.utils import download_image


class TestDownloadImage(unittest.TestCase):
    @patch('requests.get')
    def test_download_image_success(self, mock_get):
        # Composer le mock pour une réponse réussie
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'image_data'
        mock_get.return_value = mock_response

        # Appeler la fonction download_image avec une URL valide
        result = download_image('https://media.contentapi.ea.com/content/dam/ea/easfc/fc-24/ratings/common/full/player-portraits/p262848.png.adapt.50w.png')

        # Vérifier si la fonction retourne les données de l'image
        self.assertEqual(result, b'image_data')

    @patch('requests.get')
    def test_download_image_failure(self, mock_get):
        # Composer le mock pour une réponse échouée
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Appeler la fonction download_image avec une URL invalide
        result = download_image('https://media.contentapi.ea.com/content/dam/ea/easfc/fc-24/ratings/common/full/player-portraits/p26288848.png.adapt.50w.png')

        # Vérifier si la fonction retourne None en cas d'échec du téléchargement
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
