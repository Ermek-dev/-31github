# функция перевода градусов Фаренгейта в градусы Цельсия
def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result

# основная программа
temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
celsius = convert_to_celsius(temp)
print(celsius)  # градусы Цельсия