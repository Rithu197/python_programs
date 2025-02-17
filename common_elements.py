input_string1= input("enter the first list of elemnts")
input_string2= input("enter the second list of elemt numbers")
my_list1 = [int(x) for x in input_string1.split()]

my_list2 = [int(x) for x in input_string2.split()]

for i in my_list1:
    for j in my_list2:
        if(i==j):
            print(i,' is common element')
            break

