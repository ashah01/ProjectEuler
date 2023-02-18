"""
By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.
"""
for _ in range(int(input())):
    number = int(input())
    total = 0
    fibbo_prev = 1
    fibbo_curr = 2
    while fibbo_curr < number:
        tmp = fibbo_curr
        fibbo_curr = fibbo_curr + fibbo_prev
        fibbo_prev = tmp

        if fibbo_prev % 2 == 0:
            total += fibbo_prev
    
    print(total)
    
