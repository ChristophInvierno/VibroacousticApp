import math
import numpy as np
import matplotlib.pyplot as plt
from ModaleDichte import *
from wave_speeds import *


def ModesInBand( ElasticModulusData,
                 ShearModulusData,
                 PoissonRatiosData,
                 MaterialPropertiesData,
                 GeometryPropertiesData,
                 Isotrop,
                 freq ):

    fmstart = freq[ 0 ]
    fmend = freq[ -1 ]
    #    fmstart = 0.9765625
    #    fmend = 16000

    B = 1.0 / 3.0
    Baender = (1.0 / B ) * np.log2( fmend / fmstart ) + 1.0
    i = np.linspace( 1, Baender, Baender, dtype = int )

    freq_T = np.zeros( i.size )
    for j in range(i.size):
        freq_T[ j ] = fmstart*2.0**( ( i[ j ] - 1 ) * B );
        pass

    # additional input data
    subs = 1;
    f_o = freq_T * 2.0**(B / 2.0)
    f_u = freq_T * 2.0**(-B / 2.0)
    Delta_F = np.zeros( len( freq_T ) );
    Delta_F = f_o - f_u

    # MATLAB: ModDichteOben = ModaleDichte( para, f_o );
    # MATLAB: ModDichteUnten = ModaleDichte( para, f_u );


    # Prepare the data
    Result = wave_speeds( ElasticModulusData,
                          ShearModulusData,
                          PoissonRatiosData,
                          MaterialPropertiesData,
                          GeometryPropertiesData,
                          Isotrop,
                          freq_T )


    ModDichteOben = ModaleDichte( Result[ "c_L" ],
                                  Result[ "c_S" ],
                                  Result[ "c_B_eff" ],
                                  Result[ "c_g_eff" ],
                                  GeometryPropertiesData,
                                  Isotrop,
                                  f_o )

    ModDichteUnten = ModaleDichte( Result[ "c_L" ],
                                   Result[ "c_S" ],
                                   Result[ "c_B_eff" ],
                                   Result[ "c_g_eff" ],
                                   GeometryPropertiesData,
                                   Isotrop,
                                   f_u )



    bending = [ 0.0 ] * i.size
    compressional = [ 0.0 ] * i.size
    shear = [ 0.0 ] * i.size
    sum = [ 0.0 ] * i.size
    for j in range(i.size):

        bending[ j ] = 0.5 * ( ModDichteOben[ "bending" ][ j ]
                               + ModDichteUnten[ "bending" ][ j ] ) \
                           * Delta_F[ j ] * 2.0 * np.pi

        compressional[ j ] = 0.5 * ( ModDichteOben[ "compressional" ][ j ]
                                     + ModDichteUnten[ "compressional" ][ j ] ) \
                                 * Delta_F[ j ] * 2.0 * np.pi

        shear[ j ] = 0.5 * ( ModDichteOben[ "shear" ][ j ]
                             + ModDichteUnten[ "shear" ][ j ] ) \
                         * Delta_F[ j ] * 2.0 * np.pi

        sum[ j ] = bending[ j ] + compressional[ j ] + shear[ j ]

    return { "bending" : bending,
             "compressional" : compressional,
             "shear" : shear,
             "sum" : sum,
             "freq_T" : freq_T }


def EigenfrequenciesPlate( ElasticModulusData,
                           ShearModulusData,
                           PoissonRatiosData,
                           MaterialPropertiesData,
                           GeometryPropertiesData,
                           Isotrop,
                           freq ):


    # Input Variables
    thickness = GeometryPropertiesData[ 0 ][ 2 ]
    length = GeometryPropertiesData[ 0 ][ 0 ]
    width = GeometryPropertiesData[ 0 ][ 1 ]
    Density = MaterialPropertiesData[ 0 ][ 0 ]

    #if Isotrop == True:
    if Isotrop == True:

        E = ElasticModulusData[ 0 ][ 0 ]
        nu = PoissonRatiosData[ 0 ][ 0 ]

        # Calculcations
        D = E * thickness**3 / (12.0 * (1.0 - nu*nu))
        mu = Density * thickness;

        # MATLAB: omega = @( m, n ) sqrt( D / mu ) * ((m * pi / length) ^ 2 + (n * pi / width) ^ 2);
        omega = lambda m,n: np.sqrt( D / mu ) * ((m * np.pi / length)**2 + (n * np.pi / width)**2)

        # Output
        Result = { "f11" : omega( 1.0, 1.0 )/(2.0 * np.pi), \
                   "f12" : omega( 1.0, 2.0 )/(2.0 * np.pi), \
                   "f21" : omega( 2.0, 1.0 )/(2.0 * np.pi), \
                   "f22" : omega( 2.0, 2.0 )/(2.0 * np.pi) }


    if Isotrop == False:

        # Input Variables
        # x - 0; y - 1; z - 2

        E_x = ElasticModulusData[ 0 ][ 0 ]
        E_y = ElasticModulusData[ 0 ][ 1 ]

        G_xy = ShearModulusData[ 0 ][ 0 ] # sqrt( 488.9E+09 * 3.211E+08 );

        nu_x = PoissonRatiosData[ 0 ][ 0 ] # nu_xy
        nu_y = PoissonRatiosData[ 1 ][ 0 ] # nu_yx

        D_x = E_x * thickness**2 / (12.0 * (1.0 - nu_x*nu_y))
        D_y = E_y * thickness**2 / (12.0 * (1.0 - nu_x * nu_y))
        D_k = G_xy * thickness**2 / 12.0
        D_xy = D_x * nu_y + 2.0 * D_k


        # MATLAB: omega = @(m,n) pi^2/(length^2*sqrt(Density)) *
        # sqrt(D_x*m^4+2*D_xy*m^2*n^2*(length/width)^2+D_y*n^4*(length/width)^4);

        CoeffOne = ( np.pi**2 ) / ( ( length**2 ) * np.sqrt( Density ) )
        CoeffTwo = 2.0 * D_xy * ( length / width )**2
        CoeffThree = D_y * ( length / width )**4

        omega = lambda m, n: CoeffOne * np.sqrt( D_x*m**4 + CoeffTwo * m**2 * n**2 + CoeffThree * n**4 )

        #Result = [ omega( 1.0, 1.0 )/(2.0 * np.pi), \
        #           omega( 1.0, 2.0 )/(2.0 * np.pi), \
        #           omega( 2.0, 1.0 )/(2.0 * np.pi), \
        #           omega( 2.0, 2.0 )/(2.0 * np.pi) ]

        Result = { "f11" : omega( 1.0, 1.0 )/(2.0 * np.pi), \
                   "f12" : omega( 1.0, 2.0 )/(2.0 * np.pi), \
                   "f21" : omega( 2.0, 1.0 )/(2.0 * np.pi), \
                   "f22" : omega( 2.0, 2.0 )/(2.0 * np.pi) }


    return Result


def ModalOverlapFactor( MaterialPropertiesData,
                        ModalDensities,
                        Frequency ):

    BendingDensity = ModalDensities[ "bending" ]
    CompressionalDensity = ModalDensities[ "compressional" ]
    ShearDensity = ModalDensities[ "shear" ]
    LossFactor = MaterialPropertiesData[ 0 ][ 1 ]

    Coeff = 2.0 * np.pi * LossFactor
    Mhp_Bending = [ Coeff * f * d for f, d in zip( Frequency, BendingDensity ) ]
    Mhp_Shear = [ Coeff * f * d for f, d in zip( Frequency, ShearDensity ) ]
    Mhp_QuasiLongitudinal = [ Coeff * f * d for f, d in zip( Frequency, CompressionalDensity ) ]

    return { "Bending" : Mhp_Bending,
             "Shear" : Mhp_Shear,
             "QuasiLongitudinal" : Mhp_QuasiLongitudinal }


def MaximumElementSize( C_B_Array, C_B_eff_Array, Frequency ):

    LamdaH = [ C_B / f for C_B, f in zip( C_B_Array, Frequency ) ]
    LamdaH_Effective = [ C_B_eff / f for C_B_eff, f in zip( C_B_eff_Array, Frequency ) ]
    ElementSize = [ 0.25 * Entry for Entry in LamdaH_Effective ]

    return { "Lamda" : LamdaH,
             "Lamda_Eff" : LamdaH_Effective,
             "ElementSize" : ElementSize }


