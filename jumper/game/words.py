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

        self._word_list = ['football', 'basketball', 'husband', 'wife', 'chimney', 'chemical', 'pizza', 'hamburger', 'barbecue', 'teacher', 'school', 'commandments'] #Put the Eric Idea
        self._current_word = random.choice(self._word_list)
        self._used_letter_list = []
        self._lines
        self._numbers_of_lines 

    

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

