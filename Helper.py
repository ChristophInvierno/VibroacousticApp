class Flag:
    def __init__( self, Input ):
        self.__Value = Input


    def __add__(self, Input ):
        self.__Value += Input


    def getFlag(self):
        return self.__Value


    def setFlag(self, Input ):
        self.__Value = Input