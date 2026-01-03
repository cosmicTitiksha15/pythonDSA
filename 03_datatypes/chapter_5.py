# Sets
essesntial_spices = {'cardamom', 'ginger', 'cinnamon'}
optional_spices = {"cloves", "ginger", "black pepper"}

# Union
all_spices = essesntial_spices | optional_spices
print(all_spices)

# Intersection
common_spices = essesntial_spices & optional_spices
print(common_spices)

# Difference
only_in_essential = essesntial_spices - optional_spices
print(only_in_essential)

# Membership
print(f"Is clove in essesntial spices ? : {'cloves' in essesntial_spices}")
print(f"Is clove in optional spices ? : {'cloves' in optional_spices}")

# Frozen Set