import matplotlib.pyplot as plt
import numpy as np

class LineChartBuilder:
	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)

	def add_series(self, series, x = None, label = None):
		if x is not None:
			self.ax.plot(x, series, label = label)
		else:
			self.ax.plot(series, label = label)

	def set_x_axis_label(self, x_axis_label):
		self.ax.set(xlabel = x_axis_label)

	def set_y_axis_label(self, y_axis_label):
		self.ax.set(ylabel = y_axis_label)

	def set_xticks(self, x_ticks):
		self.ax.set_xticks(x_ticks)

	def set_x_ticks_labels(self, x_ticks):
		self.ax.set_xticklabels(x_ticks_labels)

	def set_y_ticks(self, y_ticks):
		self.ax.set_yticks(y_ticks)

	def set_y_ticks_labels(self, y_ticks_labels):
		self.ax.set_yticklabels(y_ticks_labels)

	def enable_legend(self):
		self.ax.legend()

	def set_title(self, title):
		self.ax.set_title(title)

	def show(self):
		plt.show()