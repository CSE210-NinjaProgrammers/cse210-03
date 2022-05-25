from game.words import Words
from game.player import Player
from game.drawing import Drawing


class Jumper:
    """
    Responsibility: The game flow. Relating the rest of the entities (players, word list and puzzle).

    Attributes:
    -_is_playing
    -_player
    -_words
    -_drawing
    -_shows_output
    -_wins

    """

    def __init__(self):
        """Constructs a Jumper.

        Args:
            self (Jumper): an instance of Jumper.
        
        """

        self._is_playing = Player()
        self._player = True
        self._words = Words()
        self._drawing  = Drawing()
        self._shows_output = True #extra attributes
        self._wins = False #extra attributes

    def start_game(self):
        """Starts the main game loop

        Args:
            while self._is_playing
        """
        while self._is_playing == True:
            self._display_outputs()
            self._do_updates()
        self._display_outputs()
        self._words.word_list
        print(self._words.word_list)

    def _get_input(self):
        """

        Args:
        """
        pass

    def _do_updates(self):
        """

        Args:
        """
        pass

    def _display_outputs(self):
        """

        Args:
        """
        pass
    



