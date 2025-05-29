

'''
Constantes y Cond Iniciales
'''
PATM = 98000.     # Pascals
T_AMB = 293.      # Kelvin
N = 6e15         # Num Particulas
NA = 6.022e23    # N Avogadro
KB = 1.38e-23    # J/K

NK = N * KB      # Precomputed constant

# Van der Waals constants (Redefinidas)
A = (N/NA)**2 * 0.137295  # Pa m^6
B = (N/NA) * 3.201e-5     # m^3

# Other physical constants
RHO_AGUA = 1000          # kg/m^3
VISCOSIDAD = 0.001       # Pa*s == kg/s
VISCOSIDAD_K = 1.002e-6  # m^2/s
S_SUP = 7e-2             # N/m
C_INF = 1500             # m/s
