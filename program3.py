# Write a program using function to check whether a string is palindrome or not

def stringispalindrome(x):
    i = 0
    for i in range(len(x)):
        if x[i] != x[-1+i]:
            print("The string is not palindrome")
            break
        else:
            print("The string is palindrome ")
            break

string = input("Enter the string :")
stringispalindrome(string)
