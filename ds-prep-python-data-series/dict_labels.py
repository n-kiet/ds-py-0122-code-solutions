# Data Set: Do Not Modify
from cProfile import label


columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    2002: 6,
    2020: 4,
    2007: 5,
    2015: 6,
    2010: 11,
    2014: 7,
    2001: 5,
    2006: 5,
    2004: 6,
    2009: 8,
    2013: 8,
    2008: 5,
    2021: 7,
    2018: 4,
    2011: 10,
    2005: 6,
    2016: 5,
    2019: 4,
    2012: 9,
    2017: 5,
    2003: 6
}

# Write your code below this line:

empty = []

# i
def last_appearing(empty):
    x= list(empty.items())
    j = x[-1]
    return dict({columns[0]: j[0], columns[1]: j[1]})

print(last_appearing(unemployment_rates))

# ii
def first_five(empty):
    x = list(empty.items())
    j = x[0:5]
    return j

print(first_five(unemployment_rates))

# iii
def check(empty, value):
    years = []
    x = list(empty.items())
    for j in x:
        years.append(j[0])
    return True if value in years else False

print("2000 is included in the data series: {}".format(check(unemployment_rates, 2000)))
print("2010 is included in the data series: {}".format(check(unemployment_rates, 2010)))

# iv
def rate(empty):
    x = list(empty.items())
    for i in x:
        if i[0] == label_order[-1]:
            return i[1]

print(rate(unemployment_rates))

# v
Unique = set({})
def unique_year(empty):
    x = list(empty.items())
    for i in x:
        Unique.add(i[0])
    return Unique

print(unique_year(unemployment_rates))

# vi
empty_1 = []
def rate_by_year(empty):
    x = list(empty.items())
    for i in label_order:
        for j in x:
            if i == j[0]:
                empty_1.append(j[1])

    return empty_1

print(rate_by_year(unemployment_rates))

# vii
def largest_rate(empty):
    x = sorted(empty_1)
    return x[-1]

print(largest_rate(unemployment_rates))

# viii
employment_rates = {}
def employment_rate(empty):
    x = list(empty.items())
    for i in x:
        (j, k) = i
        k = 100 - k
        employment_rates.update({j: k})
    return employment_rates

print(employment_rate(unemployment_rates))

# ix
series = {}
def new_series(empty):
    x = list(empty.items())
    for i in x:
        (j, k) = i
        if k >= 7:
            series.update({j: k})
    return series

print(new_series(unemployment_rates))

# x
empty_2 = {}
empty_3 = []
def count_rate(empty):
    x = list(empty.items())
    for i in x:
        (j, k) = i
        empty_3.append(k)
    for l in empty_3:
        empty_2.update({l: empty_3.count(l)})
    return empty_2

print(count_rate(unemployment_rates))
