# Дано a b c є R . Замінити найбільше значення нулем.
'''
a = first_number float
b = second_number float
c = third_number float
max_1 -  максимальне значення
'''
# Ведення даних
first_number = float(input("Введіть значення а :"))
second_number = float(input("Введіть значення b :"))
third_number = float(input("Введіть значення c :"))
max_1 = 0
# порівняння
if max_1 <= first_number:
    first_number = max_1
    print('найбільше значення :', first_number)
elif max_1 <= second_number:
    second_number = max_1
    print('найбільше значення :', second_number)
elif max_1 <= third_number:
    third_number = max_1
    print('найбільше значення  :', third_number)
