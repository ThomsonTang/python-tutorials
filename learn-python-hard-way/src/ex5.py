# More Variables and Printing

my_name = 'Thomson Tang'
my_age = 30
my_height = 174  # cm
my_weight = 70  # kg

print("Let's talk about %s." % my_name)
print('Let"s talk about %s.' % my_name)
print("Let's talk about %s." % my_name)

print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# The only catch is that if you want multiple formats in your string to print multiple variables, you need to put
# them inside ( ) (parenthesis) separated by , (commas). print "If I add %d, %d, and %d I get %d." % my_age,
# my_height, my_weight, my_age + my_height + my_weight
