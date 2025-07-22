from math import radians, sin, cos, sqrt, atan2
import numpy as np

def Haversine(Latitud1, Latitud2, Longitud1, Longitud2):
    arcsin = np.arcsin(sqrt(pow(sin(radians(Latitud2 - Latitud1) / 2), 2) +
                           cos(radians(Latitud1)) * cos(radians(Latitud2)) *
                           pow(sin(radians(Longitud2 - Longitud1) / 2), 2)))
    distance = 2 * 6371 * arcsin  # Radius of the
    
    return distance

Longitude1 = -70.762778
Longitude2 = -70.963794
Latitude1 = -34.151652
Latitude2 = -34.225633 
print(Haversine(Latitud1=Latitude1, Latitud2=Latitude2, Longitud1=Longitude1, Longitud2=Longitude2))