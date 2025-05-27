import numpy as np

def maximum_temperature(sol, verbose = False):

    #Identifico la máxima temperatura
    max_temp_index = np.argmax(sol.y[2])
    max_temp_value = sol.y[2][max_temp_index]

    if verbose:    
        print("Maximum temperature index:", max_temp_index)
        print("Maximum temperature value:", max_temp_value)

    return max_temp_index, max_temp_value