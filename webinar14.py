
def bread(obj, food=""):
    def wrapper():
        print("</---------\\>")
        func(obj, food)
        print("<\\---------/>")
    return wrapper


def fill(*args):
    def decor(func):
        def wrapper(obj,food=""):
            middle_index = len(args)//2
            for arg in args[:middle_index]:
                print(f"~{arg}~".center(14))
            func(obj,food)
            for arg in args[middle_index:]:
                print(f"~{arg}~".center(14))
        return wrapper
    return decor

# @bread
# @fill("Salad","tomato")
# def create_burger(food:str = "--Cutlet--"):
#     print(food.center(14))






# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("Arter function")
#     return wrapper
#
#
# @decorator
# def hi():
#     print("Hi")
# hi()
# ------------------
