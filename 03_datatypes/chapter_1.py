# 'int' is an immutable data type in Python.
# This means that once an integer object is created, its value cannot be changed. and here same variable name is 'reference' to that memory location.
sugar_amount = 2
print(f"Initial sugar amount: {sugar_amount} teaspoons")
print(f"Initial sugar id : {id(sugar_amount)}")
sugar_amount = 12
print(f"Updated sugar amount: {sugar_amount} teaspoons")
print(f"Updated sugar id : {id(sugar_amount)}")