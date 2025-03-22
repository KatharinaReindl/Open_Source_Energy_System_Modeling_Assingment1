import math

#Calculation of the area (rectangular)
def area (a,b):
    area = a * b
    return area

#Calculation the number of moduls (size of one pv-module in m^2)
def numberModuls (area,m):
    numbers = math.floor(area/m)
    return numbers

#Calculation of the Pv-power (power of one module in Wp)
def pv_power (numbers,powerModul):
    power = powerModul * numbers
    return power

#Calculation of feed into the grid (example for one day)
def feed(generation,load):
    feed = max(0, generation - load)
    return feed