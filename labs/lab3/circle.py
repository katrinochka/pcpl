from lab3_oop.figure import Figure
from lab3_oop.color import Color
import math

class Circle(Figure):

	name = 'Circle'

	def __init__(self, radius, color):
		self.color = color
		self.radius = radius
	
	def calc_square(self):
		return math.pi*(self.radius**2)
		
	@classmethod
	def get_name(self):
		return self.name
		
	def __repr__(self):
		return ("Name: {}; radius: {}; RGB: {},{},{}; square: {}".format(self.get_name(), str(self.radius), str(self.color.red), str(self.color.green), str(self.color.blue), str(self.calc_square())))
