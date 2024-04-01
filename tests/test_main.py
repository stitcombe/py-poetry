import unittest
from unittest.mock import patch
from src.main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_once_with("Hello, World!")


if __name__ == "__main__":
    unittest.main()
