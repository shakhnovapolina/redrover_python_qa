# 5
print("# 5")
film = {'title': "the lord of the rings", 'director': "piter jackson", 'year': 2003, 'budget': 1000000,
        'main_actor': "Elijah Wood", 'slogan': "One Ring to rule them all"}

print(*film.keys(), sep=", ")
print(*film.values(), sep=", ")
print(*film.items(), sep=", ")

# 6
print("# 6")
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))

# 7
print("# 7")
double_list = [1, 2, 3, 4, 5, 3, 2, 1]
print(list(set(double_list)))

# 8
print("# 8")
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2) and set1.issuperset(set2))
