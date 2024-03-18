import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from bot import on_message
import requests
from src.pokemon import get_random_pokemon

class TestOnMessage(unittest.IsolatedAsyncioTestCase):
    @patch('src.pokemon.requests.get')
    async def test_on_message_with_randomverse_command(self, mock_get):
        message_mock = MagicMock()
        message_mock.content = '!randomverse'
        message_mock.channel.send = AsyncMock()

        with patch('bot.on_message', return_value=None) as mock_get_random_ayah:
            mock_get_random_ayah.return_value = {'quran-uthmani': 'Verse 1', 'en.asad': 'Verse 2'}
            await on_message(message_mock)

        message_mock.channel.send.assert_called()

    async def test_on_message_with_randomwiki_command(self):
        message_mock = MagicMock()
        message_mock.content = '!randomwiki'
        message_mock.channel.send = AsyncMock()

        with patch('bot.get_random_wikipedia_page') as mock_get_random_wikipedia_page:
            mock_get_random_wikipedia_page.return_value = ('Random Wikipedia Page', 'https://en.wikipedia.org/wiki/Random_Page')
            await on_message(message_mock)

    async def test_on_message_with_randompokemon_command(self):
        message_mock = MagicMock()
        message_mock.content = '!randompokemon'
        message_mock.channel.send = AsyncMock()

        with patch('bot.get_random_pokemon') as mock_get_random_pokemon:
            mock_get_random_pokemon.return_value = ('Pikachu', 25, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png')
            await on_message(message_mock)

        message_mock.channel.send.assert_called()

    @patch('src.pokemon.requests.get')
    async def test_sprite_url(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        pokemon_name, pokemon_number, sprite_url = get_random_pokemon()
        response = requests.get(sprite_url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
