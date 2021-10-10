# Python file / module (TBD) for the Fluid Mechanics part of Materials Processing (MATS23401) at the University of Manchester.

import numpy as np

class Fluid:
    def __init__(self, density=0, speed=0, viscosity=0, reynolds=0):
        """
        Class for easy storage and manipulation of fluids
        
        Inputs:
            density: Float
            speed: Float
            viscosity: Float
            reynolds: Float
        """
        self.density = density
        self.speed = speed
        self.viscosity = viscosity
        self.reynolds = reynolds
        self.flow = None
        
    def setWater(self):
        """
        Gives fluid the properties of water at 20C
        """
        self.density = 	998.21
        self.viscosity = 1.0016*10**(-3)
        
    def Reynolds(self, diameter, density=0, speed=0, viscosity=0):
        """
        Calculates the Reynolds number
        
        Inputs:
            diameter: Float
            density: Float
            speed: Float
            viscosity: Float
        Output: Float
        """
        if density != 0: self.density = density
        if speed != 0: self.speed = speed
        if viscosity != 0: self.viscosity = viscosity
        self.reynolds = (self.density*self.speed*diameter)/self.viscosity
        return self.reynolds
    
    def Flow(self, Re=0):
        """
        Determines whether the flow is laminar, turbulent or transitional
        
        Inputs:
            reynolds: Float
        Output: String
        """
        if Re != 0: self.reynolds = Re
        if self.reynolds < 2000: self.flow = "Laminar"
        elif self.reynolds < 4000: self.flow = "Transitional"
        else: self.flow = "Turbulent"
        return self.flow

class Pipe:
    def __init__(self, diameter=0, fluid=Fluid()):
        """
        Class for easy storage and manipulation of pipes
        
        Inputs:
            diameter: Float
            fluid: Fluid
        """
        self.diameter = diameter
        self.fluid = fluid
        
    def _area(self):
        """
        Internal function to calculate the area of the pipe (assumed circular cross-section)
        """
        return np.pi*(self.diameter*self.diameter)/4
    
    def Mass_flow_rate(self, diameter=0, speed=0, density=0):
        """
        Calculates the mass flow rate within the pipe
        
        Inputs:
            diameter: Float
            speed: Float
            density: Float
        Output: Float
        """
        if speed !=0: self.fluid.speed = speed
        if density !=0: self.fluid.density = density
        if diameter !=0: self.diameter = diameter
        return self.fluid.density*self.fluid.speed*self._area()
    
    def Vol_flow_rate(self, diameter=0, speed=0):
        """
        Calculates the volumetric flow rate within the pipe assuming non-compressible fluid
        
        Inputs:
            diameter: Float
            speed: Float
        Output: Float
        """
        if speed !=0: self.fluid.speed = speed
        if diameter !=0: self.diameter = diameter
        return self.fluid.speed*self._area()
    
def bernoulli(speed, density, pressure, elevation_head, gravity=9.80665):
    """
    Calculates the total energy given by the bernoulli equation
    """
    return density*speed*speed/2+pressure+density*gravity*elevation_head
