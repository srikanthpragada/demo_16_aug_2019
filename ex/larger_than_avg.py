def higher_than_avg(*nums):
    avg = sum(nums) / len(nums)
    l = []
    for n in nums:
        if n > avg:
            l.append(n)

    return l


l = higher_than_avg(10, 20, 33, 32, 11, 22)
print(l)
