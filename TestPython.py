#!/usr/bin/env python3

## TestPython.py -- Writen by Bradley Claus
## usage: ./TestPython.py <precicion> <y-value>
##

##
##  Exit codes:
##          0: All is fine
##          -1: Error: in calculate, parameters are NaN
##          -2: Error: no parameters given to script
##          -3: Warrning: varibles given on the command line are garbage
import sys
import math
import cmath
import decimal

def eval_equation(x, g, i):
    equ = decimal.Decimal(g) * decimal.Decimal((1/(10**i)))
    return (x + equ)**(x + equ)
    pass

def calculate(user_precicion, user_yvalue):

    x = 0
    g = 9
    i = 0

    if math.isnan(user_precicion) | math.isnan(user_yvalue):
        print ("Non-Number passed to calculate...exiting")
        sys.exit(-1)

    
    while ( i <= user_precicion):
        result = eval_equation(x, g, i)
        if result >= user_yvalue:
            g -= 1
        else:
            x = decimal.Decimal( x + decimal.Decimal(g*(1/10**i)))
            i += 1
            g = 9

    print ("X -> {0}".format(x))
    pass

def main(argv):
    if len(argv) == 1:
        print ("Incorrect usage!")
        print ("<script> <precision> <y>");
        print ("Current count: {0}".format(len(argv)))
        sys.exit(-2)

    print ("Current count: {0}".format(len(argv)))
    for index in range(len(argv)):
        tu = (index, argv[index])
        print ("argv[{0}] = {1}".format(*tu))

    try:
        user_precicion = int(argv[1]) + 1;
        user_yvalue = decimal.Decimal(argv[2])
    except decimal.InvalidOperation as e:
        print (e)
        print ("Invalid input given as script parameters")
        print ("Exiting...")
        sys.exit(-3)

    decimal.getcontext().prec = (user_precicion + 1)
    calculate(user_precicion, user_yvalue)
    
    print ("Done!")
    pass

if __name__ == "__main__":
    main(sys.argv)
