class Problem:
	def __init__(self, n1, op, n2):
		self.n1 = n1
		self.n2 = n2
		self.op = op

def arithmetic_arranger(problems, display=None):
	arranged_problems = ""
	problem_arr = []
	error_strings = ["Error: Too many problems.", "Error: Operator must be '+' or '-'.",
					"Error: Numbers must only contain digits.", "Error: Numbers cannot be more than four digits."]
	#errorchecking
	problem_count = 0
	for entry in problems:
		problem_count += 1
		if problem_count == 6:
			return error_strings[0]
		entry = entry.split(" ")
		problem_arr.append(Problem(entry[0], entry[1], entry[2]))
		if entry[1] != '+' and entry[1] != '-':
			return error_strings[1]
		if entry[0].isdigit() is not True or entry[2].isdigit() is not True:
			return error_strings[2]
		if len(entry[0]) > 4 or len(entry[2]) > 4:
			return error_strings[3]
	#filling rows
	spacing = ' ' * 4
	first = ""
	second = ""
	third = ""
	fourth = ""
	arr_len = len(problem_arr)
	i = 0
	while i < arr_len:
		total = len(problem_arr[i].n1)
		if len(problem_arr[i].n2) > len(problem_arr[i].n1):
			total = len(problem_arr[i].n2)
		total += 2
		first += (total - len(problem_arr[i].n1)) * ' '
		second += problem_arr[i].op + (total - len(problem_arr[i].n2) -1) * ' '
		first += problem_arr[i].n1
		second += problem_arr[i].n2
		third += ('_' * total)
		sum = int(problem_arr[i].n1) + int(problem_arr[i].n2)
		fourth += (total - len(str(sum))) * ' ' + str(sum)
		if i != arr_len - 1:
			first += spacing
			second += spacing
			third += spacing
			fourth += spacing
		i += 1
	first += "\n"
	second += "\n"
	arranged_problems = first + second + third
	if display is not None:
		if display == True:
			arranged_problems += "\n" + fourth
	return arranged_problems
