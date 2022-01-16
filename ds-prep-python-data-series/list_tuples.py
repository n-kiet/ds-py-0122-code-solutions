# Data Set: Do Not Modify
from pickle import EMPTY_DICT
from webbrowser import get


columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    (2005, 6),
    (2001, 5),
    (2013, 8),
    (2011, 10),
    (2017, 5),
    (2006, 5),
    (2009, 8),
    (2021, 7),
    (2002, 6),
    (2007, 5),
    (2012, 9),
    (2014, 7),
    (2003, 6),
    (2019, 4),
    (2016, 5),
    (2015, 6),
    (2018, 4),
    (2008, 5),
    (2010, 11),
    (2004, 6),
    (2020, 4)
]

# Write your code below this line:

empty = []


# i
def get_last_appearing(empty):
    tup=empty[-1]
    (x,y)=tup
    return dict({columns[0]: x, columns[1]: y})

print(get_last_appearing(unemployment_rates))

# ii
def first_five(empty):
    return empty[0:5]

print(first_five(unemployment_rates))

# iii
def check(empty, value):
    empty_2=[]
    for i in empty:
        empty_2.append(i[0])
    return True if value in empty_2 else False

print("2000 is included in the data series: {}".format(check(unemployment_rates, 2000)))
print("2010 is included in the data series: {}".format(check(unemployment_rates, 2010)))

# iv
def rate(empty):
    for i in empty:
        if label_order[-1] == i[0]:
            return i[1]

print(rate(unemployment_rates))

# v
def unique(empty):
    U_year = set({})
    for i in empty:
        U_year.add(i[0])
    return U_year

print(unique(unemployment_rates))

# vi
empty_3 = []
def rate_by_year(empty, empty_3, label_order):
    for i in label_order:
        for j in empty:
            if i == j[0]:
                empty_3.append(j[1])
    return empty_3

print(rate_by_year(unemployment_rates, empty_3, label_order))

# vii
def largest_rate(empty):
    x=sorted(empty)
    return x[-1]

print(largest_rate(empty_3))

# viii
empty_4 = []
def employment(empty):
    for i in empty:
        j=list(i)
        j[1]=100-j[1]
        x= (j[0],j[1])
        empty_4.append(x)
    return empty_4

print(employment(unemployment_rates))

# ix
def rate_7(empty):
    j = []
    for i in empty:
        if i[1] >= 7:
            j.append(i)
    return j

print(rate_7(unemployment_rates))

# x
empty_5 = []
empty_6 = {}
def count_element(empty):
    empty_5 = set(empty_3)
    for i in empty_5:
        empty_6.update({i : empty_3.count(i)})
    return empty_6

print(count_element((empty_3)))
