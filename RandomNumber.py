import random as rd
print(rd.random())              # Random number between 0-1
print(rd.randint(1, 10))         # Random number between 1-10
print(rd.randrange(start=2))
list1 = [1, 2, 3, 4, 5]
print(rd.shuffle(list1))        # shuffle list
print(list1)
list2 = ['John', 'Castor', 'Troy']
print(rd.choice(list2))         # pick a random item from list
