class Category:
	"""
	gets a name for the ledger (the balance overview)
	has a instance variable for this ledger aswell, which is a list
	"""
	def __init__(self, name):
		self.name = name
		self.ledger = []
		self.balance = 0.0
	
	"""
	When the budget object is printed it should display:

	* A title line of 30 characters where the name of the category,
		is centered in a line of * characters.
	* A list of the items in the ledger. Each line should show the description and amount.
		The first 23 characters of the description should be displayed, then the amount.
		The amount should be right aligned, contain two decimal places,
		and display a maximum of 7 characters.
	* A line displaying the category total.
	"""
	def __str__(self):
		top = self.name.center(30, "*")
		overview = top + "\n"
		for entry in self.ledger:
			tag_length = 23
			tag = entry["description"][0:tag_length]
			entry_length = len(entry["description"])
			if entry_length < tag_length:
				tag = tag + (" " * (tag_length - entry_length))
			n = "{:.2f}".format(entry["amount"])
			if (len(n) > 7):
				n = n[:7]
			else:
				n = (" " * (7 - len(n))) + n
			overview += tag + n + "\n"
		overview += "Total: " + "{:.2f}".format(self.balance)
		return overview
	
	"""
	deposit method that accepts an amount and description.
	If no description is given, it should default to an empty string.
	The method should append an object to the ledger list,
	in the form of {"amount": amount, "description": description}.
	"""
	def deposit(self, amount, description=""):
		self.balance += amount
		temp = {"amount":amount, "description": description}
		self.ledger.append(temp)
	
	"""
	withdraw method that is similar to the deposit method,
	but the amount passed in should be stored in the ledger as a negative number.
	If there are not enough funds, nothing should be added to the ledger.
	This method should return True if the withdrawal took place, and False otherwise.
	"""
	def withdraw(self, amount, description=""):
		if self.balance < amount:
			return False
		self.balance -= amount
		temp = {"amount":amount*-1, "description": description}
		self.ledger.append(temp)
		return True

	"""
	get_balance method that returns the current balance of the budget category,
	based on the deposits and withdrawals that have occurred.
	"""
	def get_balance(self):
		return self.balance

	"""
	transfer method that accepts an amount and another budget category as arguments.
	The method should add a withdrawal with the amount
	and the description "Transfer to [Destination Budget Category]".
	The method should then add a deposit to the other budget category, 
	with the amount and the description "Transfer from [Source Budget Category]".
	If there are not enough funds, nothing should be added to either ledgers.
	This method should return True if the transfer took place, and False otherwise.
	"""
	def transfer(self, amount, category):
		if self.check_funds(amount) == False:
			return False
		self.withdraw(amount, "Transfer to " + category.name)
		category.deposit(amount, "Transfer from " + self.name)
		return True
	
	"""
	check_funds method that accepts an amount as an argument.
	It returns False if the amount is greater than the balance of the budget category,
	and returns True otherwise.
	This method should be used by both the withdraw method and transfer method.
	"""
	def check_funds(self, amount):
		if self.balance < amount:
			return False
		return True

"""
The chart should show the percentage spent in each category passed in to the function.
The percentage spent should be calculated only with withdrawals and not with deposits.
Down the left side of the chart should be labels 0 - 100.
The "bars" in the bar chart should be made out of the "o" character.
The height of each bar should be rounded down to the nearest 10.
The horizontal line below the bars should go two spaces past the final bar.
Each category name should be written vertically below the bar.
There should be a title at the top that says "Percentage spent by category".

EXAMPLE:
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g
"""
def create_spend_chart(categories):
	top = "Percentage spent by category\n"
	overview = ""
	overview += top
	costs = []
	for name in categories:
		sub_total = 0
		for entry in name.ledger:
			spend = entry["amount"]
			if spend < 0:
				sub_total += (spend * -1)
		costs.append(sub_total)
	total = 0
	for entry in costs:
		total += entry
	# print(costs)
	# print(total)
	ratios = []
	for entry in costs:
		percent = entry / total * 100
		ratios.append(percent)
	# print(ratios)
	percent_num = 100
	while(percent_num >= 0):
		overview += str(percent_num).rjust(3) + "|"
		for n in ratios:
			overview += " "
			if n > percent_num:
				overview += "o"
			else:
				overview += " "
			overview += " "
		overview += " \n"
		percent_num += - 10
	cat_len = len(categories)
	overview += (" " * 4) + ("---" * cat_len) + "-" + "\n"
	
	longest_one = 0
	for entry in categories:
		if len(entry.name) > longest_one:
			longest_one = len(entry.name)
	# print(longest_one)
	names_length = []
	for cat in categories:
		names_length.append(len(cat.name))
	for i in range(longest_one):
		overview += (" " * 4)
		for j in range(cat_len):
			if i >= names_length[j]:
				overview += (" " * 3)
			else:
				overview += " " + categories[j].name[i] + " "
		overview += " \n"
	# print(overview)
	return overview.rstrip("\n")
