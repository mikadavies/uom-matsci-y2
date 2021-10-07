# Python file / module (TBD) for the Continuum Mechanics part of Mechanics of Materials (MATS23101) at the University of Manchester.

import numpy as np

class Tensor():
    def __init__(self, rank=2, max_index=3):
        self.rank = rank
        self.max = max_index
        self.tensor = None
    
    def _nest(self, layers, length):
        """
            Nests a certain amount of lists (length) in a certain amount of layers (layers) 
            
            Input:
                layers: int
                length: int
                
            Output: list of lists
        """
        return [[] if layers == 1 else self._nest(layers-1, length) for _ in range(length)]
    
    def create(self, values:list):
        """
            Creates a readable and usable tensor representation given a list of values
        
            Input:
                values: list    // format [11, 12, 13 ..., 21, 22, 23...]
        """
        shell = self._nest(self.rank-1, self.max)
        self.tensor = shell
        return self.tensor #TODO: currently returns an empty 'Tensor', with the correct rank
        
