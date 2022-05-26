
import random
import urllib.request


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
        self._current_word -> Stores the selected word from the word list
        self._used_letter_list -> Stores the list of letters the player has used in the game.
        self._current_word_list ->Stores a list with the letters of the selected secret word
        self._number_of_lines -> Stores the number of letters that contains the secret word
        """     
        self.__current_word = ""
        self.__used_letter_list = []
        self.__current_word_list =[]
        self.__number_of_lines = 0
        self.__get_random_words()

    def __get_random_words(self):
        """Get random words from mit site
        
        Args:
          self (Words): An instance of Words.
           
        """
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        content = urllib.request.urlopen(word_site).read().decode('UTF-8')
        words = content.splitlines()
        self.__set_current_word(words)

    
    def __set_current_word(self, words):

        """Store a secret word in a current_word attribute and save letters in _current_word_list
        
        Args:
          self (Words): An instance of Words.
           
        """
      
        self.__current_word = random.choice(words)
        for letter in self.__current_word:
           self.__current_word_list.append(letter) 

    
    def get_current_word(self):
         """Get the current random word from the list
        
        Args:
          self (Words): An instance of Words.
           
        """
         return self.__current_word     
    
    def set_used_letter_list(self, value):
        """Update the list of letters used by the player
        
        Args:
          self (Words): An instance of Words.
          value : Contains the typed letter that is stored in the list
           
        """
        
        self.__used_letter_list.append(value)
    
    def get_used_letter_list(self):
        """Gets the list of letters used by the user
        
        Args:
          self (Words): An instance of Words.
           
        """
        return self.__used_letter_list
    
    def get_current_word_list(self):
        """Get the list of letters that contains the secret word
        
        Args:
          self (Words): An instance of Words.
           
        """
        return self.__current_word_list
    
    def get_number_of_lines(self):
        """Gets the number of letters that the secret word has
        
        Args:
          self (Words): An instance of Words.
           
        """
        self.__number_of_lines = len(self.__current_word)
        return self.__number_of_lines
    
 
     
        
