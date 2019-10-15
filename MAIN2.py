"""
Landon Buell
Keesee
PHYS 708.01
15 October 2019
"""

            #### IMPORTS ####

import numpy as np
import matplotlib.pyplot as plt
import Optical_Components as OC

            #### MAIN EXECUTABLE FUNCTION ####

if __name__ == '__main__':

    objects = OC.Object_or_Image('Arrow',0,1)               # objects to image
    system = np.array([OC.Thin_Lens('Lens 1',0.1,1,1.5)])   # all lenses in system

    for I in range (len(system)):                       # in the optical system
        pass