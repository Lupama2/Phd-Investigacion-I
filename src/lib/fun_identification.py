import numpy as np

def maximum_temperature(sol, verbose = False):

    #Identifico la máxima temperatura
    max_temp_index = np.argmax(sol.y[2])
    max_temp_value = sol.y[2][max_temp_index]

    if verbose:    
        print("Maximum temperature index:", max_temp_index)
        print("Maximum temperature value:", max_temp_value)

    return max_temp_index, max_temp_value

def instability(sol, verbose = False):
    # Identifico si la inestabilidad/radio llegó a la unidad

    instability_index = np.argmax(np.abs(sol.y[3] / sol.y[0]))
    instability_value = sol.y[3][instability_index] / sol.y[0][instability_index]
    
    if verbose:
        print(f"Instability index: {instability_index}\nValue: {instability_value}")

    if instability_value >= 1:
        instability_bool = True
        if verbose:
            print("Instability reached or exceeded the unit.")
    else:
        instability_bool = False
        if verbose:
            print("Instability did not reach the unit.")

    return instability_index, instability_value, instability_bool
        