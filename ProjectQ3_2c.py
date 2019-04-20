import numpy as np
from models.cev import myCallPut

def q2c_tabulate():
	S0 = 100
	r = 0.04
	q = 0.02
	T = 1
	K = S0
	flag = 1

	K_percentage = np.arange(90, 110 + 1, step = 2)
	
	for p in K_percentage:
		K = p/100 * S0
		v0, _, _ = myCallPut(S0, r, q, T, K, flag)
		print("%d%%S0\t%.4f"%(p, v0))

if __name__ == "__main__":
	q2c_tabulate()