from blackjack_project import __version__
from blackjack_project import Main

class Test:
    """
    Main .py file tests.
    """

    def test_version():
        assert __version__ == '0.1.0'
