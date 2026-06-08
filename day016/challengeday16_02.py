from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = "r"
print(table)

table.align["Pokemon Name"] = "c"
table.align['Type'] = "l"
print(table)
print(table.get_string(sortby='Type'))

table.sortby = 'Pokemon Name'
print(table)

table.add_row(['Bulbazoor', 'Plant']); table.add_row(['Kadabra', 'Psiquic'])
print(table)
