import numpy as np
from data_io import read_yahoo_data
from visualization.line_chart import LineChartBuilder

def log_price_diff_calculator_factory():
	cache = {"prev_adj_close": np.NAN}
	def applied(row):
		result = None
		if not np.isnan(cache["prev_adj_close"]):
			result = row["log adj close"] - cache["prev_adj_close"]
		cache["prev_adj_close"] = row["log adj close"]
		return result

	return applied

if __name__ == "__main__":
	stock_df = read_yahoo_data("./data/AAPL.csv")
	line_chart_builder = LineChartBuilder()

	line_chart_builder.add_series(
		x = None, 
		series = stock_df["adj close"]
	)
	line_chart_builder.set_xticks([])
	line_chart_builder.set_x_axis_label("Time")
	line_chart_builder.set_y_axis_label("Price")
	line_chart_builder.set_title("AAPL")
	line_chart_builder.show()

	stock_df["log adj close"] = np.log(stock_df["adj close"])
	log_price_diff_calculator = log_price_diff_calculator_factory()

	diff_log_prices = stock_df.apply(log_price_diff_calculator, axis = 1,  result_type='reduce').drop(0)

	volatility = np.std(diff_log_prices, ddof = 1)*np.sqrt(250)
	annualized_return = np.mean(diff_log_prices) + 0.5*volatility*volatility
	print("mu: ", annualized_return)
	print("sigma: ", volatility)