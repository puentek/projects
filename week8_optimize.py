from time import process_time
import random
array = []
n = 1000
for i in range(n):
    array.append(random.randint(-200,300))

start = process_time() 

# new_list = list 

# Implementing Insertion sort 
for i in range(1, len(array)):
    # This is the element we want to position in its
    # correct place
    key_item = array[i]

    # Initialize the variable that will be used to
    # find the correct position of the element referenced
    # by `key_item`
    j = i - 1

    # Run through the list of items (the left
    # portion of the array) and find the correct position
    # of the element referenced by `key_item`. Do this only
    # if `key_item` is smaller than its adjacent values.
    while j >= 0 and array[j] > key_item:
        # Shift the value one position to the left
        # and reposition j to point to the next element
        # (from right to left)
        array[j + 1] = array[j]
        j -= 1

    # When you finish shifting the elements, you can position
    # `key_item` in its correct location
    array[j + 1] = key_item

print(array)
end = process_time() 
print("Time elapsed was " + str(end-start))
