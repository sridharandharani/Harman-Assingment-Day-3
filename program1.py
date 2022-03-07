# Write a python program to square and cube every number in a given list of integer in lambda

num_list = [x for x in range(1,11)]
square_list = list(map(lambda i: (i ** 2) , num_list))
print("The square of the list is :" , square_list)
cube_list = list(map(lambda i : (i**3) , num_list))
print("The cube of the list is : " , cube_list)