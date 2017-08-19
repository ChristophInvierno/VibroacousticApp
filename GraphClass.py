from bokeh.plotting import figure
from bokeh.models.widgets import RadioButtonGroup
from bokeh.models import ColumnDataSource, Div
from bokeh.layouts import row, column, Spacer
from bokeh.plotting import figure, reset_output
from copy import deepcopy
from bokeh.plotting import reset_output
import os


class GraphCorrupted(Exception):
    pass


class GraphObject:
    IMAGE_COUNTER = 0;
    """
    That class was designed to hold all necessary data and widgets in one place.
    The class represents one complex widget that consists of three independent
    bokeh widgets, namely: figure, Div and RadioButtonGroup. These widget
    have to communicate to each other passing all relevant information like
    flags, active buttons etc. A user has to pass a list with the names
    of corresponding graphs that is going to be depicted in the
    RadioButtonGroup widget and the range of cuntions
    """


    def __init__( self, GraphNames, aRange, Width = 650, Height = 550 ):


        #.................. Set up all necessary variables ....................
        if len( GraphNames ) == 0:
            raise GraphCorrupted( "ERROR: the list of graph names is empty" )
        else:
            self.__GraphNames = GraphNames
            self.__NumberOfFunctions = len( GraphNames )
            self.Functions = range( 0, self.__NumberOfFunctions )



        if len( aRange ) == 0:
            raise GraphCorrupted( "ERROR: the list of argument values is empty" )
        else:
            self.__Range = aRange


        # Mode represents to states, namely: orthotropic(0) and isotropic(1)
        self.__Mode = 0
        self.__PlottingGraphNumber = 0;


        # ......... Initialize all widgets for that particular class ...........

        self.TestGraph = Div( text = """ Image""",
                              render_as_text = False,
                              width = 1,
                              height = 1 )



        self.GraphRadioButtons = RadioButtonGroup( labels = self.__GraphNames,
                                                   width = 500,
                                                   active = 0 )




        # Create one common widget that is going to represent the entire class
        self.Widget = row( column( self.GraphRadioButtons,
                                   self.TestGraph,
                                   Spacer( height = 550 ) ) )



    # SETTERS
    def setRange( self, aRange ):
        if len( aRange ) == 0:
            raise GraphCorrupted( "ERROR: the list of argument values is empty" )
        else:
            self.__Range = aRange


    def setMode( self, aMode ):
        if ( aMode != 0 ) and ( aMode != 1 ):
            raise GraphCorrupted( "ERROR: a wrong mode was set" )
        else:
            self.__Mode = aMode


    def setPlottingGraphNumber( self, Number ):
        if ( Number < 0 ) or ( Number > self.__NumberOfFunctions ):
            raise GraphCorrupted( "ERROR: the graph number is out of the range" )
        else:
            self.__PlottingGraphNumber = Number

        #DEBUGGING
        #print self.__PlottingGraphNumber


    # GETTERS
    def getRange(self):
        return deepcopy( self.__Range )


    def getMode(self):
        return self.__Mode


    def getCurrentGraphNumber(self):
        return self.__PlottingGraphNumber



    def loadImage(self, FileName ):

        # remove the old file from the root folder
        #File = "./static/images/{}{}.png".format(FileName, (Counter - 1))
        #if os.path.isfile( File ):
        #    os.remove( File )

        # load the new file that was generated by the caller
        self.TestGraph.text = """
            <p>
            <img src="/VibroacousticApp/static/images/{}{}.png" width=1000>
            </p>
            <p>
            </p>""".format(FileName, GraphObject.IMAGE_COUNTER )

    def remove(self, FileName ):

        # remove the old file from the root folder
        File = "./static/images/{}{}.png".format(FileName, GraphObject.IMAGE_COUNTER )
        if os.path.isfile( File ):
            os.remove( File )

    def removeAll(self):
        os.system( 'rm -f ./static/images/*' )


    def getImageCounter(self):
        return GraphObject.IMAGE_COUNTER


    def inceremetImageCounter(self):
        GraphObject.IMAGE_COUNTER += 1
        return GraphObject.IMAGE_COUNTER
