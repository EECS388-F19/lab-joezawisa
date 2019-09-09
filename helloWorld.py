import random

print("Joe")

sum = 0
for i in range(2):
    number = random.randint(0, 100)
    print(number)
    sum += number

print("Sum = " + str(sum))
print("Average = " + str(sum/2))

