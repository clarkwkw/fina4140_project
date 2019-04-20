from models.bs_formula import bs_formula

if __name__ == "__main__":
	s = 150.07
	r = 0.03
	sigma = 0.2494361491753742
	tau = 1
	print("1:", bs_formula(s, s, r, 0, sigma, tau, "call")[0])
	print("2:", bs_formula(s, 1.1*s, r, 0, sigma, tau, "call")[0])
	print("3:", bs_formula(s, 1.1*s, r, 0.01, sigma, tau, "call")[0])
	print("4:", bs_formula(s, 0.9*s, r, 0, sigma, tau, "call")[0])
	print("5:", bs_formula(s, s, r, 0, sigma, tau, "put")[0])
	print("6:", bs_formula(s, 1.1*s, r, 0, sigma, tau, "put")[0])
	print("7:", bs_formula(s, 1.1*s, r, 0.01, sigma, tau, "put")[0])
	print("8:", bs_formula(s, 0.9*s, r, 0, sigma, tau, "put")[0])