# Link bokeh libraries
from bokeh.plotting import figure
from bokeh.layouts import column, row, Spacer
from bokeh.io import curdoc, show, set_curdoc
from bokeh.models import Div, Label, Plot, ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Text
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider
from bokeh.models.widgets import TextInput, AutocompleteInput
from bokeh.plotting import figure


# Link third-party python libraries
from math import cos, sin, radians, sqrt, pi, atan2
from functools import partial
import matplotlib.pyplot as plt
import threading
from multiprocessing import Process
import time

# Link custom files
from LatexSupport import LatexLabel
from UnicodeSymbols import *
from Helper import Flag, DataCorrupted, testInputData
from wave_speeds import *
from Graphs import *
from GraphClass import GraphObject
from MessageClass import Message
from ModaleDichte import ModaleDichte
from Functions import *


# TODO: change the name of the module
from InteractiveTable import InteractiveTable


def main( ):
    # Quasi constant
    FrequencyRange = np.logspace( 0, 5, 1000 )
    # the main function only describes both graphical and comunication
    # of the app.
    doc = curdoc()

    # ========================== GRAPHICAL PART ================================

    # CREATE ALL PLOTS:
    Input = figure( title = "",
                    tools = "",
                    width = 500,
                    height = 500 )



    Graph = GraphObject( [ "Wave speed",
                           "Wave Velocities plus Limit Frequencies",
                           "Modes in Band",
                           "Modal Density",
                           "Modal Overlap Factor",
                           "Maximum Element Size (FEM)",
                           "Layers Scheme"],
                            FrequencyRange,
                            nFunctions = 7,
                            Width = 850,
                            Height = 550)


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


    # ........................ Poissons ratios ................................
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


    # ........................ Layers table .......................
    LAYER_TITEL = Div( text = """MULTI-LAYERS:""" )
    Layers = InteractiveTable( 4, 1 )
    Layers.setTitels( [ [ "Top Layer 1" ],
                        [ "Top Layer 2" ],
                        [ "Top Layer 3" ],
                        [ "Top Layer 4" ] ] )
    Layers.setValues( [ [ "0.081" ],
                        [ "0.0" ],
                        [ "0.0" ],
                        [ "0.0" ]] )



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

    Homogenize = Button( label = "Homogenize",
                          button_type = "success",
                          width = 100 )

    ShowInput = Button( label = "Show Input",
                        button_type = "success",
                        width = 100 )



    ModeRadioButtons = RadioButtonGroup( labels = [ "Orthotropic Material",
                                                    "Isotropic Material" ],
                                         width = 500,
                                         active = 0 )


    WarningMessage = Message( Color = "red",
                              Size = 2 ,
                              MessageHeader = "Warning: " );


    # SPECIFY THE LAYOUT:
    Buttons = row( row( Spacer( width = 85 ),
                        SetDefaultButton,
                        Spacer( width = 50 ),
                        ApplyButton,
                        Spacer( width = 50 ),
                        PrintReport ) )



    LeftSide = column( ModeRadioButtons,
                        ELASTIC_MODULUS_TITEL,
                        ElasticModulus.Table,
                        SHEAR_MODULUS_TITEL,
                        ShearModulus.Table,
                        POISSON_RATIO_TITEL,
                        PoissonRatios.Table,
                        MATERIALS_TITEL,
                        MaterialProperties.Table,
                        GEOMETRY_TITEL,
                        GeometryProperties.Table,
                        LAYER_TITEL,
                        row( Layers.Table,
                             Spacer(width = 85),
                             column(Homogenize,ShowInput)))

    RightSide = column( Graph.Widget , Buttons, WarningMessage.Widget )


    # ========================= COMMUNICATION PART =============================

    # set up the line and corresponding colors within the plot


    # Set up callback function for the "Apply" button
    ApplyButton.on_click( partial( updateData,
                                   ElasticModulus,
                                   ShearModulus,
                                   PoissonRatios,
                                   MaterialProperties,
                                   GeometryProperties,
                                   Graph,
                                   WarningMessage ) )


    # Set up callback function for all radion buttons that are responsible
    # for changing the mode, namely: Isotropic and Orthotropic material properties
    ModeRadioButtons.on_click( partial( updateMode,
                                        ElasticModulus,
                                        ShearModulus,
                                        PoissonRatios,
                                        MaterialProperties,
                                        GeometryProperties,
                                        WarningMessage,
                                        Graph ) )


    # Set up callback function for all radion buttons that are responsible
    # for plotting different graphs
    Graph.GraphRadioButtons.on_click( partial( updateGraph, Graph ) )


    # Set up callback function for all the "Default" button that are responsible
    # for assigning the default data to all entries
    SetDefaultButton.on_click( partial( setDeafultSettings,
                                        ElasticModulus,
                                        ShearModulus,
                                        PoissonRatios,
                                        MaterialProperties,
                                        GeometryProperties,
                                        Graph,
                                        WarningMessage ) )


    # ================= RUN SIMULATION WITH DEFAULT DATA =====================
    updateData( ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Graph,
                WarningMessage )


    #updateGraph( Graph, 0 )


    # RUN ALL WIDJETS
    doc.add_root( column( Spacer( height = 20 ),
                      row( LeftSide,
                           Spacer( width = 50 ),
                           RightSide,
                           Spacer( width = 50 ) ) ) )



# ===============================================================================
#                               HELPER FUNCTIONS
# ===============================================================================
def updateData( ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Graph,
                WarningMessage ):

    # clean the warning message
    WarningMessage.clean()


    # before calling user-define functions check the current mode
    cangeMode( ElasticModulus,
               ShearModulus,
               PoissonRatios,
               MaterialProperties,
               GeometryProperties,
               WarningMessage,
               Graph.getMode() )


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
    try:

        print Graph.getMode()

        #WarningMessage.printMessage("Running")

        testInputData( Graph.getMode(), PoissonRatiosData )

        Graph.Functions[ 0 ] = wave_speeds( ElasticModulusData,
                                            ShearModulusData,
                                            PoissonRatiosData,
                                            MaterialPropertiesData,
                                            GeometryPropertiesData,
                                            bool( Graph.getMode() ),
                                            Graph.getRange() )


        Graph.Functions[ 2 ] = ModesInBand( ElasticModulusData,
                                            ShearModulusData,
                                            PoissonRatiosData,
                                            MaterialPropertiesData,
                                            GeometryPropertiesData,
                                            bool( Graph.getMode( ) ),
                                            Graph.getRange( ) )


        Graph.Functions[ 3 ] = ModaleDichte( Graph.Functions[ 0 ][ 9 ],
                                             Graph.Functions[ 0 ][ 5 ],
                                             Graph.Functions[ 0 ][ 1 ],
                                             Graph.Functions[ 0 ][ 4 ],
                                             GeometryPropertiesData,
                                             bool( Graph.getMode( ) ),
                                             Graph.getRange( ) )


        Graph.Functions[ 4 ] = ModalOverlapFactor( MaterialPropertiesData,
                                                   Graph.Functions[ 3 ],
                                                   Graph.getRange( ) )


        Graph.Functions[ 5 ] = MaximumElementSize( Graph.Functions[ 0 ][ 0 ],
                                                   Graph.Functions[ 0 ][ 1 ],
                                                   Graph.getRange( ) )


        Graph.Functions[ 6 ] = EigenfrequenciesPlate( ElasticModulusData,
                                                      ShearModulusData,
                                                      PoissonRatiosData,
                                                      MaterialPropertiesData,
                                                      GeometryPropertiesData,
                                                      bool( Graph.getMode() ),
                                                      Graph.getRange() )

        # Update the current graph with new data
        updateGraph( Graph, Graph.getCurrentGraphNumber( ) )

        WarningMessage.clean()


    except DataCorrupted as Error:
        WarningMessage.printMessage( str(Error) )

def updateGraph( Graph, GraphNumber ):


    # Update the graph ID ( GraphNumber - it's a built-in bohek variable that
    # belongs to the RadioButton widget )
    Graph.setPlottingGraphNumber( GraphNumber )

    plotEigenfrequenciesPlate( Graph )


    # Depict coresponding lines based on the graph chosen by the user
    if (GraphNumber == 0):
        plotWaveSpeedGraph( Graph )

    if (GraphNumber == 1):
        plotWaveSpeedGraphWithLimits( Graph )

    if (GraphNumber == 2):
        plotModesInBand( Graph )

    if (GraphNumber == 3):
        plotModalDensity( Graph )

    if (GraphNumber == 4):
        plotModalOverlapFactor( Graph )

    if (GraphNumber == 5):
        plotMaximumElementSize( Graph )


def updateMode( ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                WarningMessage,
                Graph,
                Properties ):


    WarningMessage.clean( )
    Graph.setMode( Properties )

    cangeMode( ElasticModulus,
               ShearModulus,
               PoissonRatios,
               MaterialProperties,
               GeometryProperties,
               WarningMessage,
               Graph.getMode() )


def cangeMode( ElasticModulus,
               ShearModulus,
               PoissonRatios,
               MaterialProperties,
               GeometryProperties,
               WarningMessage,
               Mode ):


    if ( Mode == 1 ):

        UniformValue = ElasticModulus.getValue( 0, 0 )
        ElasticModulus.setValue( 0, 1, UniformValue )
        ElasticModulus.setValue( 0, 2, UniformValue )

        UniformValue = str( ElasticModulus.getFloatValue( 0, 0 ) \
                            / ( 2.0 * (1.0 + PoissonRatios.getFloatValue( 0, 0 ))) )
        ShearModulus.setValue( 0, 0, UniformValue )
        ShearModulus.setValue( 0, 1, UniformValue )
        ShearModulus.setValue( 0, 2, UniformValue )

        UniformValue = PoissonRatios.getValue( 0, 0 )
        PoissonRatios.setValue( 0, 1, UniformValue )
        PoissonRatios.setValue( 0, 2, UniformValue )

        try:
            testInputData( Mode, PoissonRatios.getData() )
        except DataCorrupted as Error:
            WarningMessage.printMessage( str( Error ) )



    if ( Mode == 0 ):
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

    PoissonRatios.assignValue( 1, 0, str( round(Temp,5) ) )

    # update value of nu_31
    Temp = PoissonRatios.getFloatValue( 0, 1 ) * ElasticModulus.getFloatValue( 0, 2 ) \
           / ElasticModulus.getFloatValue( 0, 0 )
    PoissonRatios.assignValue( 1, 1, str( round(Temp,5) ) )

    # update value of nu_32
    Temp = PoissonRatios.getFloatValue( 0, 2 ) * ElasticModulus.getFloatValue( 0, 2 ) \
           / ElasticModulus.getFloatValue( 0, 1 )

    PoissonRatios.assignValue( 1, 2, str( round(Temp,5) ) )


def setDeafultSettings( ElasticModulus,
                        ShearModulus,
                        PoissonRatios,
                        MaterialProperties,
                        GeometryProperties,
                        Graph,
                        WarningMessage ):

    WarningMessage.clean()

    ElasticModulus.resetByDefault( )
    ShearModulus.resetByDefault( )
    PoissonRatios.resetByDefault( )

    updateData( ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Graph,
                WarningMessage )


    # DEBUGGING
    #cangeMode( ElasticModulus,
    #           ShearModulus,
    #           PoissonRatios,
    #           MaterialProperties,
    #           GeometryProperties,
    #           Graph.getMode() )


main( )
