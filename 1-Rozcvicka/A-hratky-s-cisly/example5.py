def nsd(a,b):
    if b==0:
        return a
    else:
        return nsd(b,a % b)

x = y = 1

while y <= 1000000:
    tmp = x + y + nsd(x,y)
    x = y 
    y = tmp

print(y)