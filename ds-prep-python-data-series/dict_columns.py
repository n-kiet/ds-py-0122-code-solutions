# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    'year': [
        2009, 2011, 2005, 2016, 2001,
        2012, 2019, 2007, 2021, 2018,
        2010, 2013, 2006, 2017, 2015,
        2014, 2008, 2004, 2003, 2020,
        2002
    ],
    'unemployment_rate': [
        8, 10, 6, 5, 5,
        9, 4, 5, 7, 4,
        11, 8, 5, 5, 6,
        7, 5, 6, 6, 4,
        6
    ]
}

# Write your code below this line:

empty = []

# i
last = {}
def last_appearing(empty):
    x = list(empty.items())
    for i in x:
        last.update({i[0]: i[1][-1]})
    return last

print(last_appearing(unemployment_rates))

# ii
empty_2 = {}
def first_five(empty):
    x = list(empty.items())
    for i in x:
        (k, l) = i
        empty_2.update({k: l[0:5]})
    return list(empty_2.items())

print(first_five(unemployment_rates))

# iii
def check(empty, value):
    x = list(empty.items())
    if value in x[0][1]:
        return True
    else:
        return False

print("2000 is included in the data series: {}".format(check(unemployment_rates, 2000)))
print("2010 is included in the data series: {}".format(check(unemployment_rates, 2010)))

# iv
def rate(empty):
    x = list(empty.items())
    for i in range(len(label_order)):
        if x[0][1][i] == label_order[-1]:
            return x[1][1][i]

print(rate(unemployment_rates))

# v
def unique_year(empty):
    x = list(empty.items())
    return set(x[0][1])

print(unique_year(unemployment_rates))

# vi
empty_3 = []
empty_4 = []
def rate_by_year(empty):
    x = list(empty.items())
    for i in range(len(label_order)):
        empty_4.append([ x[0][1][i], x[1][1][i] ])
    for j in label_order:
        for k  in empty_4:
            if j == k[0]:
                empty_3.append(k[1])
    return empty_3

print(rate_by_year(unemployment_rates))

# vii
def largest_rate(empty):
    x = sorted(empty_3)
    return x[-1]

print(largest_rate(unemployment_rates))

# viii

employment = {}
l_1 = []
def Employment_rate(empty):
    x = list(empty.items())
    (a, b) = x[0]
    (j, k) = x[1]
    j = 'employment_rate'
    for l in k:
        l = 100 - l
        l_1.append(l)
    employment.update({a: b, j: l_1})
    return employment

print(Employment_rate(unemployment_rates))

# ix
year_2 = []
rate_2 = []
s_dict = {}
def series(empty):
    x = list(empty.items())
    for i in range(len(label_order)):
        if x[1][1][i] >= 7:
            rate_2.append(x[1][1][i])
            year_2.append(x[0][1][i])
    s_dict.update({x[0][0]: year_2, x[1][0]: rate_2})
    return s_dict

print(series(unemployment_rates))

# x
empty_5 = {}
def count_rate(empty):
    x = list(empty.items())
    for i in x[1][1]:
        empty_5.update({i: x[1][1].count(i)})
    return empty_5

print(count_rate(unemployment_rates))
