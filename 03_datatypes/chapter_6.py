# Dictionaries

chai_order = dict(type="masala chai", size='large', sugar=2)
print(f"Chai order : {chai_order}")

chai_recipe = {}
chai_recipe['base'] = 'black tea'
chai_recipe['liquid'] = 'milk'

print(f"Recipe base : {chai_recipe['base']}")
print(f"Recipe : {chai_recipe}")

# deleting a key:value pair in dictionary
del chai_recipe['liquid']
print(f"Recipe : {chai_recipe}")

# membership
print(f"Is sugar in chai order ? : {'sugar' in chai_order}")

chai_order = {'type': 'ginger chai', 'size': 'Medium', 'sugar': 1}
# print(f"Order Details (keys) : {chai_order.keys()}")
# print(f"Order Details (values) : {chai_order.values()}")
# print(f"Order Details (items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item : {last_item}")

# update method in dictionary extends dictionary
extra_spices = {'cardamom' : 'crushed', 'ginger' : 'sliced'}
chai_recipe.update(extra_spices)
print(chai_recipe)

# if we try to get value of some key, when thatkey des not exist in the dictionary
# chai_size = chai_order['customer note']
# print(chai_size)
# The program crashes, the better way to do it safely is as below

# 'No Note'is by default, if customer_note key does not exist
# chai_order['customer_note'] = '5 star'
customer_note = chai_order.get("customer_note", "No Note")
print(f"Customer note is : {customer_note}")