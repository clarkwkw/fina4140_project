import numpy as np
from scipy.special import erf

def bs_formula(s, e, r, q, sigma, tau, call_or_put):
	if call_or_put not in ["call", "put"]:
		raise Exception("call_or_put must be either 'call' or 'put'")

	if tau > 0:
		d1 = (np.log(s/e) + (r - q + 0.5*sigma*sigma)*tau)/(sigma*np.sqrt(tau))
		d2 = d1 - sigma*np.sqrt(tau)

		if call_or_put == "call":
			n1 = 0.5*(1+erf(d1/np.sqrt(2)))
			n2 = 0.5*(1+erf(d2/np.sqrt(2)))
			c = s*np.exp(-1*q*tau)*n1-e*np.exp(-1*r*tau)*n2
			return c
		else:
			n1 = 0.5*(1+erf(-d1/np.sqrt(2)))
			n2 = 0.5*(1+erf(-d2/np.sqrt(2)))
			p = e*np.exp(-1*r*tau)*n2-s*np.exp(-1*q*tau)*n1
			return p
	else:
		if call_or_put == "call":
			return max(s-e, 0)
		else: 
			return max(e-s, 0)


if __name__ == "__main__":
	s = 150.07
	r = 0.03
	sigma = 0.2494361491753742
	tau = 1
	print(bs_formula(s, s, r, 0, sigma, tau, "call"))
	print(bs_formula(s, 1.1*s, r, 0, sigma, tau, "call"))
	print(bs_formula(s, 1.1*s, r, 0.01, sigma, tau, "call"))
	print(bs_formula(s, 0.9*s, r, 0, sigma, tau, "call"))
	print(bs_formula(s, s, r, 0, sigma, tau, "put"))
	print(bs_formula(s, 1.1*s, r, 0, sigma, tau, "put"))
	print(bs_formula(s, 1.1*s, r, 0.01, sigma, tau, "put"))
	print(bs_formula(s, 0.9*s, r, 0, sigma, tau, "put"))