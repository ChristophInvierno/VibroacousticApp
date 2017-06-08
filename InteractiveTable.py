from bokeh.layouts import widgetbox
from bokeh.models.widgets import TextInput
from bokeh.layouts import column, row, Spacer

class TableCorrupted(Exception):
    pass

from copy import deepcopy

class InteractiveTable:
    def __init__( self, Rows, Columns ):
        self.__nRows = Rows
        self.__nColumns = Columns

        self.__LableWidth = 200
        self.__initWidgets()


    def __initWidgets(self):
        self._Widgets = []

        # TODO: add comments
        Rows = []
        for i in range( self.__nRows ):
            TextLabels = []
            for j in range( self.__nColumns ):
                TextLabels.append( TextInput( value = "Default Value",
                                              title = "Default Titel",
                                              width = self.__LableWidth) )
            self._Widgets.append( TextLabels )
            Rows.append( row( TextLabels ) )


        Columns = []
        for Row in Rows:
            Columns.append( Row )
        self.Table = column( Columns )


    def setTitels(self, Titels):

        # Check if the input data is consistent i.e.
        # check the number of rows and columns

        if ( len( Titels ) != self.__nRows ):
            raise TableCorrupted( "ERROR from setValues: wrong number of " +\
                                    "rows were passed")

        for Entry in Titels:
            if ( len(Entry) != self.__nColumns ):
                raise TableCorrupted( "ERROR from setValues: wrong number of " +\
                                       "columns were passed")


        for Row, i in zip( Titels, range( len( Titels ) ) ):
            for Entry, j in zip( Row, range( len( Row ) ) ):
                self._Widgets[ i ][ j ].title = Entry



    def setValues(self, Values):

        # Check if the input data is consistent i.e.
        # check the number of rows and columns


        if ( len( Values ) != self.__nRows ):
            raise TableCorrupted( "ERROR from setValues: wrong number of " +\
                                    "rows were passed")
        for Entry in Values:
            if ( len(Entry) != self.__nColumns ):
                raise TableCorrupted( "ERROR from setValues: wrong number of " +\
                                       "columns were passed")


        for Row, i in zip( Values, range( len( Values ) ) ):
            for Entry, j in zip( Row, range( len( Row ) ) ):
                self._Widgets[ i ][ j ].value = Entry