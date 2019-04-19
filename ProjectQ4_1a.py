import numpy as np
from models.up_and_out import up_and_out_calculator_factory
from visualization.line_chart import LineChartBuilder

K = 90
Su = 120
r = 0.03
sigma = 0.2
time_to_maturity = 1
mu = 0.1
delta_t = 0.001

def plot():
	up_and_out = up_and_out_calculator_factory(
		K = K,
		Su = Su,
		r = r,
		sigma = sigma,
		time_to_maturity = time_to_maturity
	)

	stock_prices = list(range(80, 120 + 1, 2))
	option_prices = []
	for s in stock_prices:
		option_prices.append(up_and_out(s, 0))

	chart = LineChartBuilder()
	chart.add_series(option_prices, stock_prices)
	chart.set_x_axis_label("Stock Price")
	chart.set_y_axis_label("Option Price")
	chart.set_title("European Up-and-out Barrier Option")
	chart.show()

if __name__ == "__main__":
	plot()