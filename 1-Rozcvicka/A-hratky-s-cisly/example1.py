def dividers(n):
    div = 0
    for i in range(1,n+1):
        if n % i == 0:
            div += 1
    return div

max_div = 0
numbers = []
for i in range(1,10000):
    div = dividers(i)
    if div > max_div:
        max_div = div
        numbers.clear()
        numbers.append(i)
    elif div == max_div:
        numbers.append(i)
        
print("Most dividers {} have numbers: {}".format(str(max_div),numbers))