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

class Thin_Lens ():
    """
    Creates Thin Lens Class Object
    --------------------------------
    name (str) : Name to indentify object
    x (float) : Position on x-axis where center of lens sits
    ref_idx (float) : index of refraction of thin lens
    R1 (float) : radius of curvature 1 of lens
    R2 (float) : radius of curvature 2 of lens
    --------------------------------
    """
    def __init__(self,name,x,ref_idx,R1,R2):
        """ Initiaialize Thin Lens Class Object """
        self.name = name                # name of object
        self.x = x                      # horizontal position
        self.n = ref_idx                # refraction idx
        self.R1 = R1                    # rad of curve 1
        self.R2 = R2                    # rad of curve 2
        self.f = self.focus()           # focal length
        self.type = self.lens_type()    # lens type

    def focus (self):
        """ Compute magnitude of focus from center of thin lens """
        try:
            val = (self.n - 1)*(1/self.R1-1/self.R2)
            print(val)
            return 1/val                # return 1/f len
        except ZeroDivisionError:
            print("\n\tERROR! - Focal length set to infinity")
            return np.infty

    def lens_type(self):
        """ Determine lens type based on radii of curvature """
        if (self.R1 > 0) and (self.R2 < 0):
            return 'Biconvex'           # biconvex lens
        if (self.R1 > 1e6) and (self.R2 < 0):
            return 'Planar - Convex'    # planar convex lens
        if (self.R1 > 0) and (self.R2 > 0):
            return 'Meniscus - Convex'  # meniscus convex len
        if (self.R1 < 0) and (self.R2 > 0):
            return 'Biconcave'          # bicondave lens
        if (self.R1 > 1e6) and (self.R2 > 0):
            return 'Planar - Concave'   # planar concave lens
        if (self.R1 > 0) and (self.R2 > 0):
            return 'Meniscus Concave'   # meniscus concave lens

    def image_distance(self,obj):
        """ Compute image distance from lens instance """
        d = obj.x - self.x              # distance between obj & lens
        si = (1/self.f - 1/d)**-1       # image distance
        return si                       # return image distance 
    
class Object_or_Image ():
    """
    Creates Object to image Class Object 
    --------------------------------
    name (str) : Name to indentify object
    x (float) : Position on x-axis where center of lens sits
    height (float) : height of object/image
    n (int) : system image number (0 idx)
    --------------------------------
    """
    def __init__(self,name,x,height,n):
        """ Initialize Object\Image Class Object """
        self.name = name                # name of object
        self.x = x                      # position of object/image
        self.h = height                 # height of object/image
        self.num = n                    # object number
        self.type = self.image_type()   #  type of image

    def image_type (self):
        """ Determine if image is real or virtual """
        return None

            #### FUNCTION DEFINTIONS ####

def magnification (si,so):
    """ Compute Transverse Magnification Factor """
    return -si/so                   # return mag fact

def Print_System_Lenses (lenses):
    """ Print all System Lens Parameters """
    for I in range (len(lenses)):               # for each lens in the system
        print("================================")
        print("Component Number: "+str(I+1))
        print("\tName:",lenses[I].name)
        print("\tComponent type:",lenses[I].type,"lens")
        print("\tX-Axis Postion:",lenses[I].x)
        print("\t1st Curvature radius:",lenses[I].R1)
        print("\t2nd Curvature radius:",lenses[I].R2)
        print("\tFocal length:",lenses[I].f)
        print("")

def Print_System_Object (object):
    """ Print Object Parameters for a single object """
    print("================================")
    print("Object Number: ",object.num)
    print("\tName:",object.name)
    print("\tImage type:",object.type)
    print("\tX-Axis Postion:",object.x)
    print("\tImage Height:",object.h)
    print("")

 
def Plot_System (lenses,objects,title,save=False,show=False):
    """ Produce Matplotlib Visualization of Optical System """
            #### Initialize Figure ####
    plt.figure(figsize=(20,8))                  # create and size figure
    plt.title(title,size=40,weight='bold')      # title and format
    plt.xlabel("X-Axis Position [cm]",\
        size=20,weight='bold')                  # label x axis
    plt.ylabel("y-Axis Position [cm]",\
        size=20,weight='bold')                  # label y axis
            #### Plot all Lense ####
    for lens in lenses:             # for each optical lens
        try:                        # attempt:
            fs = [(lens.x-lens.f),(lens.x+lens.f)]
            plt.plot(fs,[0,0],'o',
                     label=str(lens.name)+' Foci')
            plt.plot([lens.x,lens.x],[+100,-100],
                     linewidth=4)
            plt.annotate(str(lens.name),(lens.x,100))
        except:
            print("\n\tERROR! - Could not plot object",lens.name)

    for obj in objects:
        try:                        # attempt:          
            plt.plot([obj.x,obj.x],[obj.h,0])
            plt.annotate(str(obj.name),(obj.x,obj.h))
        except:                     # if failure
            print("\n\tERROR! - Could not plot object",obj.name)
    
    comps = np.append(lenses,objects)
    xmin = np.min([x.x for x in comps])-10
    xmax = np.max([x.x for x in comps])+10

    plt.hlines(y=0,xmin=xmin,xmax=xmax,color='black')
    plt.tight_layout()
    plt.legend()
    plt.grid()
    if save == True:
        plt.savefig(str(title)+'.png')
    if show == True:
        plt.show()
    plt.close()
