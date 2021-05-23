items = [1,2,3,4,5,6]
# yeh ek input hy joh store karta hy apne items ko

def all_cubes(items):
    for item in items:
        result = pow(item,3)
    # space complexity is 0(n), kyunki yahan number of operations depend on number of inputs.
    # Agar mere pass 6 elements(inputs) hy tho, mere pass 6 six different result hy, jo ki store karne ke liye.
    
    print(result)

all_cubes(items)

# items = [1,2,3,4,5,6]
# # yeh ek input hy joh store karta hy apne items ko

# result = []

# def all_cubes(items):
#     for item in items:
#         result.append(pow(item,3))
#     # space complexity is 0(n), kyunki yahan number of operations depend on number of inputs.
#     # Agar mere pass 6 elements(inputs) hy tho, mere pass 6 six different result hy, jo ki store karne ke liye.
    
#     print(result)

# all_cubes(items)

# num_list = [1,2,3,4,5,6,7,8,9] #0(1)

# def randomFunction(num_list):

#     totalCount = 0;
#     for num1 in num_list: #time complexity is 0(n^2)
#         for num2 in num_list:
#             print(num1, num2)
#             totalCount+=1
#     return totalCount

# print("Total number of operations performed is", randomFunction(num_list))