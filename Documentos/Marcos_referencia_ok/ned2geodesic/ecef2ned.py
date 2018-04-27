#Convierte de coordenadas en ecef a ned

import matplotlib.pyplot as plt
import numpy as np
import math
import csv
from StringIO import StringIO

#Coordenadas goedesicas de referencia del poligono a convertir

lat0 = 19.5013132374119 
lon0 = -99.1424844413996 
h0 = 2240

e = 0.0818#e = #la exentricidad del elipsoide
a = 6378137.0 #semimajor axis length a;
N = a/math.sqrt(1-e**2* math.sin(lat0)**2)

ecef = open("/home/lab-10/Documentos/Marcos_referencia_ok/ned2geodesic/poligono_cuatro/poli_ecef/poli_3_3.ecef", "r")
ecef = ecef.read()
Pecef= np.genfromtxt(StringIO(ecef))
dat = np.matrix(Pecef)

x = (dat[:,0])
y = (dat[:,1])
z = (dat[:,2])

#coordendas en ecef de referencia del poligono a convertir
x_ref = -9.559800915886955336e+05     
y_ref = -5.940173220521776006e+06                             
z_ref = 2.116489614004057832e+06       


x_ecef = x - x_ref
y_ecef = y - y_ref
z_ecef = z - z_ref
    
lamb = math.radians(lat0)
psi = math.radians(lon0)


a = -math.sin(lamb) * math.cos(psi)
b = -math.sin(lamb) * math.sin(psi)
c = math.cos(lamb)
d = -math.sin(psi)
e = math.cos(psi)
f = -math.cos(lamb) * math.cos(psi)
g = -math.cos(lamb) * math.sin(psi)
h = -math.sin(lamb)

ned_y = a*x_ecef + b* y_ecef + c*z_ecef
ned_x = d*x_ecef + e*y_ecef
ned_z = f*x_ecef + g*y_ecef + h*z_ecef


ned=np.array([ned_x, ned_y, ned_z])
east=ned[0,:]
north=ned[1,:]
down=ned[2,:]
g=np.concatenate((north,east,down),axis=1)
print g
plt.plot(ned[0,:],ned[1,:])
plt.show()
np.savetxt('/home/lab-10/Documentos/Marcos_referencia_ok/ned2geodesic/poligono_cuatro/poli_ned/poli_3_3.ned', g, delimiter='    ')   # X is an array
