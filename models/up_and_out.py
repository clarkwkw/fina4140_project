import numpy as np
from scipy.stats import norm

def d1(S, K, Su, r, sigma, tau):
	return (np.log(S/K) + (r + 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

def d2(S, K, Su, r, sigma, tau):
	return (np.log(S/K) + (r - 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

def d3(S, K, Su, r, sigma, tau):
	return (np.log(S/Su) + (r + 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

def d4(S, K, Su, r, sigma, tau):
	return (np.log(S/Su) + (r - 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

def d5(S, K, Su, r, sigma, tau):
	return (np.log(S/Su) - (r - 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

def d6(S, K, Su, r, sigma, tau):
	return (np.log(S/Su) - (r + 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

def d7(S, K, Su, r, sigma, tau):
	return (np.log(S*K/Su/Su) - (r - 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

def d8(S, K, Su, r, sigma, tau):
	return (np.log(S*K/Su/Su) - (r + 0.5*sigma*sigma)*tau)/(sigma * np.sqrt(tau))

d_formula = [d1, d2, d3, d4, d5, d6, d7, d8]

def up_and_out_calculator_factory(K, Su, r, sigma, time_to_maturity):

	def up_and_out_calculator(S, t):
		tau = time_to_maturity - t
		nd = [np.nan] + [
			norm.cdf(di(S, K, Su, r, sigma, tau)) for di in d_formula
		]

		return S*(nd[1] - nd[3] - np.float_power(Su/S, 1+2*r/sigma/sigma)*(nd[6] - nd[8])) \
				- K*np.exp(-r*tau)*(nd[2] - nd[4] - np.float_power(Su/S, -1 + 2*r/sigma/sigma)*(nd[5] - nd[7]))

	return up_and_out_calculator

