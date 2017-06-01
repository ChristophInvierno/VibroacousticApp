# Link bokeh libraries
from bokeh.plotting import figure
from bokeh.layouts import column, row, Spacer
from bokeh.io import curdoc
from bokeh.models import Div, Label, Plot
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Text
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider

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

    RightSide = column( ModeRadioButtons, Input, Buttons )
    LeftSide = column( GraphRadioButtons, Graph )
    curdoc().add_root( column( Spacer( height = 20 ),
                               row( RightSide, LeftSide ) ) )


main()