
sum = 0
i = 1;
while i <= 5:
    try:
        n = int(input("Enter a number :"))
        sum += n
        i += 1
    except ValueError:
        print("Sorry! Invalid number! Please enter valid number.")


print("Sum = ", sum)

