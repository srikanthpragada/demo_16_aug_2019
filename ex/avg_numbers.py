sum = count = 0
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num < 0:
        continue

    count += 1
    sum += num

print(f"Average  = {sum/count}")
