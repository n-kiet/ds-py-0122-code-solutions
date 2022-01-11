# 3
ages = [29, 19, 17, 26, 32, 16, 21]

# 4
print(ages)

# 6
print('Fifth element in list Ages: {}'.format(ages[4]))

# 7
print('Second to last element in list Ages: {}'.format(ages[-2]))

# 8
print('Third to sixth element in list Ages: {}'.format(ages[2:6]))

# 9
print('First four elements in list Ages: {}'.format(ages[:4]))

# 10
print('17 is in list Ages: {}'.format(17 in ages))

# 11
print('42 is in list Ages: {}'.format(42 in ages))

# 13
ages[2]= 18
print(ages)

# 14
temp = ages[4]
ages[4]=ages[3]
ages[3]=temp

# 15
print('Fourth and fifth values: {} and {}'.format(ages[3], ages[4]))

# 17
ages.append(45)

# 18
ages.insert(0, 32)

# 19
ages.insert(5,37)

# 20
print(ages)

# 22
ages.pop()

# 23
ages.pop(2)

# 24
print(ages)
