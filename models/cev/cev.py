from .CNEu import CNEu

def myCallPut(S0, r, q, T, K, flag):
	alpha = 20
	beta = 2
	M = 100
	N = 1000
	max_s = 1.3*S0
	model = CNEu(K, r, q, T, alpha, beta, max_s, M, N, is_call=flag == 0)
	
	v0 = model.price(S0)
	v = model.grid

	return v0, v, model