"""
Landon Buell
Keesee
PHYS 708.01
9 October 2019
"""

            #### IMPORTS ####

import numpy as np
import matplotlib.pyplot as plt
import Optical_Components as OC

            #### MAIN EXECUTABLE FUNCTION ####

if __name__ == '__main__':

            #### Define Components in Optical System ####

    comp1 = OC.Thick_Lens('lens1',Rs=(0.01,0.01),x=1,d=0.01,ref_idx=1.5)

    system = np.array([comp1])          # all components in optical system
    sys_mat = np.identity(2)            # system matrix

            #### Ray's Path Through System ####

    sys_mat = comp1.system_matrix()
    print(sys_mat)
    print(np.linalg.det(sys_mat))
