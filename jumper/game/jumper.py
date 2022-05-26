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
        self.__player = Player()
        self.__is_playing = True
        self.__words = Words()
        self.__drawing = Drawing()
        self.__first_time = True
        self.__winner = False
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Jumper): an instance of Jumper.
             while self._is_playing:
        """
        while self.__is_playing == True:
            self.__display_outputs()
            self.__get_input()
            self.__do_updates()
        
        self.__display_outputs()

        
    def __get_input(self):
        """Show in the console the question addressed to the user to guess the secret word

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.__player.type_letter("Guess a letter [a-z]: ")

    def __do_updates(self):
        """Perform game validations and updates

        Args:
            self (Jumper): An instance of Jumper.
        """
        while (self.__player.get_typed_letter().lower() in self.__words.get_used_letter_list() or not self.__player.get_typed_letter().isalpha() or len(self.__player.get_typed_letter().lower())>1):
            print("The typed letter you have already used or it is not a letter from a-z, Please type again!")
            self.__get_input()

        if self.__player.get_typed_letter().lower() in self.__words.get_current_word():
            for index in range(0,self.__words.get_number_of_lines()):
                if self.__words.get_current_word_list()[index] == self.__player.get_typed_letter().lower():
                    self.__drawing.update_dashes_list(index,self.__player.get_typed_letter().lower())

            if self.__drawing.get_dashes() == self.__words.get_current_word_list():
                self.__is_playing = False
                self.__winner = True
        else:
            self.__player.set_players_turn(1)
            if self.__player.get_players_turn() == 4:
                self.__is_playing = False

        self.__words.set_used_letter_list(self.__player.get_typed_letter().lower())
        
    def __display_outputs(self):
        """Shows the outputs of the game.

        Args:
            self (Jumper): An instance of Jumper.
        """
        if self.__first_time == True:
            self.__drawing.set_dashes(self.__words.get_number_of_lines())
            self.__first_time = False
        else:
            print("\nRecently used letters: ", end=" ")
            for letter in self.__words.get_used_letter_list():
             print(f'{letter}',end=",")
            print()

        self.__drawing.display_dashes(self.__words.get_number_of_lines())
        self.__drawing.draw_parachute(self.__player.get_players_turn())
        
        if self.__player.get_players_turn() == 4:
            print(f"Sorry you lost the game, the word was: {self.__words.get_current_word()}")
        
        if self.__winner == True:
            print("Congratulations, you've guessed the secret word!")
        

      

    
  