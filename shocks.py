import numpy as np
pi = np.pi

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

def p_ratio(gamma, m1, beta = pi/2):
    """
    Pressure ratio across the shock
    """
    m1n = m1*np.sin(beta)
    return 1 + 2 * gamma / (gamma + 1) * (m1n**2 - 1) 

def rho_ratio(gamma, m1n, beta = 90):
    """
    Density ratio across the shock
    """
    return (gamma  + 1)*m1n**2 / (2 + (gamma - 1 )*m1n**2)

def u_ratio(gamma, m1n, beta = 90):
    """
    Velocity ratio across the shock
    """
    return 1 / rho_ratio(gamma, m1n)

def t_ratio(gamma, m1n, beta = 90):
    """
    Temperature ratio across the shock
    """
    return p_ratio(gamma, m1n) / rho_ratio(gamma, m1n)

def m2n(gamma, m1n, beta = 0):
    num = m1n**2 + 2/(gamma-1)
    den = (2*gamma)/(gamma - 1) * m1n**2 - 1
    return np.sqrt( num / den )


