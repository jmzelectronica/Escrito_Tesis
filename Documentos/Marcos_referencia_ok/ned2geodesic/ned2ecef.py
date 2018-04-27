
#Convierte de coordenadas ned a coordenadas ecef
import matplotlib.pyplot as plt
import numpy as np
import math
import csv
from os import path
from StringIO import StringIO
import time

#poligono a convertir en ned
ned = open("/home/lab-10/Documentos/Marcos_referencia_ok/ned2geodesic/poligono_cuatro/path_ned_torres/poli_10.ned", "r")
ned = ned.read()
Pned = np.genfromtxt(StringIO(ned))
dat = np.matrix(Pned)
x_north = (dat[:,0])
y_east = (dat[:,1])
z_down = 0.0

#coordenada de referencia del poligono a convertir en geodesico
Pe = open("/home/lab-10/Documentos/Marcos_referencia_ok/ned2geodesic/poligono_cuatro/home.poly", "r")
Pe = Pe.read()
Pe = np.genfromtxt(StringIO(Pe))
date = np.matrix(Pe)
lat0 = (date[0,0])
lon0 = (date[0,1])

#coordenada de referencia a convertir en ecef
Pref= open("/home/lab-10/Documentos/Marcos_referencia_ok/ned2geodesic/poligono_cuatro/poli_ecef/poli_10.txt", "r")
Pref = Pref.read()
Pref = np.genfromtxt(StringIO(Pref))
datos = np.matrix(Pref)
x_ref = (datos[0,0])
y_ref = (datos[0,1])
z_ref = (datos[0,2])

lamb = math.radians(lat0)
psi = math.radians(lon0)

#x_ref = -9.560539003510918701e+05 #   -5.940100940902681090e+06    2.116657993919685483e+06      
#y_ref = -5.940106948859045282e+06                                                                                                         
#z_ref = 2.116652715602948796e+06  

a = -math.sin(lamb) * math.cos(psi)
b = -math.sin(psi)
c = -math.cos(lamb) * math.cos(psi)
    
d = -math.sin(lamb) * math.sin(psi)
e = math.cos(psi)
f = -math.cos(lamb) * math.cos(psi)
    
g = math.cos(lamb)
h = -math.sin(lamb)

x_1 = a*x_north + b*y_east + c*z_down
y_1 = d*x_north + e*y_east + f*z_down
z_1 = g*x_north + h*z_down
x = x_1 + x_ref
y = y_1 + y_ref
z = z_1 + z_ref
ecef=np.array([x, y, z])
x=ecef[0,:]
y=ecef[1,:]
z=ecef[2,:]
g=np.concatenate((x,y,z),axis=1)
print g
np.savetxt('/home/lab-10/Documentos/Marcos_referencia_ok/ned2geodesic/poligono_cuatro/path_ned_torres/path_ecef/path_10.ecef', g , delimiter='    ')   # X is an array
plt.plot(x,y)
plt.show()
#plt.savefig('path_ned2ecef.png')


