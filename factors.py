#p/f factor
def f_to_p(f, i, n):
    return (1/(1+i)**n)*f
#f/p factor
def p_to_f(p,i,n):
    return ((1+i)**n)*p
#a/f factor
def PMT(f, i, n):
    return f / ((1 + i)**n - 1) * i