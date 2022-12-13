from time import process_time
import random
list = []
org_list = []
n = 4000
for i in range(n):
    list.append(random.randint(-200,300))

start = process_time() 
# Lets implement an optimized code using the inserting sort practice

for i in range(1, len(list)):
    # here we want to use indicated_item to position it to the right place
    indicated_item = list[i]

    # Now lets start j and i similar to how we had in the original abs_sort but 
    # this time use j and i to subtract 
    j = i-1
    
    # the next step is to go through the list of numbers generated earlier 
    # this is done to find the correct position the number it is supposed to be in 

    while j >= 0 and list[j] > indicated_item:
        list[j+1] = list[j]
        j -= 1
        #  yay optimization !!

    list[j+1] = indicated_item

print(list)
end = process_time()
print("Time elapsed for new_list was " + str(end-start))



for i in range(n):
    org_list.append(random.randint(-200,300))

 
# Lets implement an optimized code using the inserting sort practice
start_org = process_time()
for i in range(1, len(org_list)):
    # here we want to use indicated_item to position it to the right place
    # start_org = process_time()
    indicated2_item = org_list[i]

    # Now lets start j and i similar to how we had in the original abs_sort but 
    # this time use j and i to subtract 
    j = i-1
    
    # the next step is to go through the list of numbers generated earlier 
    # this is done to find the correct position the number it is supposed to be in 

    while j >= 0 and org_list[j] > indicated2_item:
        org_list[j+1] = org_list[j]
        j -= 1
        #  yay optimization !!

    org_list[j+1] = indicated2_item

print(org_list)
end_org = process_time()
print("Time elapsed for org_list was " + str(end_org-start_org))