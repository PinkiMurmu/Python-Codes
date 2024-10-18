# Testing a number is prime or not

num = 11
# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# Finding the number prime or not using recursion

from math import sqrt

# prime function to check given number prime or not
def Prime(number, itr):  
    # base condition
    if itr == 1 or itr == 2:  
        return True
      # if given number divided by itr or not
    if number % itr == 0:  
        return False
      # Recursive function Call
    if Prime(number, itr - 1) == False:  
        return False

    return True

num = 13

itr = int(sqrt(num) + 1)

print(Prime(num, itr))
