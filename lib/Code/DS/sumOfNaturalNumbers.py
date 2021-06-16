import time

timestamp1  = time.time()

numbers = 100
total = 0

for value in range(1,numbers+1):
    total = total+value

print("Sum of 100 natural numbers is :", total)

timestamp2 = time.time()

print(timestamp2-timestamp1)