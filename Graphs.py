import matplotlib.pyplot as plt
import numpy as np
import random
from Colors import *

from bokeh.io import reset_output
from bokeh.models import ColumnDataSource
from GraphClass import GraphObject


# grid layout

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


    plt.clf()

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
    RangeY = [ GraphInstance.Functions[ 0 ][ 9 ][ 0 ],
               GraphInstance.Functions[ 0 ][ 9 ][ 0 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '-', color = DARK_BLUE )


    # ......................... c_B_shear graph ................................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 2 ],
               GraphInstance.Functions[ 0 ][ 2 ] ]

    plt.loglog( RangeX, RangeY, linestyle = ':', color = LIGHT_BLUE )


    # ............................ c_S graph ...................................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 5 ],
               GraphInstance.Functions[ 0 ][ 5 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '-', color = LIGHT_BLUE )


    # ............................ c_L_thick graph .............................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 10 ],
               GraphInstance.Functions[ 0 ][ 10 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = DARK_BLUE )


    # ............................ c_S_outofplane_1 graph ......................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 7 ],
               GraphInstance.Functions[ 0 ][ 7 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = LIGHT_BLUE )

    # ............................ c_S_outofplane_2 graph ......................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 8 ],
               GraphInstance.Functions[ 0 ][ 8 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = LIGHT_BLUE )


    plt.legend( ('Effective bending (thick plate)',
                 'Pure bending (thin plate)',
                 'Group (bending)',
                 'Group (effective bending)',
                 'Quasi-longitudial, in-plane',
                 'Shear (corrected), out-of-plane displ.',
                 'Shear, in-plane',
                 'Longitudinal out-of-plane',
                 'Shear out-of-plane prop. (G32)',
                 'Shear out-of-plane prop. (G31)'),
                  loc = 'upper left',
                  fontsize = 10,
                  bbox_to_anchor = (1.0, 1.0))


    plt.ylabel( 'Wave velocity in m/s' )
    plt.xlabel( 'Frequency in Hz' )


    Counter = GraphInstance.getImageCounter()
    plt.savefig( './static/images/WaveSpeed%d.png' %Counter, bbox_inches='tight', pdi=300 )
        #GraphInstance.updateTestGraph( "WaveSpeed", Counter )


def plotWaveSpeedGraphWithLimits( GraphInstance ):
    #print GraphInstance.Functions[ 0 ][ 0 ]

    # Find the maximum values in both x and y direction to be able to
    # depict both vertical and horizontal lines
    MaxCoordinateY = max( GraphInstance.Functions[ 0 ][ 3 ] )
    MaxCoordinateX = max( GraphInstance.getRange( ) )



    # To get better understanding what c_L, c_S_outofplane_1 means
    # please ask to Christoph or try to read wave_speed file
    # in the current implementation c_L it's just a value that represent
    # a horisontal line


    plt.clf()

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
    RangeY = [ GraphInstance.Functions[ 0 ][ 9 ][ 0 ],
               GraphInstance.Functions[ 0 ][ 9 ][ 0 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '-', color = DARK_BLUE )


    # ......................... c_B_shear graph ................................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 2 ],
               GraphInstance.Functions[ 0 ][ 2 ] ]

    plt.loglog( RangeX, RangeY, linestyle = ':', color = LIGHT_BLUE )


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

    # ............................ c_L_thick graph .............................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 10 ],
               GraphInstance.Functions[ 0 ][ 10 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = DARK_BLUE )


    # ............................ c_S_outofplane_1 graph ......................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 7 ],
               GraphInstance.Functions[ 0 ][ 7 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = LIGHT_BLUE )

    # ............................ c_S_outofplane_2 graph ......................
    RangeX = [ 1.0, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 8 ],
               GraphInstance.Functions[ 0 ][ 8 ] ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = LIGHT_BLUE )


    # .................... fR_B graph .............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 14 ],
               GraphInstance.Functions[ 0 ][ 14 ] ]
    RangeY = [ 1.0, MaxCoordinateY ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = GREEN )

    # .................... fR_B graph .............................
    RangeX = [ GraphInstance.Functions[ 0 ][ 15 ],
               GraphInstance.Functions[ 0 ][ 15 ] ]
    RangeY = [ 1.0, MaxCoordinateY ]

    plt.loglog( RangeX, RangeY, linestyle = '--', color = ORANGE )



    plt.legend( ('Effective bending (thick plate)',
                 'Pure bending (thin plate)',
                 'Group (bending)',
                 'Group (effective bending)',
                 'Quasi-longitudial, in-plane',
                 'Shear (corrected), out-of-plane displ.',
                 'Shear, in-plane',
                 '1st Thickness-shear resonance (G31)',
                 '1st Thickness-stretch resonance',
                 '1st Thickness-shear resonance (G32)',
                 'Longitudinal out-of-plane',
                 'Shear out-of-plane prop. (G32)',
                 'Shear out-of-plane prop. (G31)',
                 'Thin-Plate-Limit Phase',
                 'Thin-Plate-Limit Group'),
                  loc = 'upper left',
                  fontsize = 10,
                  bbox_to_anchor = (1.0, 1.0))


    plt.ylabel( 'Wave velocity in m/s' )
    plt.xlabel( 'Frequency in Hz' )


    Counter = GraphInstance.getImageCounter()
    plt.savefig( './static/images/WaveSpeedWithLimits%d.png' %Counter, bbox_inches='tight', pdi=300 )
    #GraphInstance.updateTestGraph( "WaveSpeed", Counter )


def plotModesInBand( GraphInstance ):
    plt.clf( )

    # ............................ bending_np graph ...................................
    plt.loglog( GraphInstance.Functions[ 2 ][ 4 ], GraphInstance.Functions[ 2 ][ 0 ],
                basex = 10, linestyle = '-', marker='o', markevery = 2, color = GREEN )

    # ............................ compressional_np graph ...................................
    plt.loglog( GraphInstance.Functions[ 2 ][ 4 ], GraphInstance.Functions[ 2 ][ 2 ],
                basex = 10, linestyle = '-', marker='o', markevery = 2, color = LIGHT_BLUE )

    # ............................ shear_np graph ...................................
    plt.loglog( GraphInstance.Functions[ 2 ][ 4 ], GraphInstance.Functions[ 2 ][ 1 ],
                basex = 10, linestyle = '-', marker='o', markevery = 2, color = DARK_BLUE )


    plt.ylabel( 'Number of modes per one-third octave band' )
    plt.xlabel( 'Frequency in Hz' )

    plt.legend( ('Effective bending (thick plate)',
                 'Shear, in-plane',
                 'Quasi-longitudial, in plane'),
                loc = 'upper left',
                fontsize = 10,
                bbox_to_anchor = (1.0, 1.0) )

    Counter = GraphInstance.getImageCounter( )
    plt.savefig( './static/images/ModesInBand%d.png' % Counter,
                 bbox_inches = 'tight', pdi = 300 )

    #GraphInstance.updateTestGraph( "ModesInBand", Counter )


def plotModalDensity( GraphInstance ):
    #MaxCoordinateY = max( GraphInstance.Functions[ 3 ][ 3 ] )
    #MaxCoordinateX = max( GraphInstance.getRange( ) )


    plt.clf()


    # ............................ bending_np graph ...................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 3 ][ 0 ],
                basex = 10, linestyle = '-',  color = DARK_BLUE )

    # ............................ shear graph ...................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 3 ][ 2 ],
                basex = 10, linestyle = '-', color = LIGHT_BLUE )

    # ............................ compressional_np graph ...................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 3 ][ 1 ],
                basex = 10, linestyle = '-', color = GREEN )


    plt.ylabel( 'Modal Density in s/rad' )
    plt.xlabel( 'Frequency in Hz' )

    plt.legend( ('Quasi-longitudinal, in-plane',
                 'Shear, in-plane',
                 'Effective bending (thick plate)'),
                  loc = 'upper left',
                  fontsize = 10,
                  bbox_to_anchor = (1.0, 1.0))

    Counter = GraphInstance.getImageCounter( )
    plt.savefig( './static/images/ModalDensity%d.png' % Counter,
                 bbox_inches = 'tight', pdi = 300 )

    #GraphInstance.updateTestGraph( "ModalDensity", Counter )



def plotModalOverlapFactor( GraphInstance ):
    plt.clf( )

    # ...................... Mhp_QuasiLongitudinal graph .......................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 4 ][ 0 ],
                basex = 10, linestyle = '-', color = DARK_BLUE )

    # ......................... Mhp_Shear graph ................................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 4 ][ 1 ],
                basex = 10, linestyle = '-', color = LIGHT_BLUE )

    # ........................ Mhp_Effective graph ..............................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 4 ][ 2 ],
                basex = 10, linestyle = '-', color = GREEN )


    plt.ylabel( 'Half Power Bandwith Modal Overlap Factor' )
    plt.xlabel( 'Frequency in Hz' )

    plt.legend( ('Quasi-longitudinal, in-plane',
                 'Shear, in-plane',
                 'Effective bending (thick plate)'),
                  loc = 'upper left',
                  fontsize = 10,
                  bbox_to_anchor = (1.0, 1.0))

    Counter = GraphInstance.getImageCounter( )
    plt.savefig( './static/images/ModalOverlapFactor%d.png' % Counter,
                 bbox_inches = 'tight', pdi = 300 )

    #GraphInstance.updateTestGraph( "ModalOverlapFactor", Counter )



def plotMaximumElementSize( GraphInstance ):

    plt.clf( )

    # ......................        LamdaH graph         .......................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 5 ][ 0 ],
                basex = 10, linestyle = ':', linewidth = 2, color = GREEN )

    # .....................  LamdaH_Effective graph  ...........................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 5 ][ 1 ],
                basex = 10, linestyle = '-.', linewidth = 2, color = GREEN )

    # ........................ ElementSize graph ..............................
    plt.loglog( GraphInstance.getRange( ), GraphInstance.Functions[ 5 ][ 2 ],
                basex = 10, linestyle = '-', linewidth = 2, color = GRAY )

    plt.ylabel( 'Maximum Element Size, [ m ]' )
    plt.xlabel( 'Frequency in Hz' )

    plt.legend( ('Bending Wave Length',
                 'Effective Bending Wave Length',
                 'Maximum Element Size \n(Quadratic Shape Functions)'),
                loc = 'upper left',
                fontsize = 10,
                bbox_to_anchor = (1.0, 1.0) )

    Counter = GraphInstance.getImageCounter( )
    plt.savefig( './static/images/MaximumElementSize%d.png' % Counter,
                 bbox_inches = 'tight', pdi = 300 )

    #GraphInstance.updateTestGraph( "MaximumElementSize", Counter )
    # LamdaH, LamdaH_Effective, ElementSize


def plotEigenfrequenciesPlate( GraphInstance ):

    plt.clf( )

    cell_text = [ str(round(Element,3)) for Element in GraphInstance.Functions[ 6 ] ]

    columns = ( '$F_{11}$', '$F_{12}$', '$F_{21}$', '$F_{22}$' )
    colors = plt.cm.BuPu( np.linspace( 0, 0.5, len( columns ) ) )

    table = plt.table( cellText = [ cell_text ],
                       colColours = colors,
                       colLabels = columns,
                       loc = 'center',
                       cellLoc = 'center',
                       bbox = (0.0, 0.4, 0.6, 0.6))

    plt.axis( 'off' )
    table.auto_set_font_size( False )
    table.set_fontsize( 8.5 )

    Counter = GraphInstance.getImageCounter( )

    plt.savefig( './static/images/Eigenfrequencies%d.png' % Counter,
                 bbox_inches = 'tight', pdi = 150)

    #GraphInstance.updateTestGraph( "Eigenfrequencies", Counter )
