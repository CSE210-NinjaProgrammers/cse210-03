import random
from secrets import choice

class Words:
    """.     
    The responsibility of Words is Managing the secret words and create a list of used letters (so that they don't repeat themselves). 
    Performing the logic to know if the guessed letter actually exists in the word of the current game.
    
    Attributes:
      
    """

    def __init__(self):
        """Constructs a new Words.

        Args:
            self (Words): An instance of Words.
        
        Attributes:
        self._word_list -> List of stored words
        self._current_word -> Stores the selected word from the word list
        self._used_letter_list -> Stores the list of letters the player has used in the game.
        self._current_word_list ->Stores a list with the letters of the selected secret word
        self._number_of_lines -> Stores the number of letters that contains the secret word
        """
        self._word_list = [ "mexico", "colombia", "canada", "venezuela", "uruguay", "argentina","guatemala", 
        "panama", "ecuador","USA","brasil","honduras"]

        self._current_word = ""
        self._used_letter_list = []
        self._current_word_list =[]
        self._number_of_lines = 0

    def get_current_word(self):
         """Get the current random word from the list
        
        Args:
          self (Words): An instance of Words.
           
        """
         return self._current_word
    
    def random_word(self):
        """Stores the current random word from the list
        
        Args:
          self (Words): An instance of Words.
           
        """
        self._current_word = random.choice(self._word_list)
        for word in self._current_word:
           self._current_word_list.append(word) 
    
    def set_used_letter_list(self, value):
        """Update the list of letters used by the player
        
        Args:
          self (Words): An instance of Words.
          value : Contains the typed letter that is stored in the list
           
        """
        
        self._used_letter_list.append(value)
    
    def get_used_letter_list(self):
        """Gets the list of letters used by the user
        
        Args:
          self (Words): An instance of Words.
           
        """
        return self._used_letter_list
    
    def get_current_word_list(self):
        """Get the list of letters that contains the secret word
        
        Args:
          self (Words): An instance of Words.
           
        """
        return self._current_word_list
    
    def get_number_of_lines(self):
        """Gets the number of letters that the secret word has
        
        Args:
          self (Words): An instance of Words.
           
        """
        self._number_of_lines = len(self._current_word)
        return self._number_of_lines
    
 
     
        
