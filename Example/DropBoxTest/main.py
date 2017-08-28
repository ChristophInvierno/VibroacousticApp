from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select
from bokeh.io import curdoc
from bokeh.layouts import column
from functools import partial
from bokeh.plotting import figure
from bokeh.models.widgets import Button
from bokeh.models import Toggle, BoxAnnotation, CustomJS


from bokeh.plotting import ColumnDataSource

code = '''\
p1.xgrid = true
'''


def main():

    p1 = figure( plot_width = 300, plot_height = 300, name = 'plot' )
    ApplyButton = Button( label = "Apply",
                          button_type = "success",
                          width = 100 )


    curdoc().add_root( column(ApplyButton, p1)  )


def pr( Plot ):
    plotToRemove = curdoc( ).get_model_by_name( 'plot' )
    for i in dir(plotToRemove):
        print i

    curdoc( ).remove( plotToRemove )









def changeDropTwo( DropTwo, DropOneValue ):

    if DropOneValue == 1:
        DropTwo.update( options=["1"], value = 1, )

    elif DropOneValue == 3:
        DropTwo.update( options = [ "1", "2" ], value = 1, )

    elif DropOneValue == 5:
        DropTwo.update( options = [ "1", "2", "3" ], value = 1, )

    elif DropOneValue == 7:
        DropTwo.update( options = [ "1", "2", "3", "4" ], value = 1, )


main()