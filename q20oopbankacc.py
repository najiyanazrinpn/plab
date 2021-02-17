class BankAcc:
	def __init__(self,name,accno,acctype):
		self.name=name
		self.accno=accno
		self.acctype=acctype
		self.balance=500.0
	def deposit(self,amt):
		self.balance+=amt
	def withdraw(self,amt):
		if (amt>(self.balance-500.0)):
			print("Insufficient balance!!!")
		else:
			self.balance-=amt
	def display(self):
		print("NAME: ",self.name)
		print("ACCOUNT NO: ",self.accno)
		print("ACCOUNT TYPE: ",self.acctype)
		print("BALANCE: ",self.balance)
name = input("Enter your name: ").upper()
accno = input("Enter account no: ")
typeacc = ["CURRENT", "SAVINGS"]
print("Select your account type")
acctype = typeacc[(int(input("Current or savings(0 for current and 1 for savings)? ")))]
b = BankAcc(name,accno,acctype)
b.display()
b.deposit(float(input("Enter amount to be deposited: ")))
b.withdraw(float(input("Enter amount to be withdrawn: ")))
b.display()