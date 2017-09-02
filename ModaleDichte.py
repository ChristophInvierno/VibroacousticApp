import numpy as np
import math
import matplotlib

#def ModaleDichte(c_L, c_S, c_B_eff, c_g_eff, Geometry, Isotrop, Bending, Compressional, Shear, Sum):
def ModaleDichte(c_L, c_S, c_B_eff, c_g_eff, Geometry, Isotrop, freq ):

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


    for i in range(freq.size):
        n_f[ i ] = ( CoeffTwo * freq[ i ] ) / ( c_B_eff[ i ] * c_g_eff[ i ] )
        delta_f_bend[ i ] = 1.0 / n_f[ i ]
        delta_f_comp[ i ] = ( c_L[ i ] * c_L[ i ] ) / ( CoeffTwo * freq[ i ] )
        delta_f_shear[ i ] = c_S * c_S / ( CoeffTwo * freq[ i ] )
        bending_np[ i ] = 1.0 / ( CoeffOne * delta_f_bend[ i ] )
        compressional_np[ i ] = 1.0 / ( CoeffOne * delta_f_comp[ i ] )
        shear_np[ i ] = 1.0 / ( CoeffOne * delta_f_shear[ i ] )
        sum_np = bending_np[ i ] + shear_np[ i ] + compressional_np[ i ]



    # Prepare data that have to be returned from the function
    Result = { "bending" : bending_np.tolist(),         #eff bemding
               "compressional" : compressional_np.tolist( ),  #quasi/longitudinal
               "shear" : shear_np.tolist( ),
               "sum" : sum_np.tolist( ) }

    return Result