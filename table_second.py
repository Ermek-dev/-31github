number = int(input())
if number<=9:
    for i in range(1,number+1):
        for j in range(5):
            print(i,end=' ')
        print(sep=' ')
else:
    print("Error!!!")
