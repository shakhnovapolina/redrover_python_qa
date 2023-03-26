import functools

my_list = [20, -3, 15, 2, -1, -21]
second_list = list(filter(lambda x: x > 0, my_list))
print(second_list)

multipl = functools.reduce(lambda x, y: x * y, my_list)
print(multipl)