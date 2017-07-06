class Flag:
    """ This class is created to make built-in python variables to be mutable"""

    def __init__( self, Input ):
        self.__Value = Input

    def getFlag(self):
        return self.__Value


    def setFlag(self, Input ):
        self.__Value = Input
