# Link bokeh libraries
from bokeh.plotting import figure
from bokeh.layouts import column, row, Spacer
from bokeh.io import curdoc
from bokeh.models import Slider, Button, Div, Arrow, OpenHead, Label, Plot
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Text

# Link third-party python libraries
from math import cos, sin, radians, sqrt, pi, atan2

# Link custom files
from LatexSupport import LatexLabel


def main():
    fig = figure( title = "",
                  tools = "",
                  x_range = (-7, 7),
                  y_range = (-1, 30),
                  width = 350,
                  height = 500 )


    curdoc().add_root( column( fig ) )


main()