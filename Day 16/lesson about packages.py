

# python package index https://pypi.org/
# Pretty table source https://pypi.org/project/prettytable/
"""to import to project open file/settings then select the current project name
then click the plus sign upper left of the opened window then search for package to import"""

from prettytable import  PrettyTable

# Be sure that you are calling the right function name which has () at the end when trying
# to create objects from class
table = PrettyTable()

# add entries into table for more info please go back to documentation from package
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# see the current attribute value of table
print(table.align)
print(table)

# modify attribute to style table
table.align = "l"

print(table)