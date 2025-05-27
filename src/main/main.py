##########################
# SIMULACIÓN EJEMPLO
##########################
import numpy as np

#Import functions from fun_differential_equations
from src.lib import fun_differential_equations #Esta
from src.lib.fun_differential_equations import fun

#Import parameters
from src.main.parameters import T_AMB, PATM

#Initial conditions
R0 = 1e-3
RDot0 = 0.
T0 = T_AMB
a0 = 1e-5
aDot0 = 0.

#Pressure parameters
A_ps = np.array([1.])
f_ps = np.array([1e3])
d_ps = np.array([0.])

# Amp_limits = [0,PATM]
# freq_limits:tuple[float] = (1e3,2e6)


#Simulation parameters
t_fin = 1e-3



#arguments of fun
ps_argument = [A_ps, f_ps, d_ps]
y0 = [R0, RDot0, T0, a0, aDot0]  # Initial conditions

#Imprimo tipos de datos
for i, arg in enumerate(ps_argument):
    print(f"Argument {i}: {type(arg)}")
for i, arg in enumerate(y0):
    print(f"y0[{i}]: {type(arg)}")

fun(0.,y0,ps_argument)

print(fun(0,y0,ps_argument))