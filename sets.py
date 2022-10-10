# Sets
# unique elements
# setname = {value1, value2, ...} # ex. x = {13, 45, 'WWW'}
# empty_sets = set()
# add() # ex. x.add(777) = {13, 45, 'WWW', 777}
# remove() # ex. x.remove(45) = {13, 'WWW', 777}
# discard() # ex. x.discard('WWW') = {13, '777}

rainbow_colors = {'green', 'blue', 'white', 'black'}
print(rainbow_colors)

empty_sets = set()
print(empty_sets)
print(type(empty_sets))

rainbow_colors.add(777)
print(rainbow_colors)

#rainbow_colors.pop()
#print(rainbow_colors)

rainbow_colors.remove(777)
print(rainbow_colors)
