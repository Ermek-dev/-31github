
number = int(input())
if number<=9:
    for i in range(number):
        for j in range(3):
            print(number,end=' ')
        print(sep=' ')
else:
    print("Error!!!")