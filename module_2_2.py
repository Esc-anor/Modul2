first = int(input('Введите первое чсисло: '))
second = int(input('Введите второе число: '))
third = int(input('Ввведите третье число: '))
if first==second==third:
    print(3)
elif first!=second==third:
    print(2)
elif first==second!=third:
    print(2)
elif second!=third==first:
    print(2)
else:
    print(0)
