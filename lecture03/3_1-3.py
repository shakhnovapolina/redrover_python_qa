# 3.1.
print("# 1")
my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[2], sep=', ')

# 3.2
print("# 2")
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
num = 0
for i in list_1:
    if type(i) is int:
        num += i
    elif type(i) is str and 'a' in i:
        print(i, sep=" ")
print(num)

# 3.3.
print("# 3")
list_2 = ['cat', 'dog', 'horse', 'cow']
print(tuple(list_2))
