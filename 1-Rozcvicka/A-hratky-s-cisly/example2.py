from math import sqrt

top_bound = 1000
numbers = set()
top = round(sqrt(top_bound))

for i in range(1,top):
    for j in range(1,top):
        for k in range(1,top):
            out = i**2 + j**2 + k**2
            if out < 1000:
                numbers.add(out)

# -1 because we don't count 0
print(str(1000 - len(numbers) - 1))