# Example: import of an entire library
import numpy as np
from math import *

# Example: import a module from a library
from bokeh.plotting import figure
from bokeh.models.widgets import RadioButtonGroup
from bokeh.io import curdoc
from bokeh.layouts import column
from functools import partial
from bokeh.models import ColumnDataSource


def main():

    # Define all necessary variables, arrays, lists etc at this section
    # I mean that you have to define all data that you have to get from GUI
    # in the main function


    # Define the number of functions that we'll get in our project
    NUMBER_OF_FUNCTIONS = 2
    Functions = range( 0, NUMBER_OF_FUNCTIONS )


    # That's the plot that will be depict on the screen
    Graph = figure( title = "",
                    tools = "",
                    width = 500,
                    height = 500 )


    # The data that will be depict on the screen
    # INPORTANT: the data will be changed inside the callback
    # function ( updateGraph ) according to a selected tag
    Data = ColumnDataSource(data = dict( XData=[], YData=[] ))

    # set up the line on the plot
    Graph.line( x = 'XData',
                y = 'YData',
                source = Data )


    # Basic comunication widget (tags)
    RadioButtons = RadioButtonGroup( labels = [ "PARABOLA",
                                                "SIN" ],
                                     width = 500,
                                     active = 0 )


    # it's your input parameters
    Argument = np.linspace( 0.0, 100, 201 )

    # At that point I'm going to call your function to grap the information
    Functions[ 0 ] = computeParabola( Argument )
    Functions[ 1 ] = computeSin( Argument )


    # Set up callback function for RadioButtons (tags)
    RadioButtons.on_click(partial( updateGraph, Data, Argument, Functions ) )


    # generate html
    curdoc().add_root( column( Graph, RadioButtons ) )



def updateGraph( Data, Argument, Functions, Properties ):

    if Properties == 0:
        #if len( Argument ) == len( FunctionOne ):
        Data.data = dict( XData = Argument, YData = Functions[ 0 ] )

    elif Properties == 1:
        #if len( Argument ) == len( FunctionOne ):
        Data.data = dict( XData = Argument, YData = Functions[ 1 ] )




################################################################################
#                               YOUR SECTION
################################################################################

# Translate your Matlab code at this section


# EXAMPLES:
def computeParabola( Variables ):
    Porabola = []
    for x in Variables:
        Porabola.append( x**2 )

    return Porabola


def computeSin( Variables ):
    Sin = []
    for x in Variables:
        Sin.append( sin( x ) )

    return Sin

################################################################################


main()