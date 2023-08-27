class Problem:
	def __init__(self):
		self.n1 = None
		self.n2 = None
		self.op = None

def arithmetic_arranger(problems, display=None):
	arranged_problems = ""
	error_strings = ["Error: Too many problems.", "Error: Operator must be '+' or '-'.",
					"Error: Numbers must only contain digits.", "Error: Numbers cannot be more than four digits."]
	#errorchecking
	problem_count = 0
	for entry in problems:
		problem_count += 1
		if problem_count == 5:
			return error_strings[0]
		#array of Problem, filling it and errorchecking it for symbols and length

	if display is not None:
		if display is True:
			print("display is set to True")

	return arranged_problems
