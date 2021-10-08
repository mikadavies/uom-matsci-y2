# Python file / module (TBD) for the Continuum Mechanics part of Mechanics of Materials (MATS23101) at the University of Manchester.

import numpy as np
import math

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #allows 52 rank tensors?

class Tensor():
    def __init__(self, rank=2, max_index=3, values=[0]*9):
        self.rank = rank
        self.max = max_index
        self.tensor = self.create(values)
    
    def __getitem__(self, item):
        return self.tensor[item] # delegate to self.__getitem__
    
    def _nest(self, layers:int, length:int) -> list:
        """
        Nests a certain amount of lists (length) in a certain amount of layers (layers) 
        """
        return [[] if layers == 0 else self._nest(layers-1, length) for _ in range(length)]
    
    def create(self, values:list) -> list:
        """
        Creates a readable and usable tensor representation given a list of values
        """
        if self.rank == 1:
            self.tensor = values
        else:
            temp_arr = np.array_split(values, len(values)/self.max) #creates the dimensions
            temp_arr = [list(x) for x in temp_arr]
            ##print(temp_arr)
            shell = self._nest(self.rank, self.max) #empty tensor
            tensor = shell
            #to make an self-changing code dependant on the tensor rank
            #I used strings, as they can be modified at will
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
    
    def _rotation_angle_2D(self):
        """
            Calculates the rotation angle of a 2D 2nd order tensor
        """
        return np.arctan((2*self.tensor[0][1])/(self.tensor[0][0]-self.tensor[1][1]))/2
    
    def _rotation_matrix_2D(self):
        """
            Determines the 2D rotation matrix to reach the principal tensor
        """
        a = self._rotation_angle_2D()
        return [[np.cos(a), np.sin(a)], [-np.sin(a), np.cos(a)]]
    
    def rotate(self, R):
        """
            Rotates the tensor through a rotation matrix R
        """
        P = []
        for i in range(self.max):
            r = []
            for j in range(self.max):
                c = 0
                for k in range(self.max):
                    for l in range(self.max):
                        c += R[i][k]*self[k][l]*R[j][l]
                if math.isclose(c, int(c), abs_tol=0.0000001):
                    c = int(c)
                r.append(c)
            P.append(r)
            r = []
        return P
        
    def principal_tensor_2D(self):
        """
            Determines a 2D tensor's principal values
        """
        R = self._rotation_matrix_2D()
        return(self.rotate(R))
    
    def invariants(self):
        """
            Calculates the invariants of 1st and 2nd order tensors
        """
        if self.rank == 1:
            return np.sqrt(dot(self, self))
        elif self.rank == 2:
            i1 = self[0][0] + self[1][1] + self[2][2]
            i2 = self[0][0]*self[1][1] + self[1][1]*self[2][2] + self[0][0]*self[2][2] - self[0][1]*self[1][0] - self[1][2]*self[2][1] - self[0][2]*self[2][0]
            i3 = -self[0][2]*self[1][1]*self[2][0] + self[0][1]*self[1][2]*self[2][0] + self[0][2]*self[1][0]*self[2][1] - self[0][0]*self[1][2]*self[2][1] - self[0][1]*self[1][0]*self[2][2] + self[0][0]*self[1][1]*self[2][2]
            return (i1, i2, i3)
        else: print("ERROR: Tensor.invariants() currently only handles 1st and 2nd order tensors")



def dot(a:Tensor, b:Tensor):
    """
        Calculates the dot product between two first order tensors of equal length
    """
    if a.rank == b.rank == 1:
        if a.max == b.max:
            c = 0
            for i in range(a.max):
                c += a[i] * b[i]
            return c
        else: print("ERROR: dot() only accepts vectors with an equal number of components")
    else: print("ERROR: dot() only accepts rank 1 tensors (vectors)")

def double_contraction(A:Tensor, B:Tensor):
    """
        Calculates the double contraction between two second order tensors of equal length
    """
    if A.rank == B.rank == 2:
        if A.max == B.max:
            c = 0
            for i in range(A.max):
                for j in range(B.max): #this is now a subscript of the list class which uses 0-indexing
                    c += A[i][j] * B[i][j]
            return c
        else: print("ERROR: double_contraction() only accepts matrices with an equal number of components")
    else: print("ERROR: dot() only accepts rank 2 tensors (matrices)")