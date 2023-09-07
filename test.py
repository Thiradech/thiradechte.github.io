def sum1(x):
    if x == 1:
        return 1
    else:
        x += sum1(x-1)
    return x
print(sum1(3))
        