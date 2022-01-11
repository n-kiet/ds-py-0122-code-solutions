# 3
trail_mix = {'m&ms', 'peanuts', 'raisins'}

# 4
print(trail_mix)

# 6
print('cashews is in trail_mix: {}'.format('cashew' in trail_mix))

# 7
print('peanuts is in trail_mix: {}'.format('peanuts' in trail_mix))

# 9
trail_mix.add('pretzels')

# 10
trail_mix.update({'peanuts', 'banana chips', 'bits of jerky'})

# 11
print("Original set trail_mix after adding 'pretzels', 'peanuts', 'banana chips', and 'bit of jerky': {}".format(trail_mix))

# 13
trail_mix.remove('m&ms')

# 14
trail_mix.discard('raisins')

# 15
trail_mix.discard('rat poison')

# 16
print("Set trail_mix after removing 'm&ms', 'raisins', and 'rat poison': {}".format(trail_mix))

# 17
nuts = {'peanuts', 'cashews', 'almonds', 'walnuts', 'pecans'}

# 19
# i
print('All elements in nuts, trail_mix, or both: {}'.format(nuts.union(trail_mix)))

# ii
print('All elements in both nuts and trail_mix: {}'.format(nuts.intersection(trail_mix)))

# iii
print('All elements in trail_mix but nuts: {}'.format(trail_mix.difference(nuts)))

# iv
print('All elements in nuts but trail_mix: {}'.format(nuts.difference(trail_mix)))
