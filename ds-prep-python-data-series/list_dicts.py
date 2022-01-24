# Data Set: Do Not Modify
from list_tuples import employment


columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    {"unemployment_rate": 8, "year": 2013},
    {"unemployment_rate": 5, "year": 2006},
    {"unemployment_rate": 5, "year": 2017},
    {"unemployment_rate": 6, "year": 2015},
    {"unemployment_rate": 6, "year": 2002},
    {"unemployment_rate": 4, "year": 2019},
    {"unemployment_rate": 9, "year": 2012},
    {"unemployment_rate": 4, "year": 2018},
    {"unemployment_rate": 6, "year": 2003},
    {"unemployment_rate": 5, "year": 2007},
    {"unemployment_rate": 11, "year": 2010},
    {"unemployment_rate": 7, "year": 2014},
    {"unemployment_rate": 6, "year": 2004},
    {"unemployment_rate": 5, "year": 2016},
    {"unemployment_rate": 6, "year": 2005},
    {"unemployment_rate": 7, "year": 2021},
    {"unemployment_rate": 5, "year": 2001},
    {"unemployment_rate": 4, "year": 2020},
    {"unemployment_rate": 10, "year": 2011},
    {"unemployment_rate": 8, "year": 2009},
    {"unemployment_rate": 5, "year": 2008}
]

# Write your code below this line:

empty = []

# i
def last_appearing(empty):
    return empty[-1]

print(last_appearing(unemployment_rates))

# ii
empty_2 = []
def first_five(empty):
    first_5 = empty[0:5]
    for i in first_5:
        empty_2.append(tuple(i.values()))
    return empty_2

print(first_five(unemployment_rates))

# iii
empty_3 = []
def check(empty, year):
    for i in empty:
        empty_3.extend(tuple(i.values()))
    return True if year in empty_3 else False

print("2000 is included in the data series: {}".format(check(unemployment_rates, 2000)))
print("2010 is included in the data series: {}".format(check(unemployment_rates, 2010)))

# iv
empty_4 = []
def rate(empty):
    for i in empty:
        empty_4.append(tuple(i.values()))
    for j in empty_4:
        if j[1] == label_order[-1]:
            return j[0]

print(rate(unemployment_rates))

# v
def unique():
    U_year = set({})
    for i in empty_4:
        U_year.add(i[1])
    return U_year

print(unique())

# vi
empty_5 = []
def rate_by_year():
    for i in label_order:
        for j in empty_4:
            if i == j[1]:
                empty_5.append(j[0])
    return empty_5

print(rate_by_year())

# vii
def largest_rate():
    x=sorted(empty_5)
    return x[-1]

print(largest_rate())

# viii
employment_rates = []
def employment(empty):
    for i in empty:
        j = list(i.keys())
        j[0]='employment_rate'
        k = list(i.values())
        k[0] = 100 - k[0]
        employment_rates.append({j[0]: k[0], j[1]: k[1]})
    return employment_rates

print(employment(unemployment_rates))

# ix
new_unemployment_rates = []
def new_rate(empty):
    for i in empty:
        j = list(i.values())
        k = list(i.keys())
        if j[0] >= 7:
            new_unemployment_rates.append({k[0]: j[0], k[1]: j[1]})
    return new_unemployment_rates

print(new_rate(unemployment_rates))

# ix
list_number = []
count_number = {}
def count_rate(empty):
    for i in empty:
        j = list(i.values())
        list_number.append(j[0])
    for k in list_number:
        count_number.update({k: list_number.count(k)})
    return count_number

print(count_rate(unemployment_rates))
