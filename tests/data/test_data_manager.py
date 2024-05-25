import unittest
from unittest.mock import patch, mock_open
from src.data.data_manager import DataManager


class TestDataManager(unittest.TestCase):

    @patch(
        "src.data.data_manager.open",
        new_callable=mock_open,
        read_data='{"key": "value"}',
    )
    def test_load_commands(self, mock_file):
        manager = DataManager()
        commands = manager.load_commands()
        self.assertEqual(commands, {"key": "value"})

    @patch("src.data.data_manager.open", new_callable=mock_open)
    def test_save_commands(self, mock_file):
        manager = DataManager()
        manager.save_commands({"key": "value"})
        mock_file.assert_called_once_with("commands.json", "w")

    @patch(
        "src.data.data_manager.open",
        new_callable=mock_open,
        read_data='{"GROQ_API_KEY": "key", "GROQ_MODEL": "model"}',
    )
    def test_load_settings(self, mock_file):
        manager = DataManager()
        settings = manager.load_settings()
        self.assertEqual(settings, {"GROQ_API_KEY": "key", "GROQ_MODEL": "model"})

    @patch("src.data.data_manager.open", new_callable=mock_open)
    def test_save_settings(self, mock_file):
        manager = DataManager()
        manager.save_settings({"GROQ_API_KEY": "key", "GROQ_MODEL": "model"})
        mock_file.assert_called_once_with("settings.json", "w")


if __name__ == "__main__":
    unittest.main()
