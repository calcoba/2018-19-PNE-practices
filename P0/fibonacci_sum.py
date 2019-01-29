def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    for i in range(n+1):
        count += n1
        n1, n2 = n2 ,(n1+n2)
    return count


term = int(input("Please enter e number to obtain the Fibonacci term:"))
fb_term = fibonacci(term)
print("The sume of the first", term, "numbers of the Fibonacci series is:", fb_term)