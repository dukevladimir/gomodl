class UnaryOperation:

	def __init__(self, func = None):
		self._func = func
		self._output = None

	def eval(self,value):
		self._output = self._func(value)

	def output(self,value):
		self.eval(value)
		return self._output

class BinaryOperation:

	def __init__(self, func = None):
		self._func = func
		self._output = None

	def eval(self,data):
		self._output = self._func(data[0],data[1])

	def output(self,data):
		self.eval(data)
		return self._output

negate = UnaryOperation( lambda x: -x )
square = UnaryOperation( lambda x: x * x )
add = BinaryOperation( lambda x, y : x + y )
subtract = BinaryOperation( lambda x, y : x - y )
multiply = BinaryOperation( lambda x, y : x * y )
divide = BinaryOperation( lambda x, y : x / y )
power = BinaryOpeartion( lambda x, y: x**y )