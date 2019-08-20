sum = 0

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    sum += num

print(f"Sum = {sum}")
