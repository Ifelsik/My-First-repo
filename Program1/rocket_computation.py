def pressure_ratio(L,l,d,a):
	lambda_f=L/d
	lambda_c=(L-l)/d
	coef=(0.014*lambda_f*a)/(3+0.027*a*lambda_c)
	return coef
def mass_ratio(cm,L):
        return cm/L
def K_a(a):
        if 0<a<=4:
                return 22/30-1/30*a
        elif a<=10:
                return 0.6-1/60*(a-4)
def stb_pr(St, L):
        return St/L
def S(d):
        s = 0.4*d*d*K_a(a)*(mass_ratio(cm,L)+0.2-pressure_ratio(L,l,d,a))/(stb_pr(St, L)-0.2-mass_ratio(cm,L))
        return s
        
