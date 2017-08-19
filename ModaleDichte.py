import numpy as np
import math
import matplotlib

#def ModaleDichte(c_L, c_S, c_B_eff, c_g_eff, Geometry, Isotrop, Bending, Compressional, Shear, Sum):
def ModaleDichte(c_L, c_S, c_B_eff, c_g_eff, Geometry, Isotrop, freq ):

    Subs = 1



    # allocate numpy arrays
    
    n_f = np.zeros(freq.size)
    delta_f_bend = np.zeros(freq.size)
    delta_f_comp = np.zeros(freq.size)
    delta_f_shear = np.zeros(freq.size)

    bending_np = np.zeros(freq.size)
    compressional_np = np.zeros(freq.size)
    shear_np = np.zeros(freq.size)
    sum_np = np.zeros(freq.size)

    Length = Geometry[ 0 ][ 0 ]
    Width = Geometry[ 0 ][ 1 ]

    # Flaeche der Platte
    Area = Length * Width
    CoeffOne = 2.0 * math.pi
    CoeffTwo = CoeffOne * Area

    ## Isotrope Berechnung
    if Isotrop == True:

        for s in range(Subs):


            for i in range(freq.size):
                n_f[ i ] = ( CoeffTwo * freq[ i ] ) / ( c_B_eff * c_g_eff[ i ] )
                delta_f_bend[ i ] = 1.0 / n_f[ i ]
                delta_f_comp[ i ] = ( c_L[ i ] * c_L[ i ] ) / ( CoeffTwo * freq[ i ] )
                delta_f_shear[ i ] = c_S * c_S / ( CoeffTwo * freq[ i ] )
                bending_np[ i ] = 1.0 / ( CoeffOne * delta_f_bend[ i ] )
                compressional_np[ i ] = 1.0 / ( CoeffOne * delta_f_comp[ i ] )
                shear_np[ i ] = 1.0 / ( CoeffOne * delta_f_shear[ i ] )
                sum_np = bending_np[ i ] + shear_np[ i ] + compressional_np[ i ]
                pass

            #n_f = 2*math.pi*A*freq[ i ]/(c_B_eff[s,i]*c_g_eff[s,i])  # elemetwise multipl
            
            #delta_f_bend = 1./n_f # n_f, delta_f_bend, delta_f_comp, delta_f_shear - vectors
            
            #delta_f_comp=c_L[s,:]**2./(2*math.pi*freq*A) #Lyon (8.2.8), S. 141
            
            #delta_f_shear=c_S[s,:]**2./(2*math.pi*freq*A) #Lyon (8.2.9), S. 141
            
            
            #bending_np[s,:]=1./(2*math.pi*delta_f_bend)
            
            #compressional_np[s,:]=1./(2*math.pi*delta_f_comp)
            
            #shear_np[s,:]=1./(2*math.pi*delta_f_shear)
                   
            
            #sum_np=bending_np+shear_np+compressional_np


    ## Orthotrope Berechnung
    elif Isotrop == False:
        
        for s in range(Subs):

            '''
            Length = Geometry[ s ][ 0 ]
            Width = Geometry[ s ][ 1 ]

            # Flaeche der Platte
            Area = Length * Width
            CoeffOne = 2.0 * math.pi
            CoeffTwo = CoeffOne * Area
            '''

            for i in range( freq.size ):
                n_f[ i ] = ( CoeffTwo * freq[ i ] ) / ( c_B_eff[ i ] * c_g_eff[ i ] )
                delta_f_bend[ i ] = 1.0 / n_f[ i ]
                delta_f_comp[ i ] = ( c_L[ i ] * c_L[ i ] ) / ( CoeffTwo * freq[ i ] )
                delta_f_shear[ i ] = c_S * c_S / ( CoeffTwo * freq[ i ] )
                bending_np[ i ] = 1.0 / ( CoeffOne * delta_f_bend[ i ] )
                compressional_np[ i ] = 1.0 / ( CoeffOne * delta_f_comp[ i ] )
                shear_np[ i ] = 1.0 / ( CoeffOne * delta_f_shear[ i ] )
                sum_np = bending_np[ i ] + shear_np[ i ] + compressional_np[ i ]
                pass

            '''
            n_f = 2.*math.pi*A*freq/(c_B_eff[s,:]*c_g_eff[s,:])
            
            delta_f_bend = 1./n_f
            delta_f_comp=c_L[s,:]**2./(2*math.pi*freq*A) #Lyon (8.2.8), S. 141
            delta_f_shear=c_S[s,:]**2./(2*math.pi*freq*A) #Lyon (8.2.9), S. 141
            bending_np[s,:]=1./(2*math.pi*delta_f_bend)
            compressional_np[s,:]=1./(2*math.pi*delta_f_comp)
            shear_np[s,:]=1./(2*math.pi*delta_f_shear)
            
            sum_np=bending_np+shear_np+compressional_np
            '''


    #del Bending[:]
    #del Compressional[:]
    #del Shear[:]
    #del Sum[:]

    #Bending.extend(bending_np.tolist())
    #Compressional.extend(compressional_np.tolist())
    #Shear.extend(shear_np.tolist())
    #Sum.extend(sum_np.tolist())


    # Prepare data that have to be returned from the function
    Result = [ bending_np.tolist(),         #eff bemding
               compressional_np.tolist( ),  #quasi/longitudinal
               shear_np.tolist( ),
               sum_np.tolist( ) ]

    return Result