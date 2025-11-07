import matplotlib.pyplot as plt
import numpy as np
import math
from functions import *

# want to read the values from matt parker csv file

class methodOfCalculation:
    resolution = 100
    ratiosUpTo = 20

    def __init__(self, calcPerimeter):
        self.calcPerimeter = calcPerimeter
        self.perimeters = setOfPerimeters(self.calcPerimeter, self.resolution, self.ratiosUpTo)

geometric = methodOfCalculation(calcGeoMean)
print(geometric.perimeters)

print(setOfPercentageErrors(geometric.perimeters))