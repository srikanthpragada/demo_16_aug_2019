
sum = 0

for i in range(1,6):
    try:
        n = int(input("Enter a number :"))
        sum += n
    except ValueError:
        pass
        # print("Sorry! Invalid number!")


print("Sum = ", sum)

