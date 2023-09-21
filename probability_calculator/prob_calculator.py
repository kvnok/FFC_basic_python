import copy
import random
# Consider using the modules imported above.

class Hat:
	# kwargs and contents
	# kwargs is input in form of blue=2, red=1, green=3
	# then contents would be ["blue", "blue", "red", "green", "green", "green"]
	def __init__(self, **kwargs):
		self.list = []
		self.contents = []
		for color, count in kwargs.items():
			self.list.append({color : count})
			self.contents.extend([color] * count)

	def draw(self, n):
		

	def printer(self):
		print(self.list)
		print(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return ""