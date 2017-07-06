from bokeh.plotting import figure
from bokeh.models.widgets import RadioButtonGroup
from bokeh.models import ColumnDataSource, Div
from bokeh.layouts import row, column, Spacer
from copy import deepcopy


class GraphCorrupted(Exception):
    pass

class GraphObject:
    """
    That class was designed to hold all necessary data and widgets in one place.
    The class represents one complex widget that consists of three independent
    bokeh widgets, namely: figure, Div and RadioButtonGroup. These widget
    have to communicate to each other passing all relevant information like
    flags, active buttons etc. A user has to pass a list with the names
    of corresponding graphs that is going to be depicted in the
    RadioButtonGroup widget and the range of cuntions
    """



    # Private class variables
    _MAX_NUMBER_OF_LINES = 24
    _LINE_COLORS = [ "black",  "black",  "black",  "black",
                     "blue",   "blue",   "blue",   "blue",
                     "green",  "green",  "green",  "green",
                     "red",    "red",    "red",    "red",
                     "orange", "orange", "orange", "orange",
                     "pink",   "pink",   "pink",   "pink" ]

    _LINE_TYPE = [ 'solid', 'dashed', 'dotdash', 'dashdot',
                   'solid', 'dashed', 'dotdash', 'dashdot',
                   'solid', 'dashed', 'dotdash', 'dashdot',
                   'solid', 'dashed', 'dotdash', 'dashdot',
                   'solid', 'dashed', 'dotdash', 'dashdot',
                   'solid', 'dashed', 'dotdash', 'dashdot' ]


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


        self.LabelText = Div( text = """Text Legend: """,
                         width = 350,
                         height = 100 )




        self.GraphRadioButtons = RadioButtonGroup( labels = self.__GraphNames,
                                                   width = 500,
                                                   active = 0 )

        self.Graph = figure( title = "",
                             tools = "",
                             width = Width,
                             height = Height )

        #self.Graph.x_mapper_type = 'log'
        #self.Graph.y_mapper_type = 'log'

        # Assign lines to the graph
        self.GraphData = [ ]
        for i in range( GraphObject._MAX_NUMBER_OF_LINES ):
            self.GraphData.append( ColumnDataSource( data = dict( XData = [ ],
                                                                  YData = [ ] ) ) )

            self.Graph.line( x = 'XData',
                             y = 'YData',
                             color = GraphObject._LINE_COLORS[ i ],
                             line_dash = GraphObject._LINE_TYPE[ i ],
                             source = self.GraphData[ i ] )



        # Create one common widget that is going to represent the entire class
        self.Widget = row( column( self.GraphRadioButtons, self.Graph ),
                           column(  Spacer( height = 100 ), self.LabelText ) )


    def removeLines(self):
        # the function assigns all entries within Graph data set to empty lists

        for i in range( len( self.GraphData ) ):
            self.GraphData[ i ].data = dict( XData = [ ], YData = [ ] )



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

        print self.__PlottingGraphNumber


    # GETTERS
    def getRange(self):
        return deepcopy( self.__Range )


    def getMode(self):
        return self.__Mode


    def getCurrentGraphNumber(self):
        return self.__PlottingGraphNumber

    def setLogAxis(self):
        self.Graph.x_mapper_type='log'
        self.Graph.y_mapper_type='log'
        print "HELLO from log"


    def setLinearAxis(self):
        self.Graph.x_mapper_type='linear'
        self.Graph.y_mapper_type='linear'
        print "HELLO from linear "