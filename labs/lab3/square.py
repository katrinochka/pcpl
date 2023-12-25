from lab3_oop.rectangle import Figure

class Square(Figure):

	name = 'Square'

	def __init__(self, length, color):
		self.color = color
		self.length = length
	
	def calc_square(self):
		return self.length**2
		
	@classmethod
	def get_name(self):
		return self.name
		
	def __repr__(self):
		return ("Name: {}; length: {}; RGB: {},{},{}; square: {}".format(self.get_name(), str(self.length), str(self.color.red), str(self.color.green), str(self.color.blue), str(self.calc_square())))
