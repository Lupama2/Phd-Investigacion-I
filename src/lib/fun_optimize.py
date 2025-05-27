# In this script I define the functions to optimize
import numpy as np
from scipy.integrate import solve_ivp


#Import functions
from src.lib.fun_differential_equations import fun
from src.utility.graphics import plot_results
from src.lib.fun_identification import maximum_temperature
from src.lib.fun_identification import instability



#Import parameters
from src.main.parameters import T_AMB

def optimize_pressure(A_ps, f_ps, plot = False, verbose = False):

    #Convierto a listas
    A_ps = np.array([A_ps])
    f_ps = np.array([f_ps])

    #Asigno fase
    d_ps = np.array([0.])

    #Initial conditions (directamente del código de Nicolás)
    R0 = 1e-3
    RDot0 = 0.
    T0 = T_AMB
    a0 = 1e-5
    aDot0 = 0.

    #Simulation parameters
    t_fin = 1e-3

    #arguments of fun
    ps_argument = [A_ps, f_ps, d_ps]
    y0 = [R0, RDot0, T0, a0, aDot0]  # Initial conditions

    sol = solve_ivp(fun, [0, t_fin], y0, args=(ps_argument,), method='RK45', rtol
    =1e-6, atol=1e-9)

    if plot:
        fig, ax = plot_results(sol, A_ps, f_ps, d_ps)
        #Save plot
        fig.savefig("data/outputs/summarize_plot.png", dpi=300)



    # Identify the maximum temperature in the solution
    max_temp_index, max_temp_value = maximum_temperature(sol, verbose)

    # Identify instability in the solution
    instability_index, instability_value, instability_bool = instability(sol, verbose)

    return max_temp_value, instability_bool
