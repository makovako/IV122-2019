def dividers(n):
    div = 0
    for i in range(1,n+1):
        if n % i == 0:
            div += 1
    return div

sum = 0

for i in range(1,1000):
    if dividers(i) == 2 and not "3" in str(i):
        sum += i

print(sum)