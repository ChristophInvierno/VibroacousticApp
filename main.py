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


# Link custom files
from LatexSupport import LatexLabel
from UnicodeSymbols import *
from Helper import Flag

# TODO: change the name of the module
from InteractiveTable import InteractiveTable


def main():
    # the main function only describes both graphical and comunication
    # of the app.


    #========================== GRAPHICAL PART =================================

    # CREATE ALL PLOTS:
    Input = figure( title = "",
                    tools = "",
                    width = 500,
                    height = 500 )


    Graph = figure( title = "",
                    tools = "",
                    x_range = (-7, 7),
                    y_range = (-1, 30),
                    width = 650,
                    height = 550 )


    # CREATE TABLES:
    # ........................ Elastic Modulus table ...........................
    ELASTIC_MODULUS_TITEL = Div(text = """ELASTIC MODULUS:""")
    ElasticModulus = InteractiveTable( 1, 3 )
    ElasticModulus.setTitels( [ [EMODUL_X, EMODUL_Y, EMODUL_Z] ] )
    ElasticModulus.setValues( [ ["1.061e10", "7.605e08", "3.667e08"] ] )


    # ........................ Shear Modulus table .............................
    SHEAR_MODULUS_TITEL = Div(text = """SHEAR MODULUS:""")
    ShearModulus = InteractiveTable( 1, 3 )
    ShearModulus.setTitels( [ [ EMODUL_XY, EMODUL_XZ, EMODUL_YZ ] ] )
    ShearModulus.setValues( [ [ "6.900e08", "1.725e08", "9.857e07" ] ] )


    # ........................ Poisson’s ratios ................................
    POISSON_RATIO_TITEL = Div(text = """POISSON'S RATIOS:""")
    PoissonRatios = InteractiveTable(2, 3)
    PoissonRatios.setTitels( [ [ POISSON_RATIO_XY,
                                 POISSON_RATIO_XZ,
                                 POISSON_RATIO_YZ ],
                               [ POISSON_RATIO_YX + "\t( auto )",
                                 POISSON_RATIO_ZX + "\t( auto )",
                                 POISSON_RATIO_ZY + "\t( auto )"] ])

    PoissonRatios.setValues([["1.184", "1.771", "0.382"],
                                  ["0.085", "0.061", "0.184"]])


    # ........................ Material Properties table .......................
    MATERIALS_TITEL = Div(text="""MATERIAL PROPERTIES:""")
    MaterialProperties = InteractiveTable(1, 2)
    MaterialProperties.setTitels( [ [ "Density" , "Loss Factor"] ] )
    MaterialProperties.setValues( [ ["450.0", "0.012"] ] )


    # ........................ Geometry table .......................
    GEOMETRY_TITEL = Div(text="""GEOMETRY:""")
    GeometryProperties = InteractiveTable(1, 3)
    GeometryProperties.setTitels( [ [ "Length", "Width", "Thickness"] ] )
    GeometryProperties.setValues( [ ["2.5", "3.0", "0.081"] ] )


    # CREATE BUTTONS:
    ApplyButton = Button( label = "Apply",
                          button_type = "success",
                          width = 100)


    PrintReport = Button( label = "Print Report",
                          button_type = "success",
                          width = 100 )


    ModeRadioButtons = RadioButtonGroup( labels = [ "Homogeneous mode",
                                                    "Non-Homogeneous mode" ],
                                     width = 500,
                                     active = 0 )


    GraphRadioButtons = RadioButtonGroup( labels = [ "Wave speed",
                                                     "Modes in Band",
                                                     "Modal Overlap Factor",
                                                     "Natural Frequencies",
                                                     "Limit frequencies",
                                                     "Wavelength - element size for FEM"],
                                     width = 500,
                                     active = 0 )


    # SPECIFY THE LAYOUT:
    Buttons = row( row( Spacer( width = 185 ),
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
    # TODO: set up all call back function
    # 1: read information from the text input labels
    # 2: pass that information to the corresponding functions
    Mode = Flag( GraphRadioButtons.active )


    # set up the line on the plot
    Data = ColumnDataSource( data=dict( XData=[], YData=[] ) )
    Graph.line(x='XData',
               y='YData',
               source = Data)


    NUMBER_OF_FUNCTIONS = 6
    Functions = range(0, NUMBER_OF_FUNCTIONS)
    Arguments = range(0, NUMBER_OF_FUNCTIONS)

    # Set up callback function for RadioButtons (tags)
    ApplyButton.on_click( partial( updateData,
                                   Data,
                                   Graph,
                                   ElasticModulus,
                                   ShearModulus,
                                   PoissonRatios,
                                   MaterialProperties,
                                   GeometryProperties,
                                   Functions,
                                   Arguments,
                                   Mode ) )


    GraphRadioButtons.on_click( partial ( updateGraph,
                                          NUMBER_OF_FUNCTIONS,
                                          Arguments,
                                          Functions,
                                          Data ) )


    ModeRadioButtons.on_click( partial ( updateMode,
                                         ElasticModulus,
                                         ShearModulus,
                                         PoissonRatios,
                                         MaterialProperties,
                                         GeometryProperties,
                                         Mode ) )


    # ================= RUN SIMULATION WITH DEFAULT DATA =====================
    updateData( Data,
                Graph,
                ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Functions,
                Arguments,
                Mode )


    updateGraph ( NUMBER_OF_FUNCTIONS,
                  Arguments,
                  Functions,
                  Data,
                  1 )




    # DEPICT ALL WIDJETS
    curdoc().add_root( column( Spacer( height = 20 ),
                               row( RightSide,
                                    Spacer( width = 50 ),
                                    LeftSide ) ) )


#===============================================================================
#                               HELPER FUNCTIONS
#===============================================================================
def updateData( Data,
                Graph,
                ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Functions,
                Arguments,
                Mode ):


    # before calling user-define functions check mode one time
    cangeMode ( ElasticModulus,
                ShearModulus,
                PoissonRatios,
                MaterialProperties,
                GeometryProperties,
                Mode )


    ElasticModulusData = ElasticModulus.getData()
    ShearModulusData = ShearModulus.getData()
    PoissonRatiosData = PoissonRatios.getData()
    MaterialPropertiesData = MaterialProperties.getData()
    GeometryPropertiesData = GeometryProperties.getData()



    #TODO: call all user-specific functions and update functions and arguments
    # lists


def updateGraph( NUMBER_OF_FUNCTIONS,
                 Argument,
                 Functions,
                 Data,
                 GraphNumber ):

    Argument[ GraphNumber ] = [ 1, 2 ]
    Functions[ GraphNumber ] = [ 1, 2 ]
    #TODO: check lengths of two lists and raise an exeption if
    # the lengths are different
    #if len( Argument ) == len( FunctionOne ):

    Data.data = dict( XData = Argument[ GraphNumber ],
                      YData = Functions[ GraphNumber ] )


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

    if ( Mode.getFlag() == 1 ):
        UniformValue = ElasticModulus.getValue( 0, 0 )
        ElasticModulus.setValue( 0, 1, UniformValue )
        ElasticModulus.setValue( 0, 2, UniformValue )


        UniformValue = ShearModulus.getValue( 0, 0 )
        ShearModulus.setValue( 0, 1, UniformValue )
        ShearModulus.setValue( 0, 2, UniformValue )


        UniformValue = PoissonRatios.getValue( 0, 0 )
        PoissonRatios.setValue( 0, 1, UniformValue )
        PoissonRatios.setValue( 0, 2, UniformValue )

        #ElasticModulus.disableElement( 0, 1, ModeNumber )
        #ElasticModulus.disableElement( 0, 2, ModeNumber )

        #ShearModulus.disableElement(0, 1, ModeNumber)
        #ShearModulus.disableElement(0, 2, ModeNumber)

        #PoissonRatios.disableElement(0, 1, ModeNumber)
        #PoissonRatios.disableElement(0, 2, ModeNumber)

        #PoissonRatios.disableElement(1, 0, ModeNumber)
        #PoissonRatios.disableElement(1, 1, ModeNumber)
        #PoissonRatios.disableElement(1, 2, ModeNumber)


    if ( Mode.getFlag() == 0 ):
        ElasticModulus.restoreValue( 0, 1 )
        ElasticModulus.restoreValue( 0, 2 )

        ShearModulus.restoreValue( 0, 1 )
        ShearModulus.restoreValue( 0, 2 )

        PoissonRatios.restoreValue( 0, 1 )
        PoissonRatios.restoreValue( 0, 2 )



main()