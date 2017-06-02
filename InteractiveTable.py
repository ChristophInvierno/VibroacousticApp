from bokeh.layouts import widgetbox
from bokeh.models.widgets import TextInput
from bokeh.layouts import column, row, Spacer

from copy import deepcopy

class InteractiveTable:
    def __init__( self, Rows, Columns ):
        self.__Rows = Rows
        self.__Column = Columns
        self.__Instance = TextInput(value="200e9", title="Exx:", width=200)
        self._breedTable()

    def _breedTable(self):
        self.__Labels = []

        for i in range( 0, self.__Rows ):
            Temp = []
            for j in range( 0, self.__Columns ):
                Temp.append( deepcopy( self.__Instance ) )
            self.__Labels.append( Temp )


