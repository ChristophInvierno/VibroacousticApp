# Link bokeh libraries
from bokeh.plotting import figure
from bokeh.layouts import column, row, Spacer
from bokeh.io import curdoc, show
from bokeh.models import Div, Label, Plot
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Text
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, TextInput, AutocompleteInput
from bokeh.layouts import widgetbox

from copy import deepcopy

# Link third-party python libraries
from math import cos, sin, radians, sqrt, pi, atan2

# Link custom files
from LatexSupport import LatexLabel


def main():

    # Create all Widgets
    Input = figure( title = "",
                    tools = "",
                    width = 500,
                    height = 500 )


    Graph = figure( title = "",
                    tools = "",
                    x_range = (-7, 7),
                    y_range = (-1, 30),
                    width = 500,
                    height = 500 )


    # add all text lebels
    # Elastic Modulus Matrix:
    ElasticModulus_XX = TextInput(value="200e9", title="Exx:", width=200)
    ElasticModulus_XY = TextInput(value="200e9", title="Exy:", width=200)
    ElasticModulus_XZ = TextInput(value="200e9", title="Exz:", width=200)
    ElasticModulus_X = row(ElasticModulus_XX,
                           ElasticModulus_XY,
                           ElasticModulus_XZ)


    ElasticModulus_YX = TextInput(value="200e9", title="Eyx:", width=200)
    ElasticModulus_YY = TextInput(value="200e9", title="Eyy:", width=200)
    ElasticModulus_YZ = TextInput(value="200e9", title="Eyz:", width=200)
    ElasticModulus_Y = row(ElasticModulus_YX,
                           ElasticModulus_YY,
                           ElasticModulus_YZ)


    ElasticModulus_ZX = TextInput(value="200e9", title="Ezx:", width=200)
    ElasticModulus_ZY = TextInput(value="200e9", title="Ezy:", width=200)
    ElasticModulus_ZZ = TextInput(value="200e9", title="Ezz:", width=200)
    ElasticModulus_Z = row(ElasticModulus_ZX,
                           ElasticModulus_ZY,
                           ElasticModulus_ZZ)


    ElasticModulus = column( ElasticModulus_X,
                             ElasticModulus_Y,
                             ElasticModulus_Z )




    # Declare all buttons
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


    Buttons = row( Spacer(width=175), column( ApplyButton, PrintReport ) )

    RightSide = column( ModeRadioButtons, ElasticModulus, Buttons )
    LeftSide = column( GraphRadioButtons, Graph )

    # depict all widgets
    curdoc().add_root( column( Spacer( height = 20 ),
                               row( RightSide, LeftSide ) ) )


main()