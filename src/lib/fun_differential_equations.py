import numpy as np
from numba import njit


#La estructura del repo es
#lib
#  - fun_differential_equations.py
#  - __init__.py
#main
#  - parameters.py
#  - __init__.py

#Import parameters
from ..main.parameters import PATM, T_AMB, N, NA, KB, NK, A, B, RHO_AGUA, VISCOSIDAD, VISCOSIDAD_K, S_SUP, C_INF

'''
P Acustica
'''
@njit(cache=True)
def ps(t:float, A:list[float], f:list[float], d:list[float]):
    """JIT-compiled version of pressure function"""
    r = 0.0
    for i in range(len(A)):
        r += A[i] * np.sin(2*np.pi * (t*f[i] + d[i]))
    return r

@njit(cache=True)
def psdot(t:float, A:list[float], f:list[float], d:list[float]):
    """JIT-compiled version of pressure derivative function"""
    r = 0.0
    for i in range(len(A)):
        if f[i] != 0:  # Fixed: was checking w != 0 instead of w[i]
            r += A[i] * (2*np.pi*f[i]) * np.cos(2*np.pi * (t*f[i] + d[i]))
    return r

'''
Eqs Diferenciales
'''
@njit(cache=True)
def fun(t, y, ps_args):
    """JIT-compiled version"""
    R, RDot, T, a, aDot = y
    A_ps, f_ps, d_ps = ps_args  # Unpack arguments
    
    # Precompute frequently used terms
    R_sq = R ** 2
    R_cu = R ** 3
    V = (4/3) * np.pi * R_cu
    V_sq = V ** 2

    alpha = RDot / C_INF
    C = V - B

    # Energy Conservation
    tDot = (2 * RDot / R) * (A / (NK * V) - T * V / C)

    # Rayleigh-Plesset
    term1 = (RDot ** 2) * (alpha - 3) / 2
    term2 = NK / C * (R * tDot / C_INF + T * (1 - alpha * (2 * V + B) / C))
    term3 = A / V_sq * (5 * alpha - 1)
    term4 = 2 * (S_SUP + 2 * VISCOSIDAD * RDot) / R
    term5 = (1 + alpha) * (PATM + ps(t, A_ps, f_ps, d_ps))
    term6 = R * psdot(t, A_ps, f_ps, d_ps) / C_INF
    
    denominator = (1 - alpha + 4 * VISCOSIDAD / (RHO_AGUA * C_INF * R)) * R

    RDotDot = (term1 + (term2 + term3 - term4 - term5 - term6) / RHO_AGUA) / denominator
    
    # Instabilities calculation
    f_max = np.max(f_ps)
    if f_max != 0:
        delta2 = 1 + 2 / R * min(np.sqrt(VISCOSIDAD_K / f_max), R / 4)
    else:
        delta2 = 3/2
    
    A2 = (-RDotDot * R_sq + 12 * S_SUP / RHO_AGUA + 8 * VISCOSIDAD_K * RDot * (3 - 2 / delta2)) / R_cu
    B2 = (3 * RDot * R - VISCOSIDAD_K * (24 + 32 / delta2)) / R_sq
    
    # Second order homogeneous ODE
    aDotDot = -B2 * aDot - A2 * a
    
    return np.array([RDot, RDotDot, tDot, aDot, aDotDot])