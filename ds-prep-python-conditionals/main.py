import random

day_of_week = 'monday'
print ("It's a weekday!") if day_of_week == 'saturday' or 'sunday' else print ("Have a good weekend!")

student_1_score = random.randint(0,99) + random.randint(0,4)*0.25
if student_1_score >= 70:
  pass_or_fail = "You passed!"
else:
  pass_or_fail = "You failed!"
print('Student 1 score:  {}  {}'.format(student_1_score, pass_or_fail))

student_2_score = random.randint(50,100) + random.randint(0,4)*0.25
if student_2_score < 60:
  letter_grade = "F"
elif student_2_score >=60 and student_2_score < 70:
  letter_grade = "D"
elif student_2_score >=70 and student_2_score < 80:
  letter_grade = "C"
elif student_2_score >= 80 and student_2_score < 90:
  letter_grade = "B"
elif student_2_score >= 90 and student_2_score < 100:
  letter_grade = "A"
else:
  letter_grade = "A+"
print('Student 2 score: {}, which is a/an: {}'.format(student_2_score, letter_grade))

def get_season_info(season):
  if season == "summer":
    print("Statistically, it's likely to be hotter today than in 6 months from now. Don't sweat it, though.")
  elif season == "spring":
    print("The flowers are blooming while it's spring, but that correlation, not causation.")
  elif season == "autumn":
    print("The leaves seem to regress to warmer colors as autumn approaches its end.")
  elif season =="winter":
    print("There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater.")
  else:
    print("That's not a season. Most likely.")

get_season_info("fasdf")

age=42
print("This is an adult") if age>=18 else print("This is a child")
