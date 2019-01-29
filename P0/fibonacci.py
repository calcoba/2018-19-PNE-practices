def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        n1, n2 = n2 ,(n1+n2)
    return n1

while True:
    term = int(input("Please enter e number to obtain the Fibonacci term:"))
    fb_term = fibonacci(term)
    print(fb_term)