import numpy as np
import pandas
from data_io import read_yahoo_data
from visualization.line_chart import LineChartBuilder

delta_t = 1/250 #day
n_trajectory = 1000
n_step = 250
summary_file = "simulation_summary.csv"
trajectory_file = "trajectory.csv"

def generate_trajectory(mu, sigma, init_price, delta_t, n_step, n_trajectory):
	sigma_dw = np.random.normal(size = (n_trajectory, n_step)) * np.sqrt(delta_t) * sigma
	trajectory = np.zeros((n_trajectory, n_step + 1))
	trajectory[:, 0] = init_price

	for i in range(1, n_step + 1):
		trajectory[:, i] = trajectory[:, i - 1] * (1 + mu*delta_t + sigma_dw[:, i - 1])

	return trajectory

def generate_summary(trajectory):
	ind_return = trajectory[:, 1:]/trajectory[:, :-1] - 1
	d = {
		"min": np.amin(trajectory, axis = 1),
		"max": np.amax(trajectory, axis = 1),
		"avg_price": np.average(trajectory, axis = 1),
		"avg_return": np.average(ind_return, axis = 1) * 250,
		"stdev": np.std(ind_return, axis = 1, ddof = 1) * np.sqrt(250)
	}
	return pandas.DataFrame(data = d)


if __name__ == "__main__":
	mu = float(input("mu: "))
	sigma = float(input("sigma: "))
	stock_df = read_yahoo_data("./data/AAPL.csv")
	init_price = stock_df.loc[stock_df["date"] == "31/12/2018", "adj close"].iloc[0]
	
	print("Initial price: %.2f"%(init_price))

	trajectory = generate_trajectory(mu, sigma, init_price, delta_t, n_step, n_trajectory)

	summary = generate_summary(trajectory)
	summary.to_csv(summary_file)

	print("Simulation summary is saved as %s"%summary_file)

	pandas.DataFrame(trajectory.T).to_csv(trajectory_file)
	print("Tajectory file is saved as %s"%trajectory_file)

	line_chart_builder = LineChartBuilder()

	for i in range(10):
		line_chart_builder.add_series(
			x = None, 
			series = trajectory[i, :]
		)

	line_chart_builder.set_xticks([])
	line_chart_builder.set_x_axis_label("Time")
	line_chart_builder.set_y_axis_label("Price")
	line_chart_builder.set_title("Simulated Price of AAPL")
	line_chart_builder.show()