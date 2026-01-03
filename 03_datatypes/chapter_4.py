# Operator Overloading
# As addition
base_liquid = ['water', 'milk']
extra_flavor = ['ginger']
full_liquid_mix = base_liquid + extra_flavor
print(full_liquid_mix)

# As multiplication
strong_brew = ['balck tea'] * 3
print(strong_brew)

strong_brew = ['black tea', 'water'] * 3
print(strong_brew)


# Converting an String to a list 
spices = list("CINNAMON")
print(spices)

# Bytearrays
raw_spice_data = bytearray(b"CINNAMOM")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARDA")
print(raw_spice_data)
