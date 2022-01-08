# Questions 1-4

person = {
  "first_name": "Kiet",
  "last_name":"Nguyen",
  "hobby": "Snowboarding"
}

print('Initial Dictionary person: {}'.format(person))


# Question 6
first_name=person['first_name']

# Question 7
last_name=person.get('last_name')

# Question 8
middle_name = person.get('middle_name')

# Question 9
print('My full name is: {} {} {}'.format(first_name, middle_name, last_name))

# Question 11
person['job']='QA Specialist'

# Question 12
print('Added job: {}'.format(person['job']))

# Question 14
person.update({'hobby':'Dragon Ball Animation'})

# Question 15
print('Updated hobby: {}'.format(person.get('hobby')))

# Question 17
person.pop('last_name')

# Question 18
print('Dictionary person after last_name got removed: {}'.format(person))
