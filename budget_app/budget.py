"""
thoughts:
deposit is unclear
how does the ledger work
when wanting to print the 'budget' object, what is called
basicly check the test_module for how the functions are called and what is expected for return
leave it for now and pick it up later

"""

class Category:
	"""
	gets a name for the ledger (the balance overview)
	has a instance variable for this ledger aswell, which is a list
	"""
	def __init__(self, name):
		self.n1 = name
		ledger = []
	"""
	deposit method that accepts an amount and description.
	If no description is given, it should default to an empty string.
	The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
	"""
	def deposit(amount, description, self):
		print("yep")
	"""
	withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number.
	If there are not enough funds, nothing should be added to the ledger.
	This method should return True if the withdrawal took place, and False otherwise.
	"""
	def withdraw(amount, description=None, self):
		print("yep")
	"""
	get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
	"""
	def get_balance(self):
		print("yep")
	"""
	transfer method that accepts an amount and another budget category as arguments.
	The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
	The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
	If there are not enough funds, nothing should be added to either ledgers.
	This method should return True if the transfer took place, and False otherwise.
	"""
	def transfer(amount, category, self):
		print("yep")
	"""
	check_funds method that accepts an amount as an argument.
	It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
	This method should be used by both the withdraw method and transfer method.
	"""
	def check_funds(amount, self):
		print("yep")

"""
get a list of categories and create a chart like the following with exact same kind of spacing:

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
	print(categories)
