def sum(n):
    total_sum = 0
    for i in range(n):
        total_sum += (i+1)
    return total_sum


number = int(input("Please enter a number:"))
total_sum = sum(number)
print("The sum of the first", number, "is:", total_sum)