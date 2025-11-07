import matplotlib.pyplot as plt
import numpy as np
import math
from functions import *



arithmetic = methodOfCalculation(calcArMean)
geometric = methodOfCalculation(calcGeoMean)
exact = methodOfCalculation(calcExact)

print(arithmetic.resolution)
print(arithmetic.perimeters)