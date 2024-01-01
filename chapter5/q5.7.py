groceries = ['milk', 'cheese', 'bread', 'cereal']
position = 0

while position < len(groceries):
    label = str(position) + '. '
    print(label + groceries[position])
    position += 1
