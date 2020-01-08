def evaluate_poly(poly, x): 
    """
    Computes the polynomial function for a given value x. Returns that value.
    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0) # f(x) = 7.0x4
     + 9.3x3
     + 5.0x2
    >>> x = -13
    >>> print evaluate_poly(poly, x) # f(-13) = 7.0(-13)4
     + 9.3(-13)3
     + 5.0(-13)2
    180339.9
    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # TO DO
    highestPower = len(poly)
    totalPolynomial = 0
    for i in range(0,highestPower):
        
        totalPolynomial += poly[i]*(x**i)

    
    return totalPolynomial

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).
    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0) # x4 + 3.0x3 + 17.5x2 - 13.39 
    >>> print compute_deriv(poly) # 4.0x3 + 9.0x2 + 35.0x 
    (0.0, 35.0, 9.0, 4.0)
    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    highestPower = len(poly)
    newPoly = ()
    for i in range(1,highestPower):
        
        deriv = poly[i]*i
        newPoly = newPoly + (deriv,)
    return newPoly

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required to
    get to the root.
    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0) #x4 + 3.0x3 + 17.5x2 - 13.39 
    >>> x_0 = 0.1 
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8)
    poly: tuple of numbers, length > 1.
    Represents a polynomial function containing at least one real root.
    The derivative of this polynomial function at x_0 is not 0.
    x_0: float 
    epsilon: float > 0
    returns: tuple (float, int)
    """

    iterations = 1
    testNum = evaluate_poly(poly,x_0)
    while abs(testNum) > abs(epsilon):
        print('testNum =',testNum)
        print('x_0 = ',x_0)
        iterations += 1
        effex = evaluate_poly(poly,x_0)
        effprimeex = evaluate_poly(compute_deriv(poly),x_0)
        x_0 -= (effex/effprimeex)
        testNum = evaluate_poly(poly,x_0)

    returnValue = (x_0,iterations)
    return returnValue





