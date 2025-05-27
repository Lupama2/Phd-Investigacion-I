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

#Resuelvo fun con solve_ivp
from scipy.integrate import solve_ivp

sol = solve_ivp(fun, [0, t_fin], y0, args=(ps_argument,), method='RK45', rtol
=1e-6, atol=1e-9)
# Print the solution
print("Time points:", sol.t)

#Plot
from src.utility.graphics import plot_results

#Creo arrays A_ps_array que tiene el mismo tamaño que sol.t. Recordemos que A_ps ya es un numpy array
# A_ps_array = np.tile(A_ps, (len(sol.t), 1)).T[0].tolist()
# f_ps_array = np.tile(f_ps, (len(sol.t), 1)).T[0].tolist()
# d_ps_array = np.tile(d_ps, (len(sol.t), 1)).T[0].tolist()

# print("A_ps_array:", A_ps_array)

# #Imprimo tipos de datos
# print("Type of A_ps_array:", type(A_ps_array))
# print("Type of f_ps_array:", type(f_ps_array))
# print("Type of d_ps_array:", type(d_ps_array))

plot_results(sol, A_ps, f_ps, d_ps)