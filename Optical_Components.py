"""
Landon Buell
Keesee
PHYS 708.01
9 October 2019
"""

            #### IMPORTS ####

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch

            #### CLASS OBJECTS ####

class Thick_Lens ():
    """
    Creates Thick Lens Class Object
    --------------------------------
    name (str) : Name to indentify object
    Rs (tup,list) : list of radii of curvature for lens faces
    x (float) : Position on x-axis where center of lens sits
    d (float) : diameter of lens object
    ref_idx (float) : Index of Refraction of lens object
    --------------------------------

    """

    def __init__(self,name,Rs,x,d,ref_idx):
        """ Initialize Class Object """
            #### Given Attributes ####
        self.name = name                # name the object
        self.rad1 = Rs[0]               # rad of curv for face 1
        self.rad2 = Rs[1]               # rad of curv for face 2
        self.diam = d                   # axial thickness
        self.height = 2                 # lens height
        self.xpos = x                   # position of center of lens
        self.n = ref_idx                # refractive index
        self.comptype = 'thick_lens'    # component type
            #### Lens Attributes ####
        self.L_edge = self.xpos - (self.diam/2)
        self.R_edge = self.xpos + (self.diam/2)
        self.top = +0.5
        self.bottom = -0.5

    def R1_mat (self):
        """ Compute refraction matrix for thick lens """
        pwr = (self.n-1)/self.rad1                  # power of surface
        R1 = np.array([[1,-pwr],[0,1]],dtype=float) # refraction matrix
        setattr(self,'R1_mat',R1)                   # set as new attr
        return R1                                   # return matrix

    def R2_mat (self):
        """ Compute refraction matrix for thick lens """
        pwr = (self.n-1)/self.rad2                  # power of surface
        R2 = np.array([[1,-pwr],[0,1]],dtype=float) # refraction matrix
        setattr(self,'R2_mat',R2)                   # set as new attr
        return R2                                   # return matrix
        
    def TR_mat (self):
        """ Transfer matrix for lens object """
        C = self.diam/self.n                           # Cth idx of matrix
        Tr =  np.array([[1,0],[C,1]],dtype=float)   # transfer matrix 
        setattr(self,'TR_mat',Tr)                   # set as new attr
        return Tr                                   # return matrix

    def system_matrix (self):
        """ Compute system matrix for optical component """
        R1 = self.R1_mat()              # refraction matrix 1
        R2 = self.R2_mat()              # refraction matrix 2
        Tr = self.TR_mat()              # transfer matrix
        B = np.matmul(Tr,R1)
        A = np.matmul(R2,B)             # system matrix
        setattr(self,'sys_mat',A)       # create attr
        return A                        # return system matrix



            #### FUNCTION DEFINITIONS ####

def free_space (x):
    """ Compute Transfer matrix for distance 'd' in free space """
    return np.array([1,x,0,1],dtype=float).reshape(2,2)     # return the matrix

 

