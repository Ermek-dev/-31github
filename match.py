# from enum import Enum
# class Color(Enum):
#     RED = 0
#     GREEN = 1
#     BLUE = 2
#
#
# def hi(color):
#     match color:
#         case Color.RED:
#             print("Это красный")
#         case Color.GREEN:
#             print("Трава зеленая")
#         case Color.BLUE:
#             print("Небо синее")


user_input = int(input("Enter the number from 1 to 3:\n>"))
# if user_input == "1":
#     print("Hi")
# elif user_input == "2":
#     print("Bye")
# elif user_input == "3":
#     print("Ok")
# else:
#     print("Error")


match user_input:
    case 1:
        print("Wake")
    case 2:
        print("Eat")
    case 3:
        print("Drink")
    case _:
        print("Hi")
