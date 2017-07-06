def cleanPlots( GraphData ):
    # the function assigns all entries within Graph data set to empty lists

    for i in range( len( GraphData ) ):
        GraphData[ i ].data = dict( XData = [ 0 ], YData = [ 0 ] )




def plotWaveSpeedGraph( Graph,
                        GraphData,
                        Functions,
                        Argiment,
                        isMaterialIsotropic ):

    # adjust plot settings
    Graph.y_mapper_type = 'log'
    Graph.x_mapper_type = 'log'

    # Find the maximum values in both x and y direction to be able to
    # depict both vertical and horizontal lines
    MaxCoordinateY = max( Functions[ 3 ] )
    MaxCoordinateX = max( Argiment )

    # GRAPHS DESCRIPTION:
    # NUMBER 0 - c_B                    **
    # NUMBER 1 - c_B_eff                **
    # NUMBER 2 - c_B_shear              **
    # NUMBER 3 - c_g                    **
    # NUMBER 4 - c_g_eff                **
    # NUMBER 5 - c_S                    **
    # NUMBER 6 - c_S_outofplane
    # NUMBER 7 - c_S_outofplane_1
    # NUMBER 8 - c_S_outofplane_2
    # NUMBER 9 - c_L                    **
    # NUMBER 10 - c_L_thick
    # NUMBER 11 - f_thickmode_shear
    # NUMBER 12 - f_thickmode_shear_x
    # NUMBER 13 - f_thickmode_shear_y


    # ............................ c_B graph ...................................
    GraphData[ 0 ].data = dict( XData = Argiment,
                                YData = Functions[ 0 ] )


    # .......................... c_B_eff graph .................................
    GraphData[ 4 ].data = dict( XData = Argiment,
                                YData = Functions[ 1 ] )


    # ............................ c_g graph ...................................
    GraphData[ 8 ].data = dict( XData = Argiment,
                                YData = Functions[ 3 ] )


    # .......................... c_g_eff graph .................................
    GraphData[ 12 ].data = dict( XData = Argiment,
                                YData = Functions[ 4 ] )

    # To get better understanding what c_L, c_S_outofplane_1 means
    # please ask to Christoph or try to read wave_speed file
    # in the current implementation c_L it's just a value that represent
    # a horisontal line


    # ............................ c_L graph ...................................
    RangeX = [ 0, MaxCoordinateX ]
    RangeY = [ Functions[ 9 ], Functions[ 9 ] ]
    print " C_L ", RangeY

    GraphData[ 3 ].data = dict( XData = RangeX,
                                YData = RangeY )


    # ........................ c_L_thick graph .................................
    #TODO: c_L_thick is equal to zero within entire range.
    #GraphData[ 15 ].data = dict( XData = Argiment,
    #                            YData = Functions[ 0 ][ 10 ] )


    # ......................... c_B_shear graph ................................
    RangeX = [ 0, MaxCoordinateX ]
    RangeY = [ Functions[ 2 ], Functions[ 2 ] ]

    GraphData[ 11 ].data = dict( XData = RangeX,
                                 YData = RangeY )


    # ............................ c_S graph ...................................
    RangeX = [ 0, MaxCoordinateX ]
    RangeY = [ Functions[ 5 ], Functions[ 5 ] ]

    GraphData[ 7 ].data = dict( XData = RangeX,
                                YData = RangeY )


    # ...................... c_S_outofplane graph ..............................
    # TODO: c_S_outofplane is equal to zero within entire range.
    #GraphData[ 12 ].data = dict( XData = Argiment,
    #                            YData = Functions[ 0 ][ 6 ] )


    # .................... f_thickmode_shear graph .............................
    RangeX = [ Functions[ 11 ], Functions[ 11 ] ]
    RangeY = [ 0, MaxCoordinateY ]

    GraphData[ 19 ].data = dict( XData = RangeX,
                                 YData = RangeY )


    # ................... f_thickmode_shear_x graph ............................
    RangeX = [ Functions[ 12 ], Functions[ 12 ] ]
    RangeY = [ 0, MaxCoordinateY ]

    GraphData[ 15 ].data = dict( XData = RangeX,
                                 YData = RangeY )

    # print out the debugged data
    print "f_thickmode_shear: ", Functions[ 11 ]
    print "f_thickmode_shear_x: ", Functions[ 12 ]
    print "f_thickmode_shear_y: ", Functions[ 13 ]

    # TODO: c_S_outofplane is equal to zero. Ask Peer about that
    # TODO: c_S_outofplane_1 is equal to zero. Ask Peer about that
    # TODO: c_S_outofplane_2 is equal to zero. Ask Peer about that
    pass
