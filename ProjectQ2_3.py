import numpy as np 
import pandas
from ProjectQ1_2 import generate_trajectory

Ms = [4, 8, 16, 32]
r = 0.03
mu = 0.032046941294592554
sigma = 0.2494361491753742
delta_t = 1/250
T = 1
n_step = int(250*T)
S = 150.07
options = [
	(2, "call", 1.1*S),
	(4, "call", 0.9*S),
	(6, "put", 1.1*S),
	(8, "put", 0.9*S)
]
Ns = [100, 1000, 5000, 10000]

def monte_carlo(exercise_price, r, t, call_or_put, n):
	if call_or_put not in ["call", "put"]:
		raise Exception("call_or_put must be either 'call' or 'put'")
	
	final_prices = generate_trajectory(mu, sigma, S, delta_t, n_step, n)[:, -1]

	payoff = 0
	if call_or_put == "call":
		payoff = np.maximum(final_prices - exercise_price, 0)
	else:
		payoff = np.maximum(exercise_price - final_prices , 0)

	prices = np.exp(-r*t)*payoff

	m = final_prices.shape[0]
	width = 1.96*np.std(prices, ddof = 1)/np.sqrt(m)
	return np.mean(prices), width

def print_header():
	print("\t", end = "")
	for i, _, _ in options:
		print("%d\t"%i, end = "")
	print()

if __name__ == "__main__":
	print_header()
	for n in Ns:
		print("n=%d\t"%n, end = "")
		for i, call_or_put, exercise_price in options:
			price, _ = monte_carlo(exercise_price, r, T, call_or_put, n)
			print("%.4f\t"%price, end = "")
		print()