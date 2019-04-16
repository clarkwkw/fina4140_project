from models.binomial_tree import calculate_price

Ms = [4, 8, 16, 32]
r = 0.03
sigma = 0.2494361491753742
T = 1
S = 150.07
options = [
	(2, "call", 1.1*S),
	(4, "call", 0.9*S),
	(6, "put", 1.1*S),
	(8, "put", 0.9*S)
]

def print_header():
	print("\t", end = "")
	for i, _, _ in options:
		print("%d\t"%i, end = "")
	print()

if __name__ == "__main__":
	print("European: ")
	print_header()
	for m in Ms:
		print("%d\t"%m, end = "")
		for _, call_or_put, exercise_price in options:
			print("%.4f\t"%calculate_price(m, r, sigma, T, exercise_price, S, call_or_put, "european"), end = "")
		print()

	print("American: ")
	print_header()
	for m in Ms:
		print("%d\t"%m, end = "")
		for _, call_or_put, exercise_price in options:
			print("%.4f\t"%calculate_price(m, r, sigma, T, exercise_price, S, call_or_put, "american"), end = "")
		print()