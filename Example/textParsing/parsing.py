import numpy as np
from copy import deepcopy
import re
from Werte_Ausgangsmaterial_CiE170111_variable_layers import Werte_Ausgangsmaterial_CiE170111_variable_layers

class WrongLayersThikness(Exception):
    pass



def main():
    #TestParseString( )

    try:

        Layers = getLayersFromString("0.2 0.6 0.1")

    except WrongLayersThikness as Error:
        print Error

    except:
        print "Error: Unexpected error. Please, refer to the code." \
              "function: checkString( aString )"

    print "LAYERS:", Layers
    print "NUMBER OF LAYERS:", len( Layers )

    E = [ 1.061e10, 7.605e08, 3.667e08 ]
    G = [ 6.900e08, 1.725e08, 9.857e07 ]
    D = Layers
    nu = [ [ 1.184, 1.771, 0.382 ], [ 0.08487, 0.06121, 0.18419 ] ]

    Data = Werte_Ausgangsmaterial_CiE170111_variable_layers( E, G, D, nu )

    print
    print Data[ 0 ]
    print Data[ 1 ]
    print Data[ 2 ]
    print Data[ 3 ]


def getLayersFromString( aString ):

    LayersThickness = parseString( aString )
    checkLayerConsistency( LayersThickness )
    Layers = mirrorLayers( LayersThickness )

    return Layers

def TestParseString():

    TestCases = generateTests()

    for aCase in TestCases:
        try:
            LayersThickness = parseString( aCase )
            checkLayerConsistency( LayersThickness )
            Layers = mirrorLayers( LayersThickness )
            print "RIGHT: ", LayersThickness, "INPUT:", aCase, "RESULT:", Layers

        except WrongLayersThikness as Error:
            print "WRONG: ", Error, aCase

        except:
            print "Error: Unexpected error. Please, refer to the code." \
                  "function: checkString( aString )"


def parseString( aString ):
    DILIMETERS = [';','|']
    EMPTY_STRING = ''

    Words = aString.split()

    # Go through all dilimeters and parse whatever it's possible to parse
    for Dilimeter in DILIMETERS:
        TempDictionary = []

        for aWord in Words:
            TempList = aWord.split( Dilimeter )

            for Element in TempList:
                if Element != EMPTY_STRING:
                    TempDictionary.append( Element )

        Words = TempDictionary

    # try to cast all words to floats. Catch and process the error if it's possible
        LayersThickness = []
    try:
        for aWord in Words:
            LayersThickness.append( float(aWord) )

    except:
        raise WrongLayersThikness( "The data format for the layers thikness is wrong. "
                                  "Please, refer to the documentation" )

    return LayersThickness

def checkLayerConsistency( Layers ):

    for Layer in Layers:
        if Layer < 0.0:
            raise WrongLayersThikness("The thickness of one of the layers "
                                      "has its negative value")
        if Layer == 0.0:
            raise WrongLayersThikness("The thickness of one of the layers "
                                      "is eqaul to zero" )

    pass

def mirrorLayers( TopLayers ):

    nTopLayers = len( TopLayers )
    if nTopLayers == 1:
        # Return the input data if there is only one layer
        return TopLayers

    nLayers = 2 * ( nTopLayers -1 ) + 1
    Layers = [ 0.0 ] * nLayers

    for i in range( nTopLayers ):
       Layers[ i ] = TopLayers[ i ]
       Layers[ -1 - i ] = TopLayers[ i ]

    return Layers

def generateTests():
    TestCases = [ ]
    TestCases.append( "0.5" )
    TestCases.append( "0.5 0,5" )
    TestCases.append( "0.5 0.2 0.232 0.44 0.235" )
    TestCases.append( "0.5; 0.2 .44 0.235" )
    TestCases.append( "0.5 ;0.2 ;0.44; 0.235" )
    TestCases.append( "0.s 0.2 0.44 0.235" )
    TestCases.append( "0.0 0.0 0.0 0.1" )
    TestCases.append( "i don't know what to write down" )
    TestCases.append( "0.20 0,18 0.1 0,01" )
    TestCases.append( "0.20 0.18 -0.1 0.01" )
    TestCases.append( "0,2" )
    TestCases.append( "01.2 0.18" )
    TestCases.append( "0.2.0 0.18" )

    return TestCases

main()
