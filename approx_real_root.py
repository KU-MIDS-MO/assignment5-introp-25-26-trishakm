def approx_real_root(coeffs, interval):
    
    def f(x):
        c0 = coeffs[0]
        c1 = coeffs[1]
        c2 = coeffs[2]
        c3 = coeffs[3]
        return c0 + c1*x + c2*x*x + c3*x*x*x

    a = interval[0]
    b = interval [1]
    
    if a >= b:
        print("enter values such that a < b")
        return None
    
    #endpoints
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        print("no root")
        return None

    if fa == 0:
        return a
    if fb == 0:
        return b

    for i in range(100000):
        median = (a + b) / 2
        fm = f(median)

        if abs(fm) < 1e-12 or (b - a) < 1e-9:       #stop condition
            return median

        if fa * fm < 0:
            b = median
            fb = fm
        else:
            a = median
            fa = fm

    return (a + b) / 2
    
    pass

coeffs = [1,0,0,1]
interval = (-2,1.75)

print(approx_real_root(coeffs, interval))

###task3

#Write a function `approx_real_root(coeffs, interval)` that:

#- receives a list `coeffs` of four numbers representing a cubic polynomial,starting with the 
#coefficient of the free term and finishing with the coefficient of x^3
#- receives a tuple `interval = (a, b)` with `a < b`,
#- assumes that **the polynomial has exactly one real root inside this interval**,
#- computes and returns a floating-point approximation of that root,
#- and ensures that the approximation is accurate to at least **1×10⁻⁹** in absolute error