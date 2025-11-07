import numpy as np
import math

#e = math.sqrt(a**2 - b**2) / a

ellipseLengths = np.loadtxt('group-poster/ellipse-lengths.csv', 
                            skiprows = 1, 
                            delimiter = ',')

def infiniteSeries(a: float, b: int = 1) -> float:
    h = (a-b)**2 / (a+b)**2
    n = 0
    sumTonthTerm = 0
    nthTerm = 1
    while nthTerm > 1e-15:
        nthTerm = (((1/((2*n-1)*4**n))*math.comb(2*n, n))**2)*(h**n)
        sumTonthTerm = sumTonthTerm + nthTerm
        n += 1
    return sumTonthTerm

def calcExact(a: float, b: int = 1) -> float:
    return math.pi*(a+b) * infiniteSeries(a,b)

def calcArMean(a: float, b: int = 1) -> float:
    return 2*math.pi*((a+b)/2)

def calcGeoMean(a: float, b: int = 1) -> float:
    return 2*math.pi*(math.sqrt(a*b))

def calcSquareAr(a: float, b: int = 1) -> float:
    return 2*math.pi*(math.sqrt((a**2+b**2)/2))

def setOfPerimeters(calcPerimeter: function, resolution: int, ratiosUpTo: int):
    perimetersMatrix = np.array([1, calcPerimeter(1)])
    for index in range(((ratiosUpTo-1)*resolution)-1):
        ratio = ((index + 1) / resolution) + 1
        nextPerimeter = np.array([ratio, calcPerimeter(ratio)])
        perimetersMatrix = np.vstack((perimetersMatrix, nextPerimeter))
    return perimetersMatrix

def calcPercentageError(estimate: float, real: float) -> float:
    pError =  ((estimate - real) / real) * 100
    return pError


#it's starting at 1, then going the whole length from 0 to 1899, 
#don't want that, need it to start at 1, finish at 19.99
#1st entry should be ratio
def setOfPercentageErrors(inputMatrix, referenceMatrix = ellipseLengths):
    errorsMatrix = np.array([1, calcPercentageError(inputMatrix[0,1], referenceMatrix[0,1])])
    for index in range(len(inputMatrix)):
        nextError = np.array([index, calcPercentageError(inputMatrix[index, 1], referenceMatrix[index, 1])])
        errorsMatrix = np.vstack((errorsMatrix, nextError))
    return errorsMatrix


class methodOfCalculation:
    resolution = 100
    ratiosUpTo = 20

    def __init__(self, calcPerimeter):
        self.calcPerimeter = calcPerimeter
        self.perimeters = setOfPerimeters(self.calcPerimeter, self.resolution, self.ratiosUpTo)

    def percentageErrors(self):
        return None
    
#shi below this still in testing phase

def compatibleMatrix(inputMatrix, otherMatrix):
    combinedMatrix = np.array([1, inputMatrix[0,1], otherMatrix[0,1]])
    i = 0
    while i <= max(len(inputMatrix), len(otherMatrix)):
        print(i)
        i += 1
    return True

#exact = methodOfCalculation(calcExact)
#exactPerimeters = exact.perimeters()



if __name__ == '__main__':
    print("lol")

# When comparing this to Matt Parker's spreadsheet we're getting different values, 
# I assume because of all the floating point numbers.
# Maybe find a way to do this using sympy? may be highly inefficient