import matplotlib.pyplot as plt
import random
from bokeh.io import reset_output
from bokeh.models import ColumnDataSource
from GraphClass import GraphObject

def plotWaveSpeedGraph( GraphInstance ):
    #print GraphInstance.Functions[ 0 ][ 0 ]

    # Find the maximum values in both x and y direction to be able to
    # depict both vertical and horizontal lines
    MaxCoordinateY = max( GraphInstance.Functions[ 0 ][ 3 ] )
    MaxCoordinateX = max( GraphInstance.getRange( ) )



    # To get better understanding what c_L, c_S_outofplane_1 means
    # please ask to Christoph or try to read wave_speed file
    # in the current implementation c_L it's just a value that represent
    # a horisontal line



    # ...................... c_S_outofplane graph ..............................
    # TODO: c_S_outofplane is equal to zero within entire range.
    #GraphData[ 12 ].data = dict( XData = Argiment,
    #                            YData = Functions[ 0 ][ 6 ] )



    # TODO: c_S_outofplane is equal to zero. Ask Peer about that
    # TODO: c_S_outofplane_1 is equal to zero. Ask Peer about that
    # TODO: c_S_outofplane_2 is equal to zero. Ask Peer about that


    plt.clf()

    DARK_BLUE = '#005293'
    LIGHT_BLUE = '#98C6EA'
    GREEN = '#A2AD00'
    ORANGE = '#E37222'
    GRAY = '#999999'
    MIDDEL_BLUE = '#64A0C8'

    # ............................ c_B graph ...................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 0 ][ 0 ],
                basex = 10, linestyle = '--', color = GREEN )


    # .......................... c_B_eff graph .................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 0 ][ 1 ],
                linestyle = '-.', linewidth = 3, color = GREEN )


    # ............................ c_g graph ...................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 0 ][ 3 ],
                linestyle = '--', color = ORANGE )


    # .......................... c_g_eff graph .................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 0 ][ 4 ],
                linestyle = '-.', linewidth = 3, color = ORANGE )


    # ............................ c_L graph ...................................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 9 ],
               GraphInstance.Functions[ 0 ][ 9 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '-', color = DARK_BLUE )


    # ......................... c_B_shear graph ................................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 2 ],
               GraphInstance.Functions[ 0 ][ 2 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = DARK_BLUE )


    # ............................ c_S graph ...................................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 5 ],
               GraphInstance.Functions[ 0 ][ 5 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '-', color = LIGHT_BLUE )


    # .................... f_thickmode_shear graph .............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 11 ],
               GraphInstance.Functions[ 0 ][ 11 ] ]
    RangeY = [ 1.0, MaxCoordinateY ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = LIGHT_BLUE )


    # ................... f_thickmode_shear_x graph ............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 12 ],
               GraphInstance.Functions[ 0 ][ 12 ] ]
    RangeY = [ 1.0, MaxCoordinateY ]

    plt.loglog( RangeX, RangeY, linestyle = '-.', linewidth = 3, color = DARK_BLUE )


    # ................... f_thickmode_shear_y graph ............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 13 ],
               GraphInstance.Functions[ 0 ][ 13 ] ]
    RangeY = [ 1.0, MaxCoordinateY ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = LIGHT_BLUE )


    plt.legend( ('Effective bending (thick plate)',
                 'Pure bending (thin plate)',
                 'Group (bending)',
                 'Group (effective bending)',
                 'Quasi-longitudial, in-plane',
                 'Longitudial, out-of-plane',
                 'Shear, in-plane',
                 '1st Thickness-shear resonance (G31)',
                 '1st Thickness-shear resonance',
                 '1st Thickness-shear resonance (G32)'),
                  loc = 'upper left',
                  fontsize = 10,
                  bbox_to_anchor = (1.0, 1.0))


    plt.ylabel( 'Wave velocity in m/s' )
    plt.xlabel( 'Frequency in Hz' )


    Counter = GraphInstance.getImageCounter()
    plt.savefig( './static/images/FirstMode%d.png' %Counter, bbox_inches='tight', pdi=300 )
    GraphInstance.updateTestGraph( "FirstMode", Counter )
    #plt.show()