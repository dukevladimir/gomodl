class UnaryOperation:

	def __init__(self, func = None):
		self._func = func
		self._output = None

	def eval(self,value):
		self._output = self._func(value)

	def output(self,value):
		self.eval(value)
		return self._output