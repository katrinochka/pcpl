from lab3_oop.color import Color
from lab3_oop.figure import Figure

class Rectangle(Figure):
	
	name = 'Rectangle'

	def __init__(self, width, height, color):
		self.width = width
		self.height = height
		self.color = color
		
	
	def calc_square(self):
		return self.width*self.height
		
	@classmethod
	def get_name(self):
		return self.name
		
	def __repr__(self):
		return ("Name: {}; width: {}; height: {}; RGB: {},{},{}; square: {}".format(self.get_name(), str(self.width), str(self.height), str(self.color.red), str(self.color.green), str(self.color.blue), str(self.calc_square())))
