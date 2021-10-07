# Python file / module (TBD) for the Continuum Mechanics part of Mechanics of Materials (MATS23101) at the University of Manchester.
# This file is deprecated

import numpy as np

class Tensor():
    def __init__(self, order:int, xx=0, xy=0, xz=0, yx=0, yy=0, yz=0, zx=0, zy=0, zz=0):
        """
            A class to easily store and manipulate tensors
        """
        self.order = order
        self.xx = xx
        self.xy = xy
        self.xz = xz
        self.yx = yx
        self.yy = yy
        self.yz = yz
        self.zx = zx
        self.zy = zy
        self.zz = zz
        if self.order == 0:
            self.tensor = self.xx
        if self.order == 1:
            self.tensor = [self.xx, self.xy, self.xz]
        else:
            self.tensor = [[self.xx, self.xy, self.xz],[self.yx, self.yy, self.yz], [self.zx, self.zy, self.zz]]
        
    def rotation_angle_2D(self):
        """
            Determines the rotation angle of a 2D 2nd order tensor
        """
        return np.arctan((2*self.xy)/(self.xx-self.yy))/2
    
    def _rotation_matrix_2D(self):
        """
            Determines the 2D rotation matrix
        """
        a = self.rotation_angle_2D()
        return [[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]]
    
    def principal_tensor_2D(self): # TODO: Implement tensor rotation
        """
            Determines the 2D principal tensor
        """
        R = self._rotation_matrix_2D()
        
            
    
    def invariants(self):
        """
            Determines the principal invariant(s) of first and second order tensors
        """
        if self.order == 1:
            return np.sqrt(dot(self, self))
        elif self.order == 2:
            i1 = self.xx + self.yy + self.zz
            i2 = self.xx*self.yy + self.yy*self.zz + self.xx*self.zz - self.xy*self.yx - self.yz*self.zy - self.xz*self.zx
            i3 = -self.xz*self.yy*self.zx + self.xy*self.yz*self.zx + self.xz*self.yx*self.zy - self.xx*self.yz*self.zy - self.xy*self.yx*self.zz + self.xx*self.yy*self.zz
            return (i1, i2, i3)
        else: print("Error: This currently only handles 1st and 2nd order tensors")
        
        
def dot(a:Tensor, b:Tensor):
    """
        Calculate the dot product between two 1st order tensors, or one 1st and one 2nd
    
        Input:
            a: Tensor
            b: Tensor
        
        Output:
            c: float  \\ for first order tensors
            c: Tensor  \\ for a second order tensor
    """
    if a.order == 2:
        c1 = a[0][0]*b[0]+a[0][1]*b[1]+a[0][2]*b[2]
        c2 = a[1][0]*b[0]+a[1][1]*b[1]+a[1][2]*b[2]
        c3 = a[2][0]*b[0]+a[2][1]*b[1]+a[2][2]*b[2]
        return Tensor(1, c1, c2, c3)
    elif b.order == 2:
        c1 = b[0][0]*a[0]+b[0][1]*a[1]+b[0][2]*a[2]
        c2 = b[1][0]*a[0]+b[1][1]*a[1]+b[1][2]*a[2]
        c3 = b[2][0]*a[0]+b[2][1]*a[1]+b[2][2]*a[2]
        return Tensor(1, c1, c2, c3)
    else:
        c = 0
        for i in range(2):
            c += a[i] * b[i]
        return c
    
def double_contraction(A:Tensor, B:Tensor):
    """
        Calculate the double contraction between two second order tensors
    
        Input:
            a: Tensor
            b: Tensor
        
        Output:
            c: float
    """
    c = 0
    for i in range(2):
        for j in range(2):
            c += A[i][j] * B[i][j]
    return c
