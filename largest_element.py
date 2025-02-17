input_string = input("Enter numbers separated by spaces: ")

# Convert the string into a list of numbers (integers in this case)
my_list = [int(x) for x in input_string.split()]

largest= my_list[0]

for x in my_list:
  if(x>largest):
        largest= x
print(largest)
