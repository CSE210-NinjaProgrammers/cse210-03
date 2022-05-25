import random

class Player:
    """The person who guess the letter . 
    
    The responsibility of a Player is Type the letter and guess the secret word.
    
    Attributes:
 
    """

    def __init__(self):
        """Constructs a new Player.

        Args:
            self (Player): An instance of Player.
        
        Attributes:
        self._typed_letter -> Stores the letter that the player types
        self._players_turn -> Stores the count of the player's available turns up to 5 turns.
        """
        self._typed_letter = ""
        self._players_turn = 0
        
    def type_letter(self, prompt):
        """Type the letter the players enters
        
        Args:
          self (Player): An instance of Player.
          prompt : Text to display in the console
           
        """
        self._typed_letter = input(prompt)
        
    def get_typed_letter(self):
        """ Gets the letter typed by the user

        Args:
            self (Player): An instance of Player.
        """
        return self._typed_letter
    
    def get_players_turn(self):
        """ Gets the turns used by the player.

        Args:
            self (Player): An instance of Player.
        """
        return self._players_turn
    
    def set_players_turn(self, next_turn):
        """ Update turns used

        Args:
            self (Player): An instance of Player.
            next_turn: Contains the number that will be used to update the count of turns used.
        """
        
        self._players_turn += next_turn