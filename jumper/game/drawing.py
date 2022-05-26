class Drawing:
    """A service that handles console operations.
    
    The responsibility of a Drawing is Drawing the man in the parachute and display in the console.
    """
    def __init__(self):
        """Constructs a new Drawing.

        Args:
            self (Drawing): An instance of Drawing.
            self._image -> It contains the list of drawings of the game's parachute according to the number of failed letters.
            self._dashes -> Stores the underscores as well as the letters that are found in the game
        """
        self.__image = ['''
                  _____
                 /_____\\
                 \     /
                  \   /
                    O 
                   /|\\
                   / \\

                 ^^^^^^^
                    ''','''

                 /_____\\
                 \     /
                  \   /
                    O 
                   /|\\
                   / \\

                ^^^^^^^
                    ''','''

    
                 \     /
                  \   /
                    O 
                   /|\\
                   / \\

                ^^^^^^^
                    ''','''

    
        
                  \   /
                    O 
                   /|\\
                   / \\

                ^^^^^^^        
                    ''','''

    
        
       
                    x 
                   /|\\
                   / \\

                ^^^^^^^        
                        '''
                            ]

        self.__dashes = []  
           
    def draw_parachute(self, value):
        """draw game parachute

        Args:
            self (Drawing): An instance of Drawing.
            value: Stores the index that indicates the drawing that will show according to the available turn
         
        """
        print(self.__image[value])

    def set_dashes(self, len_letters):
        """Stores the first list of underscores on the first turn.

        Args:
            self (Drawing): An instance of Drawing.
            len_letters: Contains the size of the word to print the underscores
         
        """
        for i in range(0,len_letters):
         self.__dashes.append('_') 
    
    def get_dashes(self):
        """Get the list of lines that will be displayed to guess the secret word.

        Args:
            self (Drawing): An instance of Drawing.
        
        """
        
        return self.__dashes
    
    def display_dashes(self, len_letters):
        """Shows the list containing the underscores and the guessed letters.

        Args:
            self (Drawing): An instance of Drawing.
            len_letters: Contains the size of the word to print the underscores
         
         
        """
        for i in range(0,len_letters):
            print(self.get_dashes()[i], end=" ")
    
    def update_dashes_list(self,index,new_value):
        """Update the list containing the underscores and the guessed letters

        Args:
            self (Drawing): An instance of Drawing.
            index: Stores the index of the list to be updated
            new_value: Stores the new value to be updated in the list
        """
        self.__dashes[index] = new_value



