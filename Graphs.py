import matplotlib.pyplot as plt

def plotWaveSpeedGraph( GraphInstance ):
    #print GraphInstance.Functions[ 0 ][ 0 ]

    # adjust plot settings
    #GraphInstance.Graph.y_mapper_type = 'log'

    # Find the maximum values in both x and y direction to be able to
    # depict both vertical and horizontal lines
    MaxCoordinateY = max( GraphInstance.Functions[ 0 ][ 3 ] )
    MaxCoordinateX = max( GraphInstance.getRange( ) )

    # GRAPHS DESCRIPTION:
    # NUMBER 0 - c_B                    ** black solid line, line code 0
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


    # LINE DESCRIPTION
    # line number: 0 - black solid
    # line number: 1 - black dashed
    # line number: 2 - black dot-dashed
    # line number: 3 - black dash-dot
    # line number: 4 - blue solid
    # line number: 5 - blue dashed
    # line number: 6 - blue dot-dashed
    # line number: 7 - blue dash-dot
    # line number: 8 - green solid
    # line number: 10 - green dashed
    # line number: 11 - green dot-dashed
    # line number: 12 - green dash-dot
    # line number: 13 - red solid
    # line number: 14 - red dashed
    # line number: 15 - red dot-dashed
    # line number: 16 - red dash-dot
    # line number: 17 - orange solid
    # line number: 18 - orange dashed
    # line number: 19 - orange dot-dashed
    # line number: 20 - orange dash-dot
    # line number: 21 - pink solid
    # line number: 22 - pink dashed
    # line number: 23 - pink dot-dashed
    # line number: 24 - pink dash-dot


    GraphInstance.LabelText.text = """ TEXT LEGEND:
                                       <br/>
                                       black solid line - c_B <br/>
                                       blue solid line - c_B_eff <br/>
                                       green solid line - c_g <br/>
                                       green dash-dot line - c_g_eff <br/>
                                       black dash-dot line - c_L <br/>
                                       green dot-dashed line - c_B_shear <br/>
                                       blue dash-dot line - c_S <br/>
                                       orange dot-dashed line - f_thickmode_shear <br/>
                                       red dot-dashed line - f_thickmode_shear_x <br/>
                                       pink dashed line - f_thickmode_shear_y <br/>
                                   """


    # ............................ c_B graph ...................................
    GraphInstance.GraphData[ 0 ].data = dict( XData = GraphInstance.getRange(),
                                              YData = GraphInstance.Functions[ 0 ][ 0 ] )


    # .......................... c_B_eff graph .................................
    GraphInstance.GraphData[ 4 ].data = dict( XData = GraphInstance.getRange(),
                                            YData = GraphInstance.Functions[ 0 ][ 1 ] )


    # ............................ c_g graph ...................................
    GraphInstance.GraphData[ 8 ].data = dict( XData = GraphInstance.getRange(),
                                            YData = GraphInstance.Functions[ 0 ][ 3 ] )


    # .......................... c_g_eff graph .................................
    GraphInstance.GraphData[ 12 ].data = dict( XData = GraphInstance.getRange(),
                                             YData = GraphInstance.Functions[ 0 ][ 4 ] )

    # To get better understanding what c_L, c_S_outofplane_1 means
    # please ask to Christoph or try to read wave_speed file
    # in the current implementation c_L it's just a value that represent
    # a horisontal line


    # ............................ c_L graph ...................................
    RangeX = [ 0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 9 ],
               GraphInstance.Functions[ 0 ][ 9 ] ]
    print " C_L ", RangeY

    GraphInstance.GraphData[ 3 ].data = dict( XData = RangeX,
                                              YData = RangeY )


    # ........................ c_L_thick graph .................................
    #TODO: c_L_thick is equal to zero within entire range.
    #GraphData[ 15 ].data = dict( XData = Argiment,
    #                            YData = Functions[ 0 ][ 10 ] )


    # ......................... c_B_shear graph ................................
    RangeX = [ 0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 2 ],
               GraphInstance.Functions[ 0 ][ 2 ] ]

    GraphInstance.GraphData[ 11 ].data = dict( XData = RangeX,
                                               YData = RangeY )


    # ............................ c_S graph ...................................
    RangeX = [ 0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 5 ],
               GraphInstance.Functions[ 0 ][ 5 ] ]

    GraphInstance.GraphData[ 7 ].data = dict( XData = RangeX,
                                              YData = RangeY )


    # ...................... c_S_outofplane graph ..............................
    # TODO: c_S_outofplane is equal to zero within entire range.
    #GraphData[ 12 ].data = dict( XData = Argiment,
    #                            YData = Functions[ 0 ][ 6 ] )


    # .................... f_thickmode_shear graph .............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 11 ],
               GraphInstance.Functions[ 0 ][ 11 ] ]
    RangeY = [ 0, MaxCoordinateY ]

    GraphInstance.GraphData[ 19 ].data = dict( XData = RangeX,
                                               YData = RangeY )


    # ................... f_thickmode_shear_x graph ............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 12 ],
               GraphInstance.Functions[ 0 ][ 12 ] ]
    RangeY = [ 0, MaxCoordinateY ]

    GraphInstance.GraphData[ 15 ].data = dict( XData = RangeX,
                                               YData = RangeY )

    # ................... f_thickmode_shear_y graph ............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 13 ],
               GraphInstance.Functions[ 0 ][ 13 ] ]
    RangeY = [ 0, MaxCoordinateY ]

    GraphInstance.GraphData[ 22 ].data = dict( XData = RangeX,
                                               YData = RangeY )

    # print out the debugged data
    print "f_thickmode_shear: ", GraphInstance.Functions[ 0 ][ 11 ]
    print "f_thickmode_shear_x: ", GraphInstance.Functions[ 0 ][ 12 ]
    print "f_thickmode_shear_y: ", GraphInstance.Functions[ 0 ][ 13 ]

    # TODO: c_S_outofplane is equal to zero. Ask Peer about that
    # TODO: c_S_outofplane_1 is equal to zero. Ask Peer about that
    # TODO: c_S_outofplane_2 is equal to zero. Ask Peer about that

    #plt.plot(GraphInstance.getRange() , GraphInstance.Functions[ 0 ][ 0 ])
    plt.loglog( GraphInstance.getRange(), GraphInstance.Functions[ 0 ][ 0 ],
                GraphInstance.getRange( ), GraphInstance.Functions[ 0 ][ 1 ],
                GraphInstance.getRange( ), GraphInstance.Functions[ 0 ][ 3 ],
                GraphInstance.getRange( ), GraphInstance.Functions[ 0 ][ 4 ],
                basex = 2 )

    plt.savefig( 'FirstMode.png' )
    #plt.show()