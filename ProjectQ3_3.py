from models.cev import myCallPut
from models.bs_formula import implied_vol

def q3_implied_vol():
	S0 = 100
	r = 0.04
	q = 0.02
	Ts = [0.25, 0.5]
	flag = 1

	K_percentage = [0.8, 0.9, 1, 1.1, 1.2]

	for p in K_percentage:
		for T in Ts:
			K = p*S0
			price, _, _ = myCallPut(S0, r, q, T, K, flag)
			vol = implied_vol(S0, K, r, q, T, price, "put" if flag == 1 else "call")
			print("%d%%\t%.2f\t%.4f"%(p*100, T, vol))

if __name__ == "__main__":
	q3_implied_vol()