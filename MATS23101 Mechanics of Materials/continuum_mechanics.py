# Python file / module (TBD) for the Continuum Mechanics part of Mechanics of Materials (MATS23101) at the University of Manchester.

import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #allows 52 rank tensors?

class Tensor():
    def __init__(self, rank=2, max_index=3):
        self.rank = rank
        self.max = max_index
        self.tensor = None
    
    def _nest(self, layers:int, length:int) -> list:
        """
        Nests a certain amount of lists (length) in a certain amount of layers (layers) 
        """
        return [[] if layers == 0 else self._nest(layers-1, length) for _ in range(length)]
    
    def create(self, values:list) -> list:
        """
        Creates a readable and usable tensor representation given a list of values
        """
        temp_arr = np.array_split(values, len(values)/self.max) #creates the dimensions
        temp_arr = [list(x) for x in temp_arr]
        ##print(temp_arr)
        shell = self._nest(self.rank, self.max) #empty tensor
        tensor = shell
        #to make an self-changing code dependant on the tensor rank
        #I used strings, as they can be iterably modified
        access_code = "tensor"
        for _ in range(0, self.rank-1):
            access_code = access_code + "[" + alphabet[_] + "]" #determines which dimension to access
        access_command = "for a in range(0, self.max):"
        for _ in range(1, self.rank-1): 
            access_command = access_command +"\n" + "    "*_ +"for " + alphabet[_] + " in range(0, self.max):" #iterates through the dimensions regardless of nesting
        cmd = "it=0\n"+ access_command  + "\n" + "    "*(self.rank-1) + access_code + " = temp_arr[it]\n"+"    "*(self.rank-1)+"it+=1"
        ##print(cmd)
        exec(cmd)
        self.tensor = tensor
        return self.tensor

