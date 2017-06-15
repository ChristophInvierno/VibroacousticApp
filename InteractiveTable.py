from bokeh.layouts import widgetbox
from bokeh.models.widgets import TextInput
from bokeh.layouts import column, row, Spacer

import numpy as np

class TableCorrupted(Exception):
    pass

from copy import deepcopy

class InteractiveTable:
    MINIMUM_WIDGET_HEIGHT = 1

    def __init__( self, Rows, Columns ):
        self.__nRows = Rows
        self.__nColumns = Columns

        self.__LableHeight = 65
        self.__LableWidth = 200

        self.__ModeCounter = np.zeros(( Rows, Columns ), dtype = int)

        self.__initWidgets()


    def __initWidgets(self):
        self.__Widgets = []

        # TODO: add comments
        Rows = []
        for i in range( self.__nRows ):
            TextLabels = []
            for j in range( self.__nColumns ):
                TextLabels.append( TextInput( value = "Default Value",
                                              title = "Default Titel",
                                              width = self.__LableWidth ) )

            self.__Widgets.append( TextLabels )
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


        # initilize buffers by default values
        self.__TitelBuffer = Titels

        for Row, i in zip( Titels, range( len( Titels ) ) ):
            for Entry, j in zip( Row, range( len( Row ) ) ):
                self.__Widgets[ i ][ j ].title = Titels[ i ][ j ]



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


        # initilize buffers by default values
        self.__ValueBuffer = Values
        self.__DefaultValues = Values


        for Row, i in zip( Values, range( len( Values ) ) ):
            for Entry, j in zip( Row, range( len( Row ) ) ):
                self.__Widgets[ i ][ j ].value = Values[ i ][ j ]



    def setValue( self, aRow, aColumn, Value ):

        if self.__ModeCounter[ aRow ][ aColumn ] == 0:
            self.__ValueBuffer[aRow][aColumn] = self.__Widgets[aRow][aColumn].value
            self.__TitelBuffer[aRow][aColumn] = self.__Widgets[aRow][aColumn].title
            self.__Widgets[aRow][aColumn].title += "\t( auto )"

        self.__Widgets[ aRow ][ aColumn ].value = Value
        self.__ModeCounter[ aRow ][ aColumn ] += 1


    def restoreValue( self, aRow, aColumn ):
        if self.__ModeCounter[ aRow ][ aColumn ] != 0:
            self.__Widgets[aRow][aColumn].value = self.__ValueBuffer[aRow][aColumn]
            self.__Widgets[aRow][aColumn].title = self.__TitelBuffer[aRow][aColumn]
            self.__ModeCounter[ aRow ][ aColumn ] = 0



    def getValue(self, aRow, aColumn ):
        return self.__Widgets[ aRow ][ aColumn ].value


    def getData( self ):

        Data = []
        for i in range( self.__nRows ):
            Temp = []

            for j in range( self.__nColumns ):
                try:
                    Temp.append( float( self.__Widgets[ i ][ j ].value ) )
                except ValueError:
                    self.__Widgets[ i ][ j ].value = self.__DefaultValues[ i ][ j ]
            Data.append( Temp )

        return Data


#    def disableElement(self, aRow, aColumn, Mode ):
#
#        if Mode == 1:
#            self.__Buffer[aRow][aColumn] = self.__Widgets[aRow][aColumn].value
#            self.__Widgets[ aRow ][ aColumn ].height = InteractiveTable.MINIMUM_WIDGET_HEIGHT
#
#        elif Mode == 0:
#            self.__Widgets[aRow][aColumn].value = self.__Buffer[aRow][aColumn]
#            self.__Widgets[aRow][aColumn].height = self.__LableHeight

