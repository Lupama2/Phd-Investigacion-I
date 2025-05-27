##########################
# SIMULACIÓN EJEMPLO
##########################
import numpy as np

from src.lib.fun_optimize import optimize_pressure



#Pressure parameters
A_ps = 1.
f_ps = 1e3
# Amp_limits = [0,PATM]
# freq_limits:tuple[float] = (1e3,2e6)

# Call the optimization function
optimize_pressure(A_ps, f_ps)

#Uso Bayesian Optimization de Optuna para maximizar la temperatura máxima
import optuna
from src.main.parameters import PATM

def objective(trial):
    # Define the search space for the parameters, ambos log
    A_ps = trial.suggest_float('A_ps', 1, PATM, log=True)  # Pressure amplitude
    f_ps = trial.suggest_float('f_ps', 1e3, 2e6, log=True)  # Pressure frequency

    # Call the optimization function
    max_temp_value, instability_bool = optimize_pressure(A_ps, f_ps)

    # Return the maximum temperature value as the objective to maximize
    return max_temp_value

# Create a study object
study = optuna.create_study(direction="maximize")

# Optimize the objective function
study.optimize(objective, n_trials=10000, n_jobs=-1)

# Save study
import joblib
joblib.dump(study, 'data/outputs/study.pkl')

# Ejecutar nuevamente el mejor caso
best_params = study.best_params

max_temp_value, instability_bool = optimize_pressure(best_params['A_ps'], best_params['f_ps'], plot=True, verbose=True)