from prettytable import PrettyTable

table = PrettyTable()

print("""
First Table - unsorted
=======================
First column aligned to right
Second column aligned to left    
""")
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = "r"
print(table)

print("""
Second Table - sorted by 'Type'
===============================
First column aligned to center
Second column aligned to left    
""")
table.align["Pokemon Name"] = "c"
table.align['Type'] = "l"
print(table)
print(table.get_string(sortby='Type'))

print("""
Third Table - sorted by 'Pokemon Name'
======================================
First column aligned to right
Second column aligned to left
""")
table.sortby = 'Pokemon Name'
print(table)

print("""
Fourth Table - Add new rows
===========================
""")
table.add_row(['Bulbazoor', 'Plant']); table.add_row(['Kadabra', 'Psiquic'])
print(table)
