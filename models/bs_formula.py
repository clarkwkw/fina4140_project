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
			c_vega = s*np.exp(-q*tau)*np.sqrt(tau)*np.exp(-0.5*d1*d1)/np.sqrt(2*np.pi)
			return c, c_vega
		else:
			n1 = 0.5*(1+erf(-d1/np.sqrt(2)))
			n2 = 0.5*(1+erf(-d2/np.sqrt(2)))
			p = e*np.exp(-1*r*tau)*n2-s*np.exp(-1*q*tau)*n1
			p_vega = s*np.exp(-q*tau)*np.sqrt(tau)*np.exp(-0.5*d1*d1)/np.sqrt(2*np.pi)
			return p, p_vega
	else:
		if call_or_put == "call":
			return max(s-e, 0), 0
		else: 
			return max(e-s, 0), 0

def newton_solve(x0, target, func, N, eps = 1e-8):
	increment = 1
	x = x0
	k = 0
	while np.abs(increment) >= eps and k < N:
		y, y_prime = func(x)
		increment = (y - target)/y_prime
		x = x - increment
		k += 1
	return x

def implied_vol(s, e, r, q, tau, price, call_or_put):
	sigma_init = 0.15
	n_steps = 100

	def price_func(sigma):
		return bs_formula(s, e, r, q, sigma, tau, call_or_put)

	return newton_solve(sigma_init, price, price_func, n_steps)