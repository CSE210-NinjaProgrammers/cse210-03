import urllib.request
import random

class Words:
    """Responsibility:
    Managing the secret words and create a list of used letters (so that they don't repeat themselves). Performing the logic to know if the guessed letter actually exists in the word of the current game.

    Attributes:
    - _word_list
    - _current_word
    - _used_letter_list
    - _lines
    - _numbers_of_lines 
    """

    def __init__(self):
        """Constructs the words.

        Args:

        """ 

        self.word_list = []
        self.__get_random_words()
        # self.current_word = random.choice(self.word_list)
        # self._used_letter_list = []
        # self._lines
        # self._numbers_of_lines 

    
    def __get_random_words(self):
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        content = urllib.request.urlopen(word_site).read().decode('UTF-8')
        words = content.splitlines()
        self.__set_current_word(words)

    

    def __set_current_word(self, words):
        self.word_list = random.choice(words)

    def get_current_word(self):
        """

        Args:
        """
        

    def _random_word(self):
        """

        Args:
        """
        current_state = ['_'] * len(self._word_list)
        print(current_state)

    def set_used_letter_list(self):
        """

        Args:
        """
        pass

    def get_used_letter_list(self):
        """

        Args:
        """
        alphabet = ['a', 'b','c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x','y','z']

        kicks = []

        while True:
            kick = input('Guess a letter [a-z]: ')
            if kick not in alphabet or kick == '':
                print('Invalid Option Try Again!')
            elif kick in kicks:
                print('Letter already chosen')
            kicks.append(kick)



    def set_lines(self):
        """

        Args:
        """
        pass   

    def get_lines(self):
        """

        Args:
        """
        pass   

    def get_numers_of_lines(self):
        """

        Args:
        """
        pass 

    def set_numers_of_lines(self):
        """

        Args:
        """
        pass                           

