from game.drawing import Drawing
from game.words import Words
from game.player import Player

class Jumper:
    """A person who directs the game. 
    
    The responsibility of a Jumper is the game flow. Relating the rest of the entities (players, word list and puzzle)

    Attributes:
     
    """

    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        
        Attributes:
        self._player -> Player class instance
        self._is_playing -> Indicates whether the game continues or not
        self._words -> Instance of the words class
        self._drawing -> Instance of the drawings class
        self._first_time -> Indicates if it is the first output to show on the game console
        self._winner -> Indicates if the player is a winner or not
        """
        self._player = Player()
        self._is_playing = True
        self._words = Words()
        self._drawing = Drawing()
        self._first_time = True
        self._winner = False
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Jumper): an instance of Jumper.
             while self._is_playing:
        """
        while self._is_playing == True:
            self._display_outputs()
            self._get_input()
            self._do_updates()
        
        self._display_outputs()

        
    def _get_input(self):
        """Show in the console the question addressed to the user to guess the secret word

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._player.type_letter("Guess a letter [a-z]: ")

    def _do_updates(self):
        """Perform game validations and updates

        Args:
            self (Jumper): An instance of Jumper.
        """
        while (self._player.get_typed_letter().lower() in self._words.get_used_letter_list() or not self._player.get_typed_letter().isalpha() or len(self._player.get_typed_letter().lower())>1):
            print("The typed letter you have already used or it is not a letter from a-z, Please type again!")
            self._get_input()

        if self._player.get_typed_letter().lower() in self._words.get_current_word():
            for index in range(0,self._words.get_number_of_lines()):
                if self._words.get_current_word_list()[index] == self._player.get_typed_letter().lower():
                    self._drawing.update_dashes_list(index,self._player.get_typed_letter().lower())

            if self._drawing.get_dashes() == self._words.get_current_word_list():
                self._is_playing = False
                self._winner = True
        else:
            self._player.set_players_turn(1)
            if self._player.get_players_turn() == 4:
                self._is_playing = False

        self._words.set_used_letter_list(self._player.get_typed_letter().lower())
        
    def _display_outputs(self):
        """Shows the outputs of the game.

        Args:
            self (Jumper): An instance of Jumper.
        """
        if self._first_time == True:
            self._words.random_word()
            self._drawing.set_dashes(self._words.get_number_of_lines())
            self._first_time = False
        else:
            print("\nRecently used letters: ", end=" ")
            for letter in self._words.get_used_letter_list():
             print(f'{letter}',end=",")
            print()

        self._drawing.display_dashes(self._words.get_number_of_lines())
        self._drawing.draw_parachute(self._player.get_players_turn())
        
        if self._player.get_players_turn() == 4:
            print("Sorry you lost the game :(")
        
        if self._winner == True:
            print("Congratulations, you've guessed the secret word!")
        

      

    
  