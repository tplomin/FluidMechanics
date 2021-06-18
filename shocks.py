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
    Weak Isentropic Wave (sound wave)
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
    Use for mach numbers greater than 1.3 and heat capacity ratio greater than 1
    """
    m1n = m1*np.sin(beta)

    num = m1n**2 + 2/(gamma-1)
    den = (2*gamma)/(gamma - 1) * m1n**2 - 1
    m2n = np.sqrt( num / den )

    return m2n/np.sin(beta-theta)

def thetaBetaM(g, theta, m, d = 1,angle="rad"):
    """
    Returns shock angle for given gamma, deflection angle, and Mach number

    Specify the angle you are using
    angle = 'rad' (default)
    angle = 'deg'
    returns angle you specify

    Specify the shock type
    Weak shock d = 1 (default)
    Strong shock d = 0
    """
    if angle == "deg":
        theta_r = theta*pi/180
    else:
        theta_r = theta
        
    l = np.sqrt((m**2-1)**2 - 3*(1 + (g-1)/2*m**2)*(1+(g+1)/2*m**2)*np.tan(theta_r)**2)
    x = 1/l**3*((m**2-1)**3-9*(1+(g-1)/2*m**2)*(1+(g-1)/2*m**2+(g+1)/4*m**4)*np.tan(theta_r)**2)
    tanbeta_n = m**2 - 1 + 2*l*np.cos((4*pi*d+np.arccos(x))/3)
    tanbeta_d = 3*(1+ (g-1)/2*m**2)*np.tan(theta_r)

    beta = np.arctan(tanbeta_n/tanbeta_d)

    if angle == "deg":
        return beta*180/pi
    else:
        return beta
