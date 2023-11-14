numbers = [1,2,3,4,5,6]
def multiply(number):
    result = list()
    for number in numbers:
        result.append(number*number)
    return result

print(numbers)
print(multiply(numbers))
