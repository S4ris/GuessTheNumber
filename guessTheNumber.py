import random
import time

print("Hello to Guess The Number game")
time.sleep(5)
print("Give me few seconds. I will draw a number")
x = random.randint(0,100) #Draws a number
time.sleep(10)

print("I have select my number. Now try to guess it")
count = 0 #Approaches count

while(True):
    num = int(input())
    count+=1
    if(num == x):
        print("Bravo! You guessed the number! Number of approaches:", count)
        break
    else: 
        if(num > x):
            print("My number is smaller")
        else:
            print("My number is bigger")