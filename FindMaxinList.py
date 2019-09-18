list1 = [4, 7, 1, 9, 3, 8, 2, 5]
max_value = list1[0]
min_value = list1[0]
for item in list1:
    if max_value < item:
        max_value = item
for item in list1:
    if min_value > item:
        min_value = item
print(max_value)
print(min_value)
