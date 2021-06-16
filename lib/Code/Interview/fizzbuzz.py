'''
In Fizzbuzz you've given a list of integers. Your task is to do the following.
1. Replace all integers that are evenly divisible by 3 with "fizz"
2. Replace all integers that are divisible by 5 with "buzz"
3. Replace all integers that are divisible by both 3 & 5 with "fizzbuzz"
'''
# Solving using enumerate() method:
numbers = [45,22,14,65,97,72]

for i, num in enumerate(numbers):
    print("Index :",int(i),"Value :",num)

# Solving using range() method:

# numbers = [45,22,14,65,97,72]

# for i in range(len(numbers)):
#     if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
#         numbers[i] = "fizzbuzz"
#     elif numbers[i] % 3 == 0:
#         numbers[i] = "fizz"
#     elif numbers[i] % 5 == 0:
#         numbers[i] = "buzz" 
