list1 = [2, 3, 5, 3, 1, 6]

for item in list1:
    # count = 0
    count = list1.count(item)
    if count > 1:
        list1.remove(item)

print(list1)
