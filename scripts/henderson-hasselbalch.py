def protonated_f(r):
    '''Returns the fraction protonated for the given R'''
    prot_frac = 1 / (1 + r)
    return(prot_frac)

def deprotonated_f(r):
    '''Returns the fraction deprotonated for the given R'''
    deprot_frac = 1 - protonated_f(r)
    return(deprot_frac)

def hh_r(pH, pKa):
    '''Returns R from the Henderson-Hasselbalch equation'''
    r = 10 ** (pH - pKa)
    return(r)
