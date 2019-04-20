import numpy as np
from models.cev import myCallPut

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def q2b_plot_graph():
	S0 = 100
	r = 0.04
	q = 0.02
	T = 1
	K = S0
	flag = 1

	v0, V, model = myCallPut(S0, r, q, T, K, flag)
	asset_prices = model.SValues
	ts = model.TValues

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	xs, ys, vs = [], [], []

	vs = V.reshape(V.shape[0]*V.shape[1])
	ys, xs = np.meshgrid(asset_prices, ts, indexing="ij")

	surf = ax.plot_trisurf(xs.reshape(-1), ys.reshape(-1), vs, cmap=cm.jet, linewidth=0.1)

	ax.set_xlabel("t")
	ax.set_ylabel('S')
	ax.set_zlabel('Option price')

	
	ax.view_init(elev=10., azim=45)
	plt.savefig("at_the_maturity_put.png")

	plt.show()

if __name__ == "__main__":
	q2b_plot_graph()