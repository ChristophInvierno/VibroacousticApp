# Link bokeh libraries
from bokeh.plotting import figure
from bokeh.layouts import column, row, Spacer
from bokeh.io import curdoc, show
from bokeh.models import Div, Label, Plot, ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Text
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider
from bokeh.models.widgets import TextInput, AutocompleteInput

# Link third-party python libraries
from math import cos, sin, radians, sqrt, pi, atan2
from functools import partial
import matplotlib.pyplot as plt

# Link custom files
from LatexSupport import LatexLabel
from UnicodeSymbols import *
from Helper import Flag
from wave_speeds import *
from wave_speeds import *
from Graphs import *

# TODO: change the name of the module
from InteractiveTable import InteractiveTable


def main( ):
    # Quasi constant
    FrequencyRange = np.linspace( 0, 1000001, num = 1000 ) + 1
    # the main function only describes both graphical and comunication
    # of the app.


    # ========================== GRAPHICAL PART =================================

    # CREATE ALL PLOTS:
    Input = figure( title = "",
                    tools = "",
                    width = 500,
                    height = 500 )

    Graph = figure( title = "",
                    tools = "",
                    width = 650,
                    height = 550 )

    # CREATE TABLES:
    # ........................ Elastic Modulus table ...........................
    ELASTIC_MODULUS_TITEL = Div( text = """ELASTIC MODULUS:""" )
    ElasticModulus = InteractiveTable( 1, 3 )
    ElasticModulus.setTitels( [ [ EMODUL_X, EMODUL_Y, EMODUL_Z ] ] )
    ElasticModulus.setValues( [ [ "1.061e10", "7.605e08", "3.667e08" ] ] )

    # ........................ Shear Modulus table .............................
    SHEAR_MODULUS_TITEL = Div( text = """SHEAR MODULUS:""" )
    ShearModulus = InteractiveTable( 1, 3 )
    ShearModulus.setTitels( [ [ EMODUL_XY, EMODUL_XZ, EMODUL_YZ ] ] )
    ShearModulus.setValues( [ [ "6.900e08", "1.725e08", "9.857e07" ] ] )

    # ........................ Poisson’s ratios ................................
    POISSON_RATIO_TITEL = Div( text = """POISSON'S RATIOS:""" )
    PoissonRatios = InteractiveTable( 2, 3 )
    PoissonRatios.setTitels( [ [ POISSON_RATIO_XY,
                                 POISSON_RATIO_XZ,
                                 POISSON_RATIO_YZ ],
                               [ POISSON_RATIO_YX + "\t( auto )",
                                 POISSON_RATIO_ZX + "\t( auto )",
                                 POISSON_RATIO_ZY + "\t( auto )" ] ] )

    PoissonRatios.setValues( [ [ "1.184", "1.771", "0.382" ],
                               [ "0.085", "0.061", "0.184" ] ] )

    # ........................ Material Properties table .......................
    MATERIALS_TITEL = Div( text = """MATERIAL PROPERTIES:""" )
    MaterialProperties = InteractiveTable( 1, 2 )
    MaterialProperties.setTitels( [ [ "Density", "Loss Factor" ] ] )
    MaterialProperties.setValues( [ [ "450.0", "0.012" ] ] )

    # ........................ Geometry table .......................
    GEOMETRY_TITEL = Div( text = """GEOMETRY:""" )
    GeometryProperties = InteractiveTable( 1, 3 )
    GeometryProperties.setTitels( [ [ "Length", "Width", "Thickness" ] ] )
    GeometryProperties.setValues( [ [ "2.5", "3.0", "0.081" ] ] )

    # CREATE BUTTONS:
    SetDefaultButton = Button( label = "Default",
                               button_type = "success",
                               width = 100 )

    ApplyButton = Button( label = "Apply",
                          button_type = "success",
                          width = 100 )

    PrintReport = Button( label = "Print Report",
                          button_type = "success",
                          width = 100 )

    ModeRadioButtons = RadioButtonGroup( labels = [ "Orthotropic Material",
                                                    "Isotropic Material" ],
                                         width = 500,
                                         active = 0 )

    GraphRadioButtons = RadioButtonGroup( labels = [ "Wave speed",
                                                     "Modes in Band",
                                                     "Modal Overlap Factor",
                                                     "Natural Frequencies",
                                                     "Limit frequencies",
                                                     "Wavelength - element size for FEM" ],
                                          width = 500,
                                          active = 0 )

    # SPECIFY THE LAYOUT:
    Buttons = row( row( Spacer( width = 115 ),
                        SetDefaultButton,
                        Spacer( width = 50 ),
                        ApplyButton,
                        Spacer( width = 50 ),
                        PrintReport ) )

    RightSide = column( ModeRadioButtons,
                        ELASTIC_MODULUS_TITEL,
                        ElasticModulus.Table,
                        SHEAR_MODULUS_TITEL,
                        ShearModulus.Table,
                        POISSON_RATIO_TITEL,
                        PoissonRatios.Table,
                        MATERIALS_TITEL,
                        MaterialProperties.Table,
                        GEOMETRY_TITEL,
                        GeometryProperties.Table )

    LeftSide = column( GraphRadioButtons, Graph, Buttons )

    # ========================= COMMUNICATION PART =============================
    Mode = Flag( GraphRadioButtons.active )
    GraphID= Flag( GraphRadioButtons.active )

    # set up the line and corresponding colors within the plot
    MAX_NUMBER_OF_LINES = 24
    LINE_COLORS = [ "black",  "black",  "black",  "black",
                    "blue",   "blue",   "blue",   "blue",
                    "green",  "green",  "green",  "green",
                    "red",    "red",    "red",    "red",
                    "orange", "orange", "orange", "orange",
                    "pink",   "pink",   "pink",   "pink" ]

    LINE_TYPE = [ 'solid', 'dashed', 'dotdash', 'dashdot',
                  'solid', 'dashed', 'dotdash', 'dashdot',
                  'solid', 'dashed', 'dotdash', 'dashdot',
                  'solid', 'dashed', 'dotdash', 'dashdot',
                  'solid', 'dashed', 'dotdash', 'dashdot',
                  'solid', 'dashed', 'dotdash', 'dashdot' ]


    # initialize the default data of lines
    Data = [ ]
    for i in range( MAX_NUMBER_OF_LINES ):
        Data.append( ColumnDataSource( data = dict( XData = [ 0 ], YData = [ 0 ] ) ) )

        Graph.line( x = 'XData',
                    y = 'YData',
                    color = LINE_COLORS[ i ],
                    line_dash = LINE_TYPE[ i ],
                    source = Data[ i ] )


    NUMBER_OF_FUNCTIONS = 6
    Functions = range( 0, NUMBER_OF_FUNCTIONS )

    # Set up callback function for the "Apply" button
    ApplyButton.on_click( partial( updateData,
                                   Data,
                                   ElasticModulus,
                                   ShearModulus,
                                   PoissonRatios,
                                   MaterialProperties,
                                   GeometryProperties,
                                   Functions,
                                   FrequencyRange,
                                   Mode,
                                   GraphID,
                                   Graph ) )


    # Set up callback function for all radion buttons that are responsible
    # for plotting different graphs
    GraphRadioButtons.on_click( partial( updateGraph,
                                         NUMBER_OF_FUNCTIONS,
                                         FrequencyRange,
                                         Functions,
                                         Data,
                                         Graph,
                                         Mode,
                                         GraphID ) )

    # Set up callback function for all radion buttons that are responsible
    # for changing the mode, namely: Isotropic and Orthotropic material properties
    ModeRadioButtons.on_click( partial( updateMode,
                                        ElasticModulus,
                                        ShearModulus,
                                        PoissonRatios,
                                        MaterialProperties,
                                        GeometryProperties,
                                        Mode ) )

    # Set up callback function for all the "Default" button that are responsible
    # for assigning the default data to all entries
    SetDefaultButton.on_click( partial( setDeafultSettings,
                                        ElasticModulus,
                                        ShearModulus,
                                        PoissonRatios,
                                        MaterialProperties,
                                        GeometryProperties,
                                        Mode,
                                        GraphRadioButtons ) )


    # ================= RUN SIMULATION WITH DEFAULT DATA =====================
    updateData( Data,
                ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Functions,
                FrequencyRange,
                Mode,
                GraphID,
                Graph )


    updateGraph( NUMBER_OF_FUNCTIONS,
                 FrequencyRange,
                 Functions,
                 Data,
                 Graph,
                 Mode,
                 GraphID,
                 0 )


    # RUN ALL WIDJETS
    curdoc( ).add_root( column( Spacer( height = 20 ),
                                row( RightSide,
                                     Spacer( width = 50 ),
                                     LeftSide ) ) )


# ===============================================================================
#                               HELPER FUNCTIONS
# ===============================================================================
def updateData( Data,
                ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Functions,
                FrequencyRange,
                Mode,
                GraphID,
                Graph ):


    # before calling user-define functions check the current mode
    cangeMode( ElasticModulus,
               ShearModulus,
               PoissonRatios,
               MaterialProperties,
               GeometryProperties,
               Mode )


    precomputePoissonRatios( ElasticModulus,
                             ShearModulus,
                             PoissonRatios )

    # get data from the corresponding tables
    ElasticModulusData = ElasticModulus.getData( )
    ShearModulusData = ShearModulus.getData( )
    PoissonRatiosData = PoissonRatios.getData( )
    MaterialPropertiesData = MaterialProperties.getData( )
    GeometryPropertiesData = GeometryProperties.getData( )


    #################### CALL USER-SPECIFIC FAUNCTION ##########################

    Functions[ 0 ] = wave_speeds( ElasticModulusData,
                                  ShearModulusData,
                                  PoissonRatiosData,
                                  MaterialPropertiesData,
                                  GeometryPropertiesData,
                                  bool( Mode.getFlag ),
                                  Functions,
                                  FrequencyRange )


    # Update the current graph with new data
    updateGraph( 6,
                 FrequencyRange,
                 Functions,
                 Data,
                 Graph,
                 Mode,
                 GraphID,
                 GraphID.getFlag() )



def updateGraph( NUMBER_OF_FUNCTIONS,
                 FrequencyRange,
                 Functions,
                 GraphData,
                 Graph,
                 Mode,
                 GraphID,
                 GraphNumber ):

    # Update the graph ID ( GraphNumber - it's a built-in bohek variable that
    # belongs to the RadioButton widget )
    GraphID.setFlag( GraphNumber )


    # Remove existing lines from the plot bokeh widget
    cleanPlots( GraphData )


    # Depict coresponding lines based on the graph chosen by the user
    if (GraphNumber == 0):
        plotWaveSpeedGraph( Graph,
                            GraphData,
                            Functions[ 0 ],
                            FrequencyRange,
                            Mode )

    if (GraphNumber == 1):
        Graph.line(Functions[ 0 ][ 0 ],FrequencyRange )



def updateMode( ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Mode,
                Properties ):


    Mode.setFlag( Properties )

    cangeMode( ElasticModulus,
               ShearModulus,
               PoissonRatios,
               MaterialProperties,
               GeometryProperties,
               Mode )


def cangeMode( ElasticModulus,
               ShearModulus,
               PoissonRatios,
               MaterialProperties,
               GeometryProperties,
               Mode ):


    if (Mode.getFlag( ) == 1):

        UniformValue = ElasticModulus.getValue( 0, 0 )
        ElasticModulus.setValue( 0, 1, UniformValue )
        ElasticModulus.setValue( 0, 2, UniformValue )

        UniformValue = str( ElasticModulus.getFloatValue( 0, 0 ) \
                            / (
                            2.0 * (1.0 + PoissonRatios.getFloatValue( 0, 0 ))) )
        ShearModulus.setValue( 0, 0, UniformValue )
        ShearModulus.setValue( 0, 1, UniformValue )
        ShearModulus.setValue( 0, 2, UniformValue )

        UniformValue = PoissonRatios.getValue( 0, 0 )
        PoissonRatios.setValue( 0, 1, UniformValue )
        PoissonRatios.setValue( 0, 2, UniformValue )


    if (Mode.getFlag( ) == 0):
        ElasticModulus.restoreValue( 0, 1 )
        ElasticModulus.restoreValue( 0, 2 )

        ShearModulus.restoreValue( 0, 0 )
        ShearModulus.restoreValue( 0, 1 )
        ShearModulus.restoreValue( 0, 2 )

        PoissonRatios.restoreValue( 0, 1 )
        PoissonRatios.restoreValue( 0, 2 )

    precomputePoissonRatios( ElasticModulus,
                             ShearModulus,
                             PoissonRatios )


def precomputePoissonRatios( ElasticModulus,
                             ShearModulus,
                             PoissonRatios ):

    # update value of nu_21
    Temp = PoissonRatios.getFloatValue( 0, 0 ) * ElasticModulus.getFloatValue ( 0, 1 ) \
           / ElasticModulus.getFloatValue( 0, 0 )

    PoissonRatios.assignValue( 1, 0, str( Temp ) )

    # update value of nu_31
    Temp = PoissonRatios.getFloatValue( 0, 1 ) * ElasticModulus.getFloatValue( 0, 2 ) \
           / ElasticModulus.getFloatValue( 0, 0 )
    PoissonRatios.assignValue( 1, 1, str( Temp ) )

    # update value of nu_32
    Temp = PoissonRatios.getFloatValue( 0, 2 ) * ElasticModulus.getFloatValue( 0, 2 ) \
           / ElasticModulus.getFloatValue( 0, 1 )

    PoissonRatios.assignValue( 1, 2, str( Temp ) )


def setDeafultSettings( ElasticModulus,
                        ShearModulus,
                        PoissonRatios,
                        MaterialProperties,
                        GeometryProperties,
                        Mode,
                        Widget ):


    ElasticModulus.resetByDefault( )
    ShearModulus.resetByDefault( )
    PoissonRatios.resetByDefault( )


    cangeMode( ElasticModulus,
               ShearModulus,
               PoissonRatios,
               MaterialProperties,
               GeometryProperties,
               Mode )


main( )
