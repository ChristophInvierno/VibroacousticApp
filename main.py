# Link bokeh libraries
from bokeh.plotting import figure
from bokeh.layouts import column, row, Spacer
from bokeh.io import curdoc, show
from bokeh.models import Div, Label, Plot
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Text
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider
from bokeh.models.widgets import TextInput, AutocompleteInput


from bokeh.layouts import widgetbox

from copy import deepcopy, copy

# Link third-party python libraries
from math import cos, sin, radians, sqrt, pi, atan2

# Link custom files
from LatexSupport import LatexLabel
from UnicodeSymbols import *

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
    ELASTIC_MODULUS_TITEL = Div(text="""ELASTIC MODULUS:""")
    ElasticModulus = InteractiveTable( 3, 3 )
    ElasticModulus.setTitels([[EMODUL_XX, EMODUL_XY, EMODUL_XZ],
                              [EMODUL_YX, EMODUL_YY, EMODUL_YZ],
                              [EMODUL_ZX, EMODUL_ZY, EMODUL_ZZ]])

    ElasticModulus.setValues([["200e9", "200e9", "200e9"],
                              ["200e9", "200e9", "200e9"],
                              ["200e9", "200e9", "200e9"]])


    # ........................ Stress Modulus table ............................
    STRESSES_TITEL = Div(text="""STRESSES:""")
    StressCoefficients = InteractiveTable(3, 3)
    StressCoefficients.setTitels([[ SIGMA_XX, SIGMA_XY, SIGMA_XZ],
                                  [ SIGMA_YX, SIGMA_YY, SIGMA_YZ],
                                  [ SIGMA_ZX, SIGMA_ZY, SIGMA_ZZ]])

    StressCoefficients.setValues([["150", "150", "150"],
                                  ["150", "150", "150"],
                                  ["150", "150", "150"]])


    # ........................ Material Properties table .......................
    PROPERTIES_TITEL = Div(text="""MATERIAL PROPERTIES:""")
    MaterialProperties = InteractiveTable(1, 2)
    MaterialProperties.setTitels([[ "Dumping", "Density"]])
    MaterialProperties.setValues([["2.0", "7850"]])


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


    GraphRadioButtons = RadioButtonGroup( labels = [ "Option 1",
                                                     "Option 2",
                                                     "Option 3",
                                                     "Option 4",
                                                     "Option 5"],
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
                        STRESSES_TITEL,
                        StressCoefficients.Table,
                        PROPERTIES_TITEL,
                        MaterialProperties.Table )
    LeftSide = column( GraphRadioButtons, Graph, Buttons )


    # ========================= COMMUNICATION PART =============================
    # TODO: set up all call back function
    # 1: read information from the text input labels
    # 2: pass that information to the corresponding functions



    # DEPICT ALL WIDJETS
    curdoc().add_root( column( Spacer( height = 20 ),
                               row( RightSide,
                                    Spacer( width = 50 ),
                                    LeftSide ) ) )


main()