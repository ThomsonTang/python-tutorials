# -*- coding: utf-8 -*-

""" 1.1 Unpacking a Sequence into Separate Variables
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.
The only requirement is that the number of variables and structure match the sequence.

Unpacking actually works with any object that happens to be iterable, not just tuples or lists. This includes strings,
files, iterators, and generators.
"""

p = (4, 5)
x, y = p
print(x, y)

data = ['Name', 59, 123.4, (2017, 1, 1)]
name, amount, price, date = data
print(name)
print(amount)
print(price)
print(date)

name, amount, price, (year, month, day) = data
print(year)
print(month)
print(day)

"""if there is a mismatch in the number of elements, you'll get an error.
for example:

x, y, z = p
print z

"""

s = "Hello"
a, b, c, d, e = s
print(a, b, c, d, e)

"""Pick a throwaway variable name to discard certain values when unpacking.
"""
teams = ["warriors", "spurs", "rockets", "jazz"]
_, s, _, j = teams
print(s)
print(j)
