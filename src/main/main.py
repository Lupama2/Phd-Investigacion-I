# Investigacion 1
# 
# mail: pablo.chehade.villalba@gmail.com
# fecha: 2025/02/10
#
# Resuelvo una burbuja con RP y ec de energía para la temperatura
# Nomenclatura: y1 = R, y2 = dot(R), y3 = T

import numpy as np
from numpy import pi

#Parameters
rho_0 = 1101.8 #densidad del líquido en la superficie de la burbuja en [kg/m3] para agua D2O a Tinf=35+273.15. Lo copié del código de Gabriela. 
sigma = 0.07031 #Tensión superficial [N/m]. Valor obtenido del código de Gabriela
mu = 0.000869 #Viscosidad [Pa.s]. Valor obtenido del código de Gabriela
p_0 = 0.925*(101325) #Presión ambiente en el infinito en [Pa]. Son 0.925 atm correspondientes a Bariloche. Conversión: (atm)(101325 Pa/atm)
K = 1.380649e-23 #constante de Boltzmann [J/K], obtenida de NIST
N_A = 6.02214076e23 #Nro de avogadro [1/mol], obtenida de NIST}
R_GI = 8.3145 #Constante de los gases ideales. J mol^-1 K^-1. La saqué de Wikipedia


#Parameters to play with
n = 1e-8 #Nro de moles de Ar



def Vol(R):
    # Volumen de una esfera
    return 4/3*pi*R**3

def p_g(R, T):

    p = n*R_GI*T/Vol(R)

    return p



def derivative(t, y):

    #Desempaqueto variables
    y1, y2, y3 = y[0], y[1], y[2]

    dydt = np.empty(3)

    #Ecuacion de Rayleigh-Plesset
    dydt[1 - 1] = y2
    dydt[2 - 1] = 1/y1*( 1/rho_0*( p_g(y1,y3) - 2*sigma/y1 - 4*mu*y2/y1 - p_0 ) - 3/2*y2**2   )

    #Ecuación de la energía
    dydt[3 - 1] = -p_g(y1,y3)*y1**2*y2*8*pi/(3*K*n*N_A)

    return dydt


#Resuelvo el sistema de ecuaciones usando LSODA de scipy
from scipy.integrate import solve_ivp

#Condiciones iniciales
R0 = 1e-3 #Radio inicial en [m]
dot_R0 = 0 #Derivada del radio inicial en [m/s]
T0 = 35 + 273.15 #Temperatura inicial en [K]

y0 = [R0, dot_R0, T0]

#Tiempo de integración
t_ini = 0
t_fin = 1e-3

sol = solve_ivp(derivative, [t_ini, t_fin], y0, method = 'LSODA')

#Grafico
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 1, sharex=True)

#Disminuyo a cero la distancia entre los subplots
plt.subplots_adjust(wspace=0)

ax[0].plot(sol.t, sol.y[0])
ax[0].set_ylabel('R [m]')

ax[1].plot(sol.t, sol.y[1])
ax[1].set_ylabel('dR/dt [m/s]')

ax[2].plot(sol.t, sol.y[2])
ax[2].set_ylabel('T [K]')

plt.xlabel('t [s]')


plt.show()