import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from bot import on_message

class TestOnMessage(unittest.IsolatedAsyncioTestCase):
    async def test_on_message_with_randomverse_command(self):
        message_mock = MagicMock()
        message_mock.content = '!randomverse'
        message_mock.channel.send = AsyncMock()

        with patch('bot.on_message', return_value=None) as mock_on_message:
            await on_message(message_mock)

        message_mock.channel.send.assert_called()
    '''     
    async def test_on_message_with_invalid_command(self):
        message_mock = MagicMock()
        message_mock.content = '!invalidcommand'
        message_mock.channel.send = AsyncMock()

        with patch('bot.on_message', return_value=None) as mock_on_message:
            await on_message(message_mock)

        message_mock.channel.send.assert_not_called()
    '''
if __name__ == '__main__':
    unittest.main()
