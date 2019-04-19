import numpy as np
import pandas

S = 157.066376
K = 0.9*S
Su = 1.02*S
T = 1
r = 0.03
q = 0

def accumulator():
	simulation = pandas.read_csv("data/trajectory.csv", index_col = 0).as_matrix()
	knocked_out = np.any(simulation >= Su, axis = 0)

	alive_indices = np.logical_not(knocked_out)
	payoff = np.zeros(simulation.shape[1])
	payoff[alive_indices] = simulation[-1, alive_indices] - K

	estimations = np.exp(-r*T) * payoff

	print("S0 = %d, Monte Carlo estimation: %.4f"%(S, np.mean(estimations)))
	print("Standard deviation: %.4f"%np.std(estimations, ddof = 1)) 

if __name__ == "__main__":
	accumulator()