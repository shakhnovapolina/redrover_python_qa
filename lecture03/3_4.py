print("# 4")
family_1 = input("Введите членов 1 семьи через запятую: ").split(',')
family_2 = input("Введите членов 2 семьи через запятую: ").split(',')
print(family_1 if len(family_1) > len(family_2) else family_2 if  len(family_1) < len(family_2) else 'Equal')