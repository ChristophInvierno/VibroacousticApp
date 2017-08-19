class Flag:
    """ This class is created to make built-in python variables to be mutable"""

    def __init__( self, Input ):
        self.__Value = Input

    def getFlag(self):
        return self.__Value


    def setFlag(self, Input ):
        self.__Value = Input


class DataCorrupted(Exception):
    pass


def testInputData( Mode, Nu):

    if ( Mode == 0 ):
        # Checking criteria for stability all values must be positive
        FirstTerm = Nu[ 0 ][ 0 ] * Nu[ 1 ][ 0 ]
        SecondTerm = Nu[ 0 ][ 1 ] * Nu[ 1 ][ 1 ]
        ThirdTerm = Nu[ 0 ][ 2 ] * Nu[ 1 ][ 2 ]
        FourthTerm = 2.0 * Nu[ 0 ][ 0 ] * Nu[ 0 ][ 2 ] * Nu[ 1 ][ 1 ]

        CheckOne = 1 - FirstTerm
        CheckTwo = 1 - SecondTerm
        CheckThree = 1 - ThirdTerm
        CheckFour = 1 - FirstTerm - SecondTerm - ThirdTerm - FourthTerm

        if CheckOne < 0 or CheckTwo < 0 or CheckThree < 0 or CheckFour < 0:
            raise DataCorrupted("The material property is not feasible")

    if (Mode == 1):

        Threshold = 0.49

        if Nu[ 0 ][ 0 ] > Threshold or Nu[ 0 ][ 1 ] > Threshold or Nu[ 0 ][ 2 ] > Threshold:
            raise DataCorrupted("The material property is not feasible.</p>"
                                "<p> Current mode: ISOTROPIC; Threshold: 0.49 </p>"
                                "<p> Change: POISSON'S RATIOS VALUE")
        pass