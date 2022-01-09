# 3
passenger = tuple((12, True, 'Bonnell, Miss. Elizabeth', 'female', 58))

# 4
print(passenger)

# 6
name = passenger[2]

# 7
age = passenger[-1]

# 8
print('Full Name: {}       Age: {}'.format(name, age))

# 9
survived_and_name = passenger[1:3]

#10
gender_and_age = passenger[3:]

# 11
print('survived_and_name / gender_and_age: {} / {}'.format(survived_and_name, gender_and_age))

# 12
is_female = 'female' in passenger

# 13
is_male = 'male' in passenger

# 14
print('is_female: {}      is_male: {}'.format(is_female, is_male))

# 15
def get_survival_info(passenger):
  (id, survived, name, gender, age) = passenger
  new_tuple = (age, gender, survived)
  return new_tuple

# 17
print(get_survival_info(passenger))

# 18
passenger_2 = ((11, True, 'Sandstrom, Miss. Marguerite Rut', 'female', 4))
passenger_3 = ((28, False, 'Fortune, Mr. Charles Alexander', 'male', 19))
passenger_4= ((51, False, 'Master. Juha Niilo', 'male', 7))

# 19
print(get_survival_info(passenger_2))
print(get_survival_info(passenger_3))
print(get_survival_info(passenger_4))
