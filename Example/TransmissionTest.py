import numpy as np
import matplotlib.pyplot as plt

def main():
    SIZE = 10;

    Transmission = range( 2 )
    Transmission[ 0 ] = [ 0 ]*SIZE
    Transmission[ 1 ] = [ 0 ]*SIZE

    Transmission[ 0 ], Transmission[ 1 ] = foo()
    plt.plot( Transmission[ 0 ], Transmission[ 1 ] )
    plt.show()



def foo():
    Arg = [ i for i in range(10) ]
    Func = [ i**2 for i in range(10) ]

    return Arg, Func

main()