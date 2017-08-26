import matplotlib.pyplot as plt
import numpy as np
import random
from Colors import *

from bokeh.io import reset_output
from bokeh.models import ColumnDataSource
from GraphClass import GraphObject


def plotWaveSpeedGraphWithLimits( GraphInstance ):

    GraphInstance.cleanGraph()
    GraphInstance.Graph.yaxis.axis_label = "Wave velocity in m/s"
    GraphInstance.Graph.xaxis.axis_label = "Frequency in Hz"

    # Find the maximum values in both x and y direction to be able to
    # depict both vertical and horizontal lines
    MaxCoordinateY = max( GraphInstance.Functions[ 0 ][ 3 ] )
    MaxCoordinateX = max( GraphInstance.getRange( ) )
    MinCoordinateY = min( GraphInstance.Functions[ 0 ][ 1 ] )
    MinCoordinateX = min( GraphInstance.getRange( ) )

    # ............................ c_L graph ...................................
    # 'Quasi-longitudial, in-plane'
    RangeX = [ MinCoordinateX, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 9 ][ 0 ],
               GraphInstance.Functions[ 0 ][ 9 ][ 0 ] ]


    GraphInstance.GraphData[ 0 ].data = dict( XData = RangeX,
                                              YData = RangeY )

    GraphInstance.defineLine( 0, 'Quasi-longitudial, in-plane',
                              DARK_BLUE,
                              'solid' )

    # .................... c_L_thick graph .............................
    # 'Longitudinal out-of-plane'
    RangeX = [ MinCoordinateX, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 10 ],
               GraphInstance.Functions[ 0 ][ 10 ] ]

    GraphInstance.GraphData[ 1 ].data = dict( XData = RangeX,
                                               YData = RangeY )

    GraphInstance.defineLine( 1, 'Longitudinal out-of-plane',
                              DARK_BLUE,
                              'dashed' )


    # ............................ c_S graph ...................................
    # 'Shear, in-plane'
    RangeX = [ MinCoordinateX, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 5 ],
               GraphInstance.Functions[ 0 ][ 5 ] ]

    GraphInstance.GraphData[ 2 ].data = dict( XData = RangeX,
                                              YData = RangeY )

    GraphInstance.defineLine( 2, 'Shear, in-plane',
                              LIGHT_BLUE,
                              'solid' )


    # ................... c_S_outofplane_1 graph ............................
    # 'Shear out-of-plane prop. (G32)'
    RangeX = [ MinCoordinateX, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 7 ],
               GraphInstance.Functions[ 0 ][ 7 ] ]

    GraphInstance.GraphData[ 3 ].data = dict( XData = RangeX,
                                               YData = RangeY )

    GraphInstance.defineLine( 3, 'Shear out-of-plane prop. (G32)',
                              LIGHT_BLUE,
                              'dashed' )


    # ................... c_S_outofplane_2 graph ............................
    # 'Shear out-of-plane prop. (G31)'
    RangeX = [ MinCoordinateX, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 8 ],
               GraphInstance.Functions[ 0 ][ 8 ] ]

    GraphInstance.GraphData[ 4 ].data = dict( XData = RangeX,
                                               YData = RangeY )

    GraphInstance.defineLine( 4, 'Shear out-of-plane prop. (G31)',
                              LIGHT_BLUE,
                              'dashed' )


    # ......................... c_B_shear graph ................................
    # 'Shear (corrected), out-of-plane displ.'
    RangeX = [ MinCoordinateX, MaxCoordinateX ]
    RangeY = [ GraphInstance.Functions[ 0 ][ 2 ],
               GraphInstance.Functions[ 0 ][ 2 ] ]

    GraphInstance.GraphData[ 5 ].data = dict( XData = RangeX,
                                              YData = RangeY )

    GraphInstance.defineLine( 5, 'Shear (corrected), out-of-plane displ.',
                              LIGHT_BLUE,
                              'dotted' )


    # .......................... c_B_eff graph .................................
    # 'Pure bending (thin plate)'
    GraphInstance.GraphData[ 6 ].data = dict( XData = GraphInstance.getRange(),
                                              YData = GraphInstance.Functions[ 0 ][ 1 ] )

    GraphInstance.defineLine( 6, 'Pure bending (thin plate)',
                              GREEN,
                              'dotdash' )


    # ............................ c_B graph ...................................
    # 'Effective bending (thick plate)'
    GraphInstance.GraphData[ 7 ].data = dict( XData = GraphInstance.getRange(),
                                              YData = GraphInstance.Functions[ 0 ][ 0 ] )

    GraphInstance.defineLine( 7, 'Effective bending (thick plate)',
                              GREEN,
                              'dashed' )



    # ............................ c_g graph ...................................
    # 'Group (bending)'
    GraphInstance.GraphData[ 8 ].data = dict( XData = GraphInstance.getRange(),
                                              YData = GraphInstance.Functions[ 0 ][ 3 ] )

    GraphInstance.defineLine( 8, 'Group (bending)',
                              ORANGE,
                              'dashed' )


    # .......................... c_g_eff graph .................................
    # 'Group (effective bending)'
    GraphInstance.GraphData[ 9 ].data = dict( XData = GraphInstance.getRange(),
                                              YData = GraphInstance.Functions[ 0 ][ 4 ] )

    GraphInstance.defineLine( 9, 'Group (effective bending)',
                              ORANGE,
                              'dotdash' )


    # .................... fR_B graph .............................
    # 'Thin-Plate-Limit Group'
    RangeX = [ GraphInstance.Functions[ 0 ][ 15 ],
               GraphInstance.Functions[ 0 ][ 15 ] ]
    RangeY = [ MinCoordinateY, MaxCoordinateY ]

    GraphInstance.GraphData[ 10 ].data = dict( XData = RangeX,
                                               YData = RangeY )

    GraphInstance.defineLine( 10, 'Thin-Plate-Limit Group',
                              ORANGE,
                              'dashed' )


    # .................... fR_B graph .............................
    # 'Thin-Plate-Limit Phase'
    RangeX = [ GraphInstance.Functions[ 0 ][ 14 ],
               GraphInstance.Functions[ 0 ][ 14 ] ]
    RangeY = [ MinCoordinateY, MaxCoordinateY ]

    GraphInstance.GraphData[ 11 ].data = dict( XData = RangeX,
                                               YData = RangeY )

    GraphInstance.defineLine( 11, 'Thin-Plate-Limit Phase',
                              GREEN,
                              'dashed' )


    # ................... f_thickmode_shear_y graph ............................
    # '1st Thickness-shear resonance (G32)'
    RangeX = [ GraphInstance.Functions[ 0 ][ 13 ],
               GraphInstance.Functions[ 0 ][ 13 ] ]
    RangeY = [ MinCoordinateY, MaxCoordinateY ]

    GraphInstance.GraphData[ 12 ].data = dict( XData = RangeX,
                                              YData = RangeY )

    #plt.loglog( RangeX, RangeY, linestyle = '--', color = LIGHT_BLUE )
    GraphInstance.defineLine( 12, '1st Thickness-shear resonance (G32)',
                              LIGHT_BLUE,
                              'dashed' )


    # .................... f_thickmode_shear graph .............................
    # '1st Thickness-shear resonance (G31)'
    RangeX = [ GraphInstance.Functions[ 0 ][ 11 ],
               GraphInstance.Functions[ 0 ][ 11 ] ]
    RangeY = [ MinCoordinateY, MaxCoordinateY ]

    GraphInstance.GraphData[ 13 ].data = dict( XData = RangeX,
                                              YData = RangeY )

    GraphInstance.defineLine( 13, '1st Thickness-shear resonance (G31)',
                              LIGHT_BLUE,
                              'dashed' )


    # ................... f_thickmode_shear_x graph ............................
    # '1st Thickness-stretch resonance'
    RangeX = [ GraphInstance.Functions[ 0 ][ 12 ],
               GraphInstance.Functions[ 0 ][ 12 ] ]
    RangeY = [ MinCoordinateY, MaxCoordinateY ]

    GraphInstance.GraphData[ 14 ].data = dict( XData = RangeX,
                                              YData = RangeY )


    GraphInstance.defineLine( 14, '1st Thickness-stretch resonance',
                              DARK_BLUE,
                              'dotdash' )


def plotWaveSpeedGraph( GraphInstance ):

        GraphInstance.cleanGraph()
        GraphInstance.Graph.yaxis.axis_label = "Wave velocity in m/s"
        GraphInstance.Graph.xaxis.axis_label = "Frequency in Hz"

        # Find the maximum values in both x and y direction to be able to
        # depict both vertical and horizontal lines
        MaxCoordinateY = max( GraphInstance.Functions[ 0 ][ 3 ] )
        MaxCoordinateX = max( GraphInstance.getRange( ) )
        MinCoordinateY = min( GraphInstance.Functions[ 0 ][ 1 ] )
        MinCoordinateX = min( GraphInstance.getRange( ) )

        # ............................ c_L graph ...................................
        # 'Quasi-longitudial, in-plane'
        RangeX = [  MinCoordinateX, MaxCoordinateX ]
        RangeY = [ GraphInstance.Functions[ 0 ][ 9 ][ 0 ],
                   GraphInstance.Functions[ 0 ][ 9 ][ 0 ] ]


        GraphInstance.GraphData[ 0 ].data = dict( XData = RangeX,
                                                  YData = RangeY )

        GraphInstance.defineLine( 0, 'Quasi-longitudial, in-plane',
                                  DARK_BLUE,
                                  'solid' )


        # .................... c_L_thick graph .............................
        # 'Longitudinal out-of-plane'
        RangeX = [ MinCoordinateX, MaxCoordinateX ]
        RangeY = [ GraphInstance.Functions[ 0 ][ 10 ],
                   GraphInstance.Functions[ 0 ][ 10 ] ]

        GraphInstance.GraphData[ 1 ].data = dict( XData = RangeX,
                                                  YData = RangeY )

        GraphInstance.defineLine( 1, 'Longitudinal out-of-plane',
                                  DARK_BLUE,
                                  'dashed' )


        # ............................ c_S graph ...................................
        # 'Shear, in-plane'
        RangeX = [ MinCoordinateX, MaxCoordinateX ]
        RangeY = [ GraphInstance.Functions[ 0 ][ 5 ],
                   GraphInstance.Functions[ 0 ][ 5 ] ]

        GraphInstance.GraphData[ 2 ].data = dict( XData = RangeX,
                                                  YData = RangeY )

        GraphInstance.defineLine( 2, 'Shear, in-plane',
                                  LIGHT_BLUE,
                                  'solid' )


        # ................... c_S_outofplane_1 graph ............................
        # 'Shear out-of-plane prop. (G32)'
        RangeX = [ MinCoordinateX, MaxCoordinateX ]
        RangeY = [ GraphInstance.Functions[ 0 ][ 7 ],
                   GraphInstance.Functions[ 0 ][ 7 ] ]

        GraphInstance.GraphData[ 3 ].data = dict( XData = RangeX,
                                                  YData = RangeY )

        GraphInstance.defineLine( 3, 'Shear out-of-plane prop. (G32)',
                                  LIGHT_BLUE,
                                  'dashed' )


        # ................... c_S_outofplane_2 graph ............................
        # 'Shear out-of-plane prop. (G31)'
        RangeX = [ MinCoordinateX, MaxCoordinateX ]
        RangeY = [ GraphInstance.Functions[ 0 ][ 8 ],
                   GraphInstance.Functions[ 0 ][ 8 ] ]

        GraphInstance.GraphData[ 4 ].data = dict( XData = RangeX,
                                                  YData = RangeY )

        GraphInstance.defineLine( 4, 'Shear out-of-plane prop. (G31)',
                                  LIGHT_BLUE,
                                  'dashed' )


        # ......................... c_B_shear graph ................................
        # 'Shear (corrected), out-of-plane displ.'
        RangeX = [ MinCoordinateX, MaxCoordinateX ]
        RangeY = [ GraphInstance.Functions[ 0 ][ 2 ],
                   GraphInstance.Functions[ 0 ][ 2 ] ]

        GraphInstance.GraphData[ 5 ].data = dict( XData = RangeX,
                                                  YData = RangeY )

        GraphInstance.defineLine( 5, 'Shear (corrected), out-of-plane displ.',
                                  LIGHT_BLUE,
                                  'dotted' )


        # .......................... c_B_eff graph .................................
        # 'Pure bending (thin plate)'
        GraphInstance.GraphData[ 6 ].data = dict( XData = GraphInstance.getRange(),
                                                  YData = GraphInstance.Functions[ 0 ][ 1 ] )

        GraphInstance.defineLine( 6, 'Pure bending (thin plate)',
                                  GREEN,
                                  'dotdash' )


        # ............................ c_B graph ...................................
        # 'Effective bending (thick plate)'
        GraphInstance.GraphData[ 7 ].data = dict( XData = GraphInstance.getRange(),
                                                  YData = GraphInstance.Functions[ 0 ][ 0 ] )

        GraphInstance.defineLine( 7, 'Effective bending (thick plate)',
                                  GREEN,
                                  'dashed' )


        # ............................ c_g graph ...................................
        # 'Group (bending)'
        GraphInstance.GraphData[ 8 ].data = dict( XData = GraphInstance.getRange(),
                                                  YData = GraphInstance.Functions[ 0 ][ 3 ] )

        GraphInstance.defineLine( 8, 'Group (bending)',
                                  ORANGE,
                                  'dashed' )


        # .......................... c_g_eff graph .................................
        # 'Group (effective bending)'
        GraphInstance.GraphData[ 9 ].data = dict( XData = GraphInstance.getRange(),
                                                  YData = GraphInstance.Functions[ 0 ][ 4 ] )

        GraphInstance.defineLine( 9, 'Group (effective bending)',
                                  ORANGE,
                                  'dotdash' )


def plotModesInBand( GraphInstance ):

    GraphInstance.cleanGraph( )
    GraphInstance.Graph.yaxis.axis_label = "Number of modes per one-third octave band"
    GraphInstance.Graph.xaxis.axis_label = "Frequency in Hz"

    # ............................ bending_np graph ............................
    # 'Effective bending (thick plate)'
    GraphInstance.GraphData[ 0 ].data = dict( XData = GraphInstance.Functions[ 2 ][ 4 ],
                                              YData = GraphInstance.Functions[ 2 ][ 0 ] )

    GraphInstance.defineLine( 0, 'Effective bending (thick plate)',
                              GREEN,
                              'solid' )


    # ............................ compressional_np graph ......................
    # 'Shear, in-plane'
    GraphInstance.GraphData[ 1 ].data = dict( XData = GraphInstance.Functions[ 2 ][ 4 ],
                                              YData = GraphInstance.Functions[ 2 ][ 2 ] )

    GraphInstance.defineLine( 1, 'Shear, in-plane',
                              LIGHT_BLUE,
                              'solid' )


    # ............................ shear_np graph ..............................
    # 'Quasi-longitudial, in plane'
    GraphInstance.GraphData[ 2 ].data = dict( XData = GraphInstance.Functions[ 2 ][ 4 ],
                                              YData = GraphInstance.Functions[ 2 ][ 1 ] )

    GraphInstance.defineLine( 2, 'Quasi-longitudial, in plane',
                              DARK_BLUE,
                              'solid' )


def plotModalDensity( GraphInstance ):

    GraphInstance.cleanGraph( )
    GraphInstance.Graph.yaxis.axis_label = "Modal Density in s/rad"
    GraphInstance.Graph.xaxis.axis_label = "Frequency in Hz"

    # ............................ bending_np graph ............................
    # 'Quasi-longitudinal, in-plane'
    GraphInstance.GraphData[ 0 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 3 ][ 0 ] )

    GraphInstance.defineLine( 0, 'Quasi-longitudinal, in-plane',
                              DARK_BLUE,
                              'solid' )

    # ............................ bending_np graph ............................
    # 'Shear, in-plane'
    GraphInstance.GraphData[ 1 ].data = dict( XData = GraphInstance.getRange( ),
                                                YData = GraphInstance.Functions[ 3 ][ 2 ] )

    GraphInstance.defineLine( 1, 'Shear, in-plane',
                              LIGHT_BLUE,
                              'solid' )

    # ............................ bending_np graph ............................
    # 'Effective bending (thick plate)'
    GraphInstance.GraphData[ 2 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 3 ][ 1 ] )

    GraphInstance.defineLine( 2, 'Effective bending (thick plate)',
                              GREEN,
                              'solid' )


def plotModalOverlapFactor( GraphInstance ):

    GraphInstance.cleanGraph( )
    GraphInstance.Graph.yaxis.axis_label = "Half Power Bandwith Modal Overlap Factor"
    GraphInstance.Graph.xaxis.axis_label = "Frequency in Hz"

    # ...................... Mhp_QuasiLongitudinal graph .......................
    # 'Quasi-longitudinal, in-plane'
    GraphInstance.GraphData[ 0 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 4 ][ 0 ] )

    GraphInstance.defineLine( 0, 'Quasi-longitudinal, in-plane',
                              DARK_BLUE,
                              'solid' )

    # ......................... Mhp_Shear graph ................................
    # 'Shear, in-plane'
    GraphInstance.GraphData[ 1 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 4 ][ 1 ] )

    GraphInstance.defineLine( 1, 'Shear, in-plane',
                              LIGHT_BLUE,
                              'solid' )

    # ........................ Mhp_Effective graph .............................
    # 'Effective bending (thick plate)'
    GraphInstance.GraphData[ 2 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 4 ][ 2 ] )

    GraphInstance.defineLine( 2, 'Effective bending (thick plate)',
                              GREEN,
                              'solid' )


def plotMaximumElementSize( GraphInstance ):

    GraphInstance.cleanGraph( )
    GraphInstance.Graph.yaxis.axis_label = "Maximum Element Size, [ m ]"
    GraphInstance.Graph.xaxis.axis_label = "Frequency in Hz"

    # ......................        LamdaH graph         .......................
    # 'Bending Wave Length'
    GraphInstance.GraphData[ 0 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 5 ][ 0 ] )

    GraphInstance.defineLine( 0, 'Bending Wave Length',
                              GREEN,
                              'dotted' )

    # .....................  LamdaH_Effective graph  ...........................
    # 'Effective Bending Wave Length'
    GraphInstance.GraphData[ 1 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 5 ][ 1 ] )

    GraphInstance.defineLine( 1, 'Effective Bending Wave Length',
                              GREEN,
                              'dotdash' )


    # ........................ ElementSize graph ...............................
    # 'Maximum Element Size \n(Quadratic Shape Functions)'
    GraphInstance.GraphData[ 2 ].data = dict( XData = GraphInstance.getRange( ),
                                              YData = GraphInstance.Functions[ 5 ][ 2 ] )

    GraphInstance.defineLine( 2, 'Maximum Element Size (QSF)',
                              GRAY,
                              'solid' )


def plotEigenfrequenciesPlate( GraphInstance ):
    Text = "F<sub>11</sub> = {} [Hz], F<sub>12</sub> = {} [Hz], " \
           "F<sub>21</sub> = {} [Hz], F<sub>22</sub> = {} [Hz]".format(
        round( GraphInstance.Functions[ 6 ][ 0 ], 2 ),
        round( GraphInstance.Functions[ 6 ][ 1 ], 2 ),
        round( GraphInstance.Functions[ 6 ][ 2 ], 2 ),
        round( GraphInstance.Functions[ 6 ][ 3 ], 2 )
    )


    GraphInstance.TextWidget.printMessage( Text )
    pass
    '''
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
    '''