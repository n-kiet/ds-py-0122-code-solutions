# 4
record = (1, 'Grimdiana', 'Bones', 'boulders')

# 5
row =' '

#6
for i in record:
    row = row + str(i) + ','

# 7
print(row)

# 9
values_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]

# 10
for x in values_list:
  print(x)

# 11
index_list = []

# 12
for i in reversed(range(len(values_list))):
  index_list.append(i)

# 13
print(index_list)

# 14
for i in index_list:
  if i % 2 != 0 :
    del values_list[i]

# 15
print(values_list)

# 17
vowels = {'A', 'E', 'I', 'O', 'U'}

# 18
parts_of_the_big_letter = {'L', 'M', 'N', 'O', 'P'}

# 19
for i in vowels:
  if i in parts_of_the_big_letter:
    parts_of_the_big_letter.remove(i)

# 20
print(parts_of_the_big_letter)

# 22
player_positions = {
  'Who': '1B',
  'What': '2B',
  "I don't Know": '3B',
  'Why': 'LF',
  'Because': "CF",
  'Tomorrow': 'P',
  'Today': 'C',
  "I Don't Care": 'SS'
}

# 23
players = []

# 24
for x in player_positions.keys():
  players.append(x)

# 25
print(players)

# 26
positions = set()

# 27
for x in player_positions.values():
  positions.add(x)

# 28
print(positions)

# 29
for i, j in player_positions.items():
  print(i,'is on',j)
