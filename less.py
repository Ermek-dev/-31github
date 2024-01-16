from main import multiply,SomeError

def user_multiply():
    try:
        first, second = list(map(int, input("Enter two number in comma:").split(",")))
    except ValueError as e:
        print(e)
        print("Enter only number in comma!")
    except SomeError as e:
        print(e.args)    
        print('You must enter only numbers separated by commas')
    else:
        try:
            result = multiply(first,second)
            print(result)
        except SomeError as e:
            print(e.args)




user_multiply()
# ----------------------------

# from distutils import extension


# def get_numbers_fron_list(path:str):
#     try:
#         with open("test.txt","r") as file:
#             numbers = list(map(int, file.read().split(",")))
#     except FileNotFoundError as e:
#         print(e.args)
#         file = open(path, "w")
#         file.close()
#     except ValueError as e:
#         print(e)
#         numbers = input("Enter the number in comma:")
#         with open(path,"w") as file:
#             file.write(numbers)
#     else:
#         return numbers        
#     return None
  

# path = "test.txt"
# numbers = get_numbers_fron_list(path)
# while numbers is None:
#     numbers = get_numbers_fron_list(path)

# import sys


# class InvalidFileExtensionError(Exception):
#     pass


# def validate_file_extension(path:str):
#     name, extension = path.split(".")
#     if extension !='txt':
#         raise InvalidFileExtensionError("Incorrect file ,wait the text *.txt")
#     return path    


# def get_numbers_fron_list(path:str):
#     try:
#         with open("test.txt","r") as file:
#             numbers = list(map(int, file.read().split(",")))
#             print(numbers)
#     except FileNotFoundError as e:
#         print(e.args)
#         file = open(path, "w")
#         file.close()
#     except ValueError as e:
#         print(e)
#         numbers = input("Enter the number in comma:")
#         with open(path,"w") as file:
#             file.write(numbers)
#     except InvalidFileExtensionError as e:
#         print(e.args)
#         file.exit()        
#     else:
#         return numbers        
#     return None
  

# FileNotFoundError
# path = "test.tt"
# numbers = get_numbers_fron_list(path)
# while numbers is None:
#     numbers = get_numbers_fron_list(path)
