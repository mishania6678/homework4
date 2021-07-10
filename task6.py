from itertools import count, cycle

# 1
for i in count(1):
    if i == 101: break
    print(i)

# 2
counter = 0
for i in cycle(['First', 'Second', 'Third', 'ListEnd\n']):
    if counter == 100: break
    print(i)
    counter += 1
