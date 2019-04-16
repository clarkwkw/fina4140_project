from enum import Enum
import numpy as np

class OptionType(Enum):
	european = 0
	american = 1

class PutCallType(Enum):
	put = 0
	call = 1

class BTree:
	def __init__(self, s_0, u, d, m, q, discount_factor, K, put_or_call, european_or_american):
		self.node_collection = {}
		self.u = u
		self.d = d
		self.q = q
		self.discount_factor = discount_factor
		self.k = K 
		self.put_call_type = put_or_call
		self.option_type = european_or_american
		self.root = self.create_node(s_0, 0, 0)
		self.root.expand(m, self.create_node)

	def create_node(self, s_0, level, u_count):
		index = (level, u_count)
		if index not in self.node_collection:
			node = BTreeNode(s_0, self.u, self.d, level, u_count)
			self.node_collection[index] = node
		else:
			node = self.node_collection[index]
		return node

	@property
	def price(self):
		return self.root.compute_price(self.q, self.discount_factor, self.k, self.put_call_type, self.option_type)

class BTreeNode:
	def __init__(self, s_0, u, d, level, u_count):
		self.s_0 = s_0
		self.u = u
		self.d = d
		self.u_child, self.d_child = None, None
		self.__price = None
		self.u_count = u_count
		self.level = level

	def expand(self, level, create_node):
		if level == 0:
			return 

		if self.u_child is None:
			self.u_child = create_node(self.s_0*self.u, level = self.level+1, u_count = self.u_count+1)
			self.u_child.expand(level - 1, create_node)

		if self.d_child is None:
			self.d_child = create_node(self.s_0*self.d, level = self.level+1, u_count = self.u_count)
			self.d_child.expand(level - 1, create_node)

	def compute_price(self, *args, **kwargs):
		if self.__price is None:
			self.__price = self.__compute_price(*args, **kwargs)
		return self.__price 

	def __compute_exercise_payoff(self, k, put_call_type):
		if PutCallType[put_call_type] == PutCallType["put"]:
			return max(k-self.s_0, 0)
		else:
			return max(self.s_0 - k, 0)

	def __compute_price(self, q, discount_factor, k, put_call_type, option_type):
		if self.__price is not None:
			return self.__price

		if self.u_child is None:
			return self.__compute_exercise_payoff(k, put_call_type)

		u_child_price = self.u_child.compute_price(q, discount_factor, k, put_call_type, option_type)
		d_child_price = self.d_child.compute_price(q, discount_factor, k, put_call_type, option_type)

		own_price = discount_factor*(q*u_child_price+(1-q)*d_child_price)

		if OptionType[option_type] == OptionType["european"]:
			return own_price
		else:
			return max(own_price, self.__compute_exercise_payoff(k, put_call_type))

def calculate_price(m, r, sigma, T, K, S, put_or_call, european_or_american):
	delta_t = T/m
	discount_factor = np.exp(-r*delta_t)
	beta = 0.5*(discount_factor+np.exp(delta_t*pow(sigma, 2))/discount_factor)
	u = beta + np.power(beta*beta - 1, 0.5)
	d = 1/u
	q = (1/discount_factor-d)/(u-d)

	tree = BTree(
		s_0 = S, 
		u = u, 
		d = d, 
		m = m, 
		q = q, 
		discount_factor = discount_factor, 
		K = K, 
		put_or_call = put_or_call, 
		european_or_american = european_or_american
	)
	return tree.price