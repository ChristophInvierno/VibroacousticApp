import math
import numpy as np
import matplotlib.pyplot as plt


def wave_speeds( ElasticModulusData,
                 ShearModulusData,
                 PoissonRatiosData,
                 MaterialPropertiesData,
                 GeometryPropertiesData,
                 Isotrop,
                 Function,
                 freq ):
    # Isotrop is a boolean



    # Wellengeschwindigkeiten

    Subs = len( ElasticModulusData )

    # Omega Vektor
    omeg = np.array( 2 * math.pi * freq )

    # Schubkorrekturfaktor
    kappa = 5.0 / 6

    # allocate numpy arrays
    l = np.zeros( Subs )
    b = np.zeros( Subs )
    d = np.zeros( Subs )
    rho = np.zeros( Subs )
    E1 = np.zeros( Subs )
    E2 = np.zeros( Subs )
    E3 = np.zeros( Subs )

    nu21 = np.zeros( Subs )
    nu13 = np.zeros( Subs )
    nu23 = np.zeros( Subs )

    nu12 = np.zeros( Subs )
    nu31 = np.zeros( Subs )
    nu32 = np.zeros( Subs )

    G12 = np.zeros( Subs )
    G13 = np.zeros( Subs )
    G23 = np.zeros( Subs )
    D_int = np.zeros( Subs )

    # Initialize parameters that have to be return from the function
    c_B = np.zeros( (Subs, freq.size) )
    c_B_eff = np.zeros( (Subs, freq.size) )
    c_B_shear = np.zeros( (Subs, freq.size) )
    c_g = np.zeros( (Subs, freq.size) )
    c_g_eff = np.zeros( (Subs, freq.size) )
    c_g_eff = np.zeros( (Subs, freq.size) )
    c_S = np.zeros( (Subs, freq.size) )
    c_S_outofplane = np.zeros( (Subs, freq.size) )
    c_S_outofplane_1 = np.zeros( (Subs, freq.size) )
    c_S_outofplane_2 = np.zeros( (Subs, freq.size) )
    c_L = np.zeros( (Subs, freq.size) )
    c_L_thick = np.zeros( (Subs, freq.size) )

    f_thickmode_long = np.zeros( Subs )
    f_thickmode_shear = np.zeros( Subs )
    f_thickmode_shear_x = np.zeros( Subs )
    f_thickmode_shear_y = np.zeros( Subs )

    for i in range( Subs ):
        l[ i ] = np.array( GeometryPropertiesData[ i ][ 0 ] )
        b[ i ] = np.array( GeometryPropertiesData[ i ][ 1 ] )
        d[ i ] = np.array( GeometryPropertiesData[ i ][ 2 ] )
        E1[ i ] = np.array( ElasticModulusData[ i ][ 0 ] )
        E2[ i ] = np.array( ElasticModulusData[ i ][ 1 ] )
        E3[ i ] = np.array( ElasticModulusData[ i ][ 2 ] )

        nu12[ i ] = PoissonRatiosData[ 0 ][ 0 ]
        nu13[ i ] = PoissonRatiosData[ 0 ][ 1 ]
        nu23[ i ] = PoissonRatiosData[ 0 ][ 2 ]

        nu21[ i ] = PoissonRatiosData[ 1 ][ 0 ]
        nu31[ i ] = PoissonRatiosData[ 1 ][ 1 ]
        nu32[ i ] = PoissonRatiosData[ 1 ][ 2 ]

        G12[ i ] = np.array( ShearModulusData[ i ][ 0 ] )
        G13[ i ] = np.array( ShearModulusData[ i ][ 1 ] )
        G23[ i ] = np.array( ShearModulusData[ i ][ 2 ] )
        rho[ i ] = np.array( MaterialPropertiesData[ i ][ 0 ] )
        D_int[ i ] = np.array( MaterialPropertiesData[ i ][ 1 ] )

    ## Berechnung der Wellengeschwindigkeiten
    # debugging


    if Isotrop == True:  # ISO
        # allocate numpy arrays
        c_B = np.zeros( (Subs, freq.size) )
        c_L = np.zeros( (Subs, freq.size) )
        c_S = np.zeros( (Subs, freq.size) )
        c_g = np.zeros( (Subs, freq.size) )
        c_B_shear = np.zeros( (Subs, freq.size) )
        c_B_eff = np.zeros( (Subs, freq.size) )
        c_g_eff = np.zeros( (Subs, freq.size) )
        c_B_eff_1 = np.zeros( (Subs, freq.size) )
        c_B_eff_2 = np.zeros( (Subs, freq.size) )

        fR_B = np.zeros( Subs )
        fR_g = np.zeros( Subs )

        G = np.zeros( Subs )
        B = np.zeros( Subs )
        S = np.zeros( Subs )
        U = np.zeros( Subs )

        f_thickmode_long = np.zeros( Subs )
        f_thickmode_shear = np.zeros( Subs )
        f_thickmode_shear_x = np.zeros( Subs )
        f_thickmode_shear_y = np.zeros( Subs )

        for i in range( Subs ):
            G[ i ] = E1[ i ] / (
                2 * (1 + nu21[ i ]))  # Schubmodul aus isotropem Materialgesetz
            B[ i ] = E1[ i ] * d[ i ] ** 3 / (
                12 * (1 - nu21[ i ] ** 2))  # Biegesteifigkeit

            c_B_shear[ i, : ] = np.sqrt( G[ i ] * kappa / rho[ i ] )  # |

            # S[i]=l[i]*b[i]              # Flaeche der Platte
            # U[i] = 2*l[i]+2*b[i]       #Umfang der Platte
            # |
            c_L[ i, : ] = np.sqrt(
                E1[ i ] / (rho[ i ] * (1 - nu21[ i ] ** 2)) )  # |
            # |
            # |
            c_S[ i, : ] = np.sqrt( G[ i ] / rho[ i ] )  # |
            # |

            # --Anspassung der Biegemoden an dicke Platte v.a. nach Meier 2000--
            # tw,01.02.17

            # rayleighwellengeschwindigkeit nach Moeser et al 2010
            c_B_shear[ i, : ] = 1 * c_B_shear[ i,
                                    : ]  # Abschaetzung Rayleighgeschwindigkeit

            fR_B[ i ] = c_B_shear[ i, 0 ] ** 2 / (2 * math.pi) * np.sqrt(
                (rho[ i ] * d[ i ]) / B[ i ] )  # Grenzfrequenz nach Meier 2000
            fR_g[ i ] = fR_B[ i ] / 4

            c_B[ i, : ] = ((omeg ** 2 * B[ i ]) / (rho[ i ] * d[ i ])) ** (
                1.0 / 4)  # gesamte formel zB Craik
            c_g[ i, : ] = 2 * c_B[ i, : ]
            c_B_eff[ i, : ] = c_B_shear[ i, : ] * freq / fR_B[ i ] * np.sqrt(
                -0.5 + 0.5 * np.sqrt( 1 + (2 * fR_B[
                    i ] / freq) ** 2 ) )  # korrigierte Biegewellengeschwindigkeit dicke Platte
            c_g_eff[ i, : ] = c_B_eff[ i, : ] ** 3 / c_B_shear[ i,
                                                     : ] ** 2 * np.sqrt(
                1 + (2 * fR_B[
                    i ] / freq) ** 2 )  # korrigierte Biegegruppenwellengeschwindigkeit

            f_thickmode_long[ i ] = c_L[ i, 0 ] / (2 * d[ i ])
            f_thickmode_shear[ i ] = c_S[ i, 0 ] / (2 * d[ i ])
            f_thickmode_shear_x[ i ] = f_thickmode_shear[ i ]
            f_thickmode_shear_y[ i ] = f_thickmode_shear[ i ]
            c_B_eff_1[ i, : ] = c_B_eff[ i, : ]
            c_B_eff_2[ i, : ] = c_B_eff[ i, : ]


    elif Isotrop == False:

        # allocate numpy arrays
        c_B = np.zeros( (Subs, freq.size) )
        c_g = np.zeros( (Subs, freq.size) )
        c_L = np.zeros( (Subs, freq.size) )
        c_L_thick = np.zeros( (Subs, freq.size) )

        c_S = np.zeros( (Subs, freq.size) )
        c_S_outofplane = np.zeros( (Subs, freq.size) )
        c_S_outofplane_1 = np.zeros( (Subs, freq.size) )
        c_S_outofplane_2 = np.zeros( (Subs, freq.size) )
        # c_S = np.zeros((Subs, freq.size))
        # c_S_outofplane_1 = np.zeros((Subs, freq.size))
        # c_S_outofplane_2 = np.zeros((Subs, freq.size))

        # c_B_shear = np.zeros((Subs, freq.size))
        c_B_shear = np.zeros( (Subs, freq.size) )
        c_B_shear_1 = np.zeros( (Subs, freq.size) )
        c_B_shear_2 = np.zeros( (Subs, freq.size) )

        c_B_eff = np.zeros( (Subs, freq.size) )
        c_g_eff = np.zeros( (Subs, freq.size) )
        c_B_eff_1 = np.zeros( (Subs, freq.size) )
        c_g_eff_1 = np.zeros( (Subs, freq.size) )
        c_B_eff_2 = np.zeros( (Subs, freq.size) )
        c_g_eff_2 = np.zeros( (Subs, freq.size) )

        '''nu12 = np.zeros(Subs)
        nu31 = np.zeros(Subs)
        nu32 = np.zeros(Subs)
        '''

        D_nu = np.zeros( Subs )
        S = np.zeros( Subs )
        U = np.zeros( Subs )
        c_L_1 = np.zeros( Subs )
        c_L_2 = np.zeros( Subs )
        B1 = np.zeros( Subs )
        B2 = np.zeros( Subs )
        B = np.zeros( Subs )

        fR_B = np.zeros( Subs )
        fR_g = np.zeros( Subs )
        fR_B_1 = np.zeros( Subs )
        fR_g_1 = np.zeros( Subs )
        fR_B_2 = np.zeros( Subs )
        fR_g_2 = np.zeros( Subs )

        c_B_1 = np.zeros( (Subs, freq.size) )
        c_g_1 = np.zeros( (Subs, freq.size) )
        c_B_2 = np.zeros( (Subs, freq.size) )
        c_g_2 = np.zeros( (Subs, freq.size) )

        f_thickmode_long = np.zeros( Subs )
        f_thickmode_shear = np.zeros( Subs )
        f_thickmode_shear_x = np.zeros( Subs )
        f_thickmode_shear_y = np.zeros( Subs )

        G = np.zeros( Subs )

        # Orthotrope Berechnung

        for i in range( Subs ):
            '''
            nu12[i]=E1[i]/E2[i]*nu21[i]    # Aus orthotropem Materialgesetz
            nu31[i]=E1[i]/E3[i]*nu13[i]
            nu32[i]=E2[i]/E3[i]*nu23[i]
            '''

            # Determinante der Nachgiebigkeitsmatrix nach Wikipedia Orthotropie
            D_nu[ i ] = 1 - nu12[ i ] * nu21[ i ] - nu13[ i ] * nu31[ i ] - \
                        nu23[ i ] * \
                        nu32[ i ] - 2 * \
                                    nu12[
                                        i ] * \
                                    nu23[
                                        i ] * \
                                    nu31[
                                        i ]

            # Biegesteifigkeit,Anpassung Emodul um Querdehnungsbehinderung zu beruecksichtigen
            B1[ i ] = E1[ i ] * d[ i ] ** 3 / (12 * (1 - nu12[ i ] * nu21[ i ]))
            B2[ i ] = E2[ i ] * d[ i ] ** 3 / (12 * (1 - nu12[ i ] * nu21[ i ]))
            B[ i ] = np.sqrt( B1[ i ] * B2[ i ] )

            # S[i]=l[i]*b[i]              # Flaeche der Platte
            # U[i] = 2*l[i]+2*b[i]        #Umfang der Platte

            # |cw,18.12.16, Anpassung Emodul um Querdehnungsbehinderung zu beruecksichtigen

            c_L_1[ i ] = np.sqrt(
                E1[ i ] / (rho[ i ] * (1 - nu12[ i ] * nu21[ i ])) )
            c_L_2[ i ] = np.sqrt(
                E2[ i ] / (rho[ i ] * (1 - nu12[ i ] * nu21[ i ])) )
            c_L[ i, : ] = np.sqrt( c_L_1[ i ] * c_L_2[ i ] )

            c_L_thick[ i, : ] = np.sqrt(
                E3[ i ] / rho[ i ] * (1 - nu12[ i ] * nu21[ i ]) / D_nu[ i ] )

            c_B_shear_1[ i, : ] = np.sqrt( G13[ i ] * kappa / rho[ i ] )
            c_B_shear_2[ i, : ] = np.sqrt( G23[ i ] * kappa / rho[ i ] )
            c_B_shear[ i, : ] = np.sqrt(
                c_B_shear_1[ i, 0 ] * c_B_shear_2[ i, 0 ] )

            c_S_outofplane_1[ i, : ] = np.sqrt( G13[ i ] / (rho[ i ]) )
            c_S_outofplane_2[ i, : ] = np.sqrt( G23[ i ] / (rho[ i ]) )
            c_S_outofplane[ i, : ] = np.sqrt(
                c_S_outofplane_1[ i, 0 ] * c_S_outofplane_2[ i, 0 ] )
            # | cw,18.12.16 2*G12 anstatt G12 fuer thick plate theory acc. to stiffness matrix

            c_S[ i, : ] = np.sqrt( 2 * G12[ i ] / rho[ i ] )
            # --Anspassung der Biegemoden an dicke Platte v.a. nach Meier 2000--
            # tw,01.02.17

            # Grenzfrequenz nach Meier 2000
            fR_B[ i ] = c_B_shear[ i, 0 ] ** 2 / (2 * math.pi) * np.sqrt(
                (rho[ i ] * d[ i ]) / B[ i ] )
            fR_g[ i ] = fR_B[ i ] / 4

            # Grenzfrequenz nach Meier 2000
            fR_B_1[ i ] = c_B_shear_1[ i, 0 ] ** 2 / (2 * math.pi) * np.sqrt(
                (rho[ i ] * d[ i ]) / B1[ i ] )
            fR_g_1[ i ] = fR_B_1[ i ] / 4

            fR_B_2[ i ] = c_B_shear_2[ i, 0 ] ** 2 / (2 * math.pi) * np.sqrt(
                (rho[ i ] * d[ i ]) / B2[ i ] )  # Grenzfrequenz nach Meier 2000
            fR_g_2[ i ] = fR_B_2[ i ] / 4

            # gesamte formel zB Craik
            c_B[ i, : ] = ((omeg ** 2 * B[ i ]) / (rho[ i ] * d[ i ])) ** (
            1.0 / 4)
            c_g[ i, : ] = 2 * c_B[ i, : ]
            c_B_eff[ i, : ] = c_B_shear[ i, : ] * freq / fR_B[ i ] * np.sqrt(
                -0.5 + 0.5 * np.sqrt( 1 + (2 * fR_B[
                    i ] / freq) ** 2 ) )  # korrigierte Biegewellengeschwindigkeit dicke Platte
            c_g_eff[ i, : ] = c_B_eff[ i, : ] ** 3 / c_B_shear[ i,
                                                     : ] ** 2 * np.sqrt(
                1 + (2 * fR_B[
                    i ] / freq) ** 2 )  # korrigierte Biegegruppenwellengeschwindigkeit

            c_B_1[ i, : ] = ((omeg ** 2 * B1[ i ]) / (rho[ i ] * d[ i ])) ** (
                1.0 / 4)  # gesamte formel zB Craik
            c_g_1[ i, : ] = 2 * c_B_1[ i, : ]
            c_B_eff_1[ i, : ] = c_B_shear_1[ i ] * freq / fR_B_1[ i ] * np.sqrt(
                -0.5 + 0.5 * np.sqrt( 1 + (2 * fR_B_1[
                    i ] / freq) ** 2 ) )  # korrigierte Biegewellengeschwindigkeit dicke Platte
            c_g_eff_1[ i, : ] = c_B_eff_1[ i, : ] ** 3 / c_B_shear_1[
                                                             i ] ** 2 * np.sqrt(
                1 + (
                    2 * fR_B_1[
                        i ] / freq) ** 2 )  # korrigierte Biegegruppenwellengeschwindigkeit

            c_B_2[ i, : ] = ((omeg ** 2 * B2[ i ]) / (rho[ i ] * d[ i ])) ** (
                1.0 / 4)  # gesamte formel zB Craik
            c_g_2[ i, : ] = 2 * c_B_2[ i, : ]
            c_B_eff_2[ i, : ] = c_B_shear_2[ i ] * freq / fR_B_2[ i ] * np.sqrt(
                -0.5 + 0.5 * np.sqrt( 1 + (2 * fR_B_2[
                    i ] / freq) ** 2 ) )  # korrigierte Biegewellengeschwindigkeit dicke Platte
            c_g_eff_2[ i, : ] = c_B_eff_2[ i, : ] ** 3 / c_B_shear_2[
                                                             i ] ** 2 * np.sqrt(
                1 + (
                    2 * fR_B_2[
                        i ] / freq) ** 2 )  # korrigierte Biegegruppenwellengeschwindigkeit

            f_thickmode_long[ i ] = c_L_thick[ i, 0 ] / (2 * d[ i ])
            f_thickmode_shear[ i ] = c_S_outofplane[ i, 0 ] / (2 * d[ i ])
            f_thickmode_shear_x[ i ] = c_S_outofplane_1[ i, 0 ] / (2 * d[ i ])
            f_thickmode_shear_y[ i ] = c_S_outofplane_2[ i, 0 ] / (2 * d[ i ])




    # Prepare data that have to be returned from the function
    Result = [ c_B.tolist( )[ 0 ],
               c_B_eff.tolist( )[ 0 ],
               c_B_shear.tolist( )[ 0 ][ 0 ],
               c_g.tolist( )[ 0 ],
               c_g_eff.tolist( )[ 0 ],
               c_S.tolist( )[ 0 ][ 0 ],
               c_S_outofplane.tolist( )[ 0 ],
               c_S_outofplane_1.tolist( )[ 0 ][ 0 ],
               c_S_outofplane_2.tolist( )[ 0 ],
               c_L.tolist( )[ 0 ][ 0 ],
               c_L_thick.tolist( )[ 0 ],
               f_thickmode_shear.tolist( )[ 0 ],
               f_thickmode_shear_x.tolist( )[ 0 ],
               f_thickmode_shear_y.tolist( )[ 0 ] ]


    return Result
