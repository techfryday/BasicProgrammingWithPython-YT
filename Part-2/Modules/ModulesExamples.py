""" # Import module
import Calculator
print(Calculator.add(12,23)) """

""" # From module import components
from Calculator import add, sub
print(add(12,12))
print(mult(12,23)) """

""" # From module import everything
from Calculator import *
print(add(12,23)) """

""" # Import as
import Calculator as calc
print(calc.add(12,34)) """

""" # From module import components as
from Calculator import mult as calc
print(calc(12,23)) """

# -----------------------------------------------------

""" # Importing modules from packages
from Calculations import Scientific, Simple
print(Scientific.areaOfCircle(12)) """

# Importing * From a package
from Calculations import *
print(Simple.mult(12,12))

""" # Importing components from module withing a package
from Calculations.Simple import add, mult
print(mult(10,10)) """