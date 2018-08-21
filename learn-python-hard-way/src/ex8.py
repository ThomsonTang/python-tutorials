# Printing, Printing

formatter = "%r %r %r %r"
another_formatter = "%s %s %s %s"

print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % ("one", "two", "three", "four"))
print(another_formatter % ("one", "two", "three", "four"))
print(formatter % (formatter, formatter, formatter, formatter))
