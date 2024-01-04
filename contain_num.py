user_input = input()
for i in user_input:
    if i.isdigit():
        print("Цифра")
        break
else:
    print("Цифр нет")

#
# def containNum(value):
#     for character in value:
#         if character.isdigit():
#             return "Цифра"
#     return "Цифр нет"
#
# user_input = input()
# print(containNum(user_input))
#
#
#
# s = input()
# digits = '0123456789'
#
# for c in s:
#     if c in digits:
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')
#
#
