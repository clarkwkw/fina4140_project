from data_io import read_yahoo_data
from visualization.line_chart import LineChartBuilder


if __name__ == "__main__":
	stock_df = read_yahoo_data("./data/AAPL.csv")
	line_chart_builder = LineChartBuilder()

	line_chart_builder.add_series(
		x = None, 
		series = stock_df["close"]
	)
	line_chart_builder.set_xticks([])
	line_chart_builder.set_x_axis_label("Time")
	line_chart_builder.set_y_axis_label("Price")
	line_chart_builder.set_title("AAPL")
	line_chart_builder.show()