import pandas
import numpy as np

def read_yahoo_data(path):
	df = pandas.read_csv(
		path, 
		parse_dates = ["Date"], 
		dayfirst = True
	)
	df.rename(str.lower, axis='columns', inplace = True)
	return df
