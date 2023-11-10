number = int(input())
if number<=9:
    for i in range(1,number+1):
        for j in range(1,10):
            print(i,'+',j,'=',i+j)
        print()
