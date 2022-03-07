# Write a python program to calculate length of the string from the user and save that length of the string in data.txt

string = input("Enter a string :")
length = len(string)
file = open("data.txt", "w")
data = file.write(str(length))

