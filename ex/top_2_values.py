def top2(values):
    first = max(values)
    second = max([v for v in values if v != first])
    return (first, second)


l = [29, 60, 80, 90, 90, 76, 55]

print(top2(l))
