class UnaryOperation:

	def __init__(self, func = None):
		self._func = func
		self._output = None

	def eval(self,value):
		self._output = self._func(value)

	def output(self,value):
		self.eval(value)
		return self._output

def BinaryOperation:

	def __init__(self, func = None):
		self._func = func
		self._output = None

	def eval(self,data):
		self._output = self._func(data[0],data[1])

	def output(self,data):
		self.eval(data)
		return self._output