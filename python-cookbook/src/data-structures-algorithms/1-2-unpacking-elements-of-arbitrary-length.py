"""1.2 Unpacking Elements from Iterables of Arbitrary Length
Python "star expressions" can be used to address this problem.
"""

# drop the first and last homework grades, and only average the rest of them.
"""
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
"""

record = ('Tom', 'thomson@qq.com', '123-456-789', '111-222-333')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

# the starred variable can also be the first one in the list.
""" for example:

*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
return avg_comparison(trailing_avg, current_qtr)

"""

*trailing, current = [10, 8, 7, 8, 5, 10, 3]
print(trailing)
print(current)

# It is worth noting that the star syntax can be especially useful when iterating over a sequence of tuples of varying
# length.
records = [
    ('tom', 1, 2),
    ('lisa', 'pretty'),
    ('tom', 3, 4),
]


def do_tom(x, y):
    print('tom', x, y)


def do_lisa(s):
    print('lisa', s)


for tag, *args in records:
    if tag == 'tom':
        do_tom(*args)
    elif tag == 'lisa':
        do_lisa(*args)

# Use the star syntax when combined with certain kinds of string processing operations
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print(uname, homedir, sh)

# unpack values and throw them away
record = ('tom', 30, 175, (1, 1, 1987))
name, *_, (*_, year) = record
print(name, year)

# There is a certain similarity between star unpacking and list-processing features of various functional languages.
items = [1, 2, 3, 4]
head, *tail = items
print(head, tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))
