import numpy as np 

K = 90
Su = 120
r = 0.03
sigma = 0.2
time_to_maturity = 1
mu = 0.1
delta_t = 0.001

def generate_trajectory_with_ko(mu, sigma, init_price, delta_t, n_step, n_trajectory, upper_limit):
	sigma_dw = np.random.normal(size = (n_trajectory, n_step)) * np.sqrt(delta_t) * sigma
	trajectory = np.zeros(n_trajectory)
	trajectory[:] = init_price
	knocked_out = np.zeros(n_trajectory, dtype=bool)

	for i in range(1, n_step + 1):
		trajectory = trajectory * (1 + mu*delta_t + sigma_dw[:, i - 1])
		knocked_out[trajectory >= upper_limit] = True

	return trajectory, knocked_out

def monte_carlo():
	s0 = 100
	n_trajectory = 10000
	n_simulation = 200

	estimates = []

	for _ in range(n_simulation):
		trajectory, knocked_out = generate_trajectory_with_ko(
			mu, 
			sigma, 
			s0, 
			delta_t, 
			int(time_to_maturity/delta_t), 
			n_trajectory,
			Su
		)

		alive_indices = np.logical_not(knocked_out)
		option_payoff = np.zeros(n_trajectory)
		option_payoff[alive_indices] = np.maximum(trajectory[alive_indices] - K, 0)
		option_price = np.mean(np.exp(-r*time_to_maturity) * option_payoff) 
		estimates.append(option_price)

	print("S0 = %d, Monte Carlo estimation: %.4f"%(s0, np.mean(estimates)))
	print("Standard deviation: %.4f"%np.std(estimates, ddof = 1))

if __name__ == "__main__":
	monte_carlo()