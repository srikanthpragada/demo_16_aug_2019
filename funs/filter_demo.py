def isodd(n):
    # print("Value = ", n)
    return n % 2 == 1


num = [10, 20, 30, 44, 55, 6, 77, 99]
oddnums = filter(isodd, num)
# for n in oddnums:
#     print(n)

oddnums = filter(lambda n: n % 2 == 1, num)
for n in oddnums:
    print(n)
