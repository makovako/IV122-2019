def collatz_steps(n):
    number = n
    count = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        count += 1
    return count

numbers = set()
max_count = 0

for i in range(1,10000):
    curr_count = collatz_steps(i)
    if curr_count > max_count:
        numbers.clear()
        numbers.add(i)
        max_count = curr_count
    elif curr_count == max_count:
        numbers.add(i)

print("Numbers {} need maximum number of steps {}.".format(numbers, max_count))