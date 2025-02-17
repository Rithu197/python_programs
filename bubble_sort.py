def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so we skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

# Input from user
input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Sorting the list using bubble sort
sorted_list = bubble_sort(input_list)

print("Sorted list:", sorted_list)
