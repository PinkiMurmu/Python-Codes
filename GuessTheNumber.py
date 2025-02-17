import random
import math

print("Hi welcome to the game, This is a number guessing game .\nYou will get number of chances according to the range . Let's start the game .")

m = int(input("Enter lowest : "))
n = int(input("Enter largest : "))
a=random.randint(m, n)
# print(a)

x=0
guess = math.log2(n-m+1)
# guess = round(guess,0)

while x<guess:
    x += 1
    num = int(input("Enter guessed number : "))
    if (num==a):
        print("Your number is ",a," and you guessed it right! in the ",x," attempt ")
        break
    elif x>=guess and num!=a:
        print("The number is ",a," better luck next time..")
    elif(num<a):
        print("Try again! You guessed too small..")
    elif(num>a):
        print("Try again! You guessed too high..")