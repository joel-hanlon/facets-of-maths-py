import matplotlib.pyplot as plt
import numpy as np
import math
from functions import *

arithmetic = methodOfCalculation(calcArMean)
geometric = methodOfCalculation(calcGeoMean)
exact = methodOfCalculation(calcExact)


plt.plot(arithmetic.perimeters[:,0], arithmetic.perimeters[:,1])
plt.ylabel("Perimeter of Ellipse")
plt.xlabel("Ratio of a to b")
plt.grid()
plt.show()