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
    
            #### ESTABLISH SYSTEM OPTICAL COMPONENTS ####
    lenses = np.array([ OC.Thin_Lens('Lens 1',100,1.5,20,-20),
                        OC.Thin_Lens('Lens 2',130,1.5,20,-20)])        
    objects = np.array([OC.Object_or_Image('Arrow_0',90,100)])       

            #### ITTERATE THROUGH SYSTEM ####
    for I in range (len(lenses)):                   # in the optical system
            
        si = lenses[I].image_distance(objects[I])   # image dist. from I-th lens
        so = lenses[I].x - objects[I].x             # obj dist. from I-th lens
        xn = lenses[I].x + si                       # obj dist. from origin
        mag = OC.magnification(si,so)               # transvere magnification factor
        
        image_name = 'Arrow_'+str(I+1)              # system obj/image name
        image_height = objects[I].h * mag           # compute height of image
        
        image = OC.Object_or_Image(image_name,xn,image_height)  # create instance
        objects = np.append(objects,image)          # add the image object to the 
          
            #### PRINT SYSTEM DETAILS & PLOT SYSTEM ####

    OC.Print_System_Lenses(lenses)
    OC.Plot_System(lenses,objects,'Simple_Optical_System_1',save=True,show=True)