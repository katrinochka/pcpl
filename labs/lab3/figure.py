from abc import ABC, abstractmethod

class Figure(ABC):
	@abstractmethod
	def calc_square(self):
		pass
