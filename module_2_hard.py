def generate_password(n):
    result = ""
    for i in range(1, n):
        if i > n // 2:
            break
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)
                break

    return result


number = 0
while number < 3 or number > 20:
    number = int(input("Введите число для пароля от 3 до 20: "))
password = generate_password(number)
print(f"Для числа {number}: Нужный пароль - {password}")
print("Наконец-то! Вы выбрались из ловушки!")
