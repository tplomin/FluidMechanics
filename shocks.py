import numpy as np

def idealGas(R, P=0, rho=0, T=0):
    """
    Solve ideal gas equations 
    P = rho R T
    """
    if (P == 0):
        return rho * R * T
    elif (rho == 0):
        return P / (R * T)
    else:
        return P / (rho * R)

def speedOfSound(gamma, R, T):
    """
    Weak Isentropic Wave
    """
    return np.sqrt(gamma* R * T)



