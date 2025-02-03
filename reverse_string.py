String= input("enter the string: ")
s=String.lower()
reversed_string= s[::-1]
if(s==reversed_string):
    print(String," is palindrome")
else:
    print(String, "is not palindrome")