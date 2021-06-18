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

def rho_ratio(gamma, m1, beta = pi/2):
    """
    Density ratio across the shock
    """
    m1n = m1*np.sin(beta)
    return (gamma  + 1)*m1n**2 / (2 + (gamma - 1 )*m1n**2)

def u_ratio(gamma, m1, beta = pi/2):
    """
    Velocity ratio across the shock
    """
    m1n = m1*np.sin(beta)
    return 1 / rho_ratio(gamma, m1n)

def t_ratio(gamma, m1, beta = pi/2):
    """
    Temperature ratio across the shock
    """
    m1n = m1*np.sin(beta)
    return p_ratio(gamma, m1n) / rho_ratio(gamma, m1n)

def m2(gamma, m1, theta = 0, beta = pi/2):
    """
    Mach number after the shock
    """
    m1n = m1*np.sin(beta)

    num = m1n**2 + 2/(gamma-1)
    den = (2*gamma)/(gamma - 1) * m1n**2 - 1
    m2n = np.sqrt( num / den )

    return m2n/np.sin(beta-theta)


