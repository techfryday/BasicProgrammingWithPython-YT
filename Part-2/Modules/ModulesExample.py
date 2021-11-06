""" # Importing module and calling functions
import Calculator
print(Calculator.add(12,34))
 """
""" # Importing module as..
import Calculator as calc
print(Calculator.add(12,34)) """

""" # From <module_name> import <components>
from Calculator import add, mult, pi
print(add(12,34)) """

""" # From <module> import Everything
from Calculator import *
print(divi(12,6)) """

""" # From <PackageName> import <Modules>
from Calculations import Simple, Scientific
print(Simple.add(12,34)) """

""" # From <Package>.<Module> import <Components>
from Calculations.Simple import mult, divi
from Calculations.Scientific import *
print(areaOfCircle(10)) """

from Calculations import *
print(Scientific.areaOfRectangle(12,34))

