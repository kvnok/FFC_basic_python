import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
	# kwargs and contents
	# kwargs is input in form of blue=2, red=1, green=3
	# then contents would be ["blue", "blue", "red", "green", "green", "green"]
	def __init__(self, **kwargs):
		# self.list = []
		self.contents = []
		for color, count in kwargs.items():
			# self.list.append({color : count})
			self.contents.extend([color] * count)

	def draw(self, n):
		if n >= len(self.contents):
			return self.contents
		kinda_random = random.sample(self.contents, n)
		for entry in kinda_random:
			self.contents.remove(entry)
		return kinda_random

	def __copy__(self):
		hat_copy = Hat()
		hat_copy.contents = self.contents#[:]
		return hat_copy

	# def printer(self):
	# 	print(self.list)
	# 	print(self.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	done_succes = 0
	for i in range(num_experiments):
		hat_copy = copy.deepcopy(hat)
		kinda_random = hat_copy.draw(num_balls_drawn)
		#for use later
		unique = set(kinda_random)
		the_dict = {}
		for color in unique:
			count = kinda_random.count(color)
			the_dict[color] = count
		success = True
		#check
		for color, quantity in expected_balls.items():
			if color not in the_dict or the_dict[color] < quantity:
				success = False
				break
		if success == True:
			done_succes += 1
	return done_succes / num_experiments
