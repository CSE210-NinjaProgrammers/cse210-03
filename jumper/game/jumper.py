from game.words import Words


class Jumper:
    """
    Responsibility: The game flow. Relating the rest of the entities (players, word list and puzzle).

    Attributes:
    -_is_playing
    -_player
    -_words
    -_drawing

    """

    def __init__(self):
        """Constructs a Jumper.

        Args:
            self (Jumper): an instance of Jumper.?
        """

        self._is_playing = True
        self._player = True
        self._words = Words()
        self._drawing  = True

    def start_game(self):
        """

        Args:
        """
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
    



