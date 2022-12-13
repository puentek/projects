# Created by Karina Puente Oct 2022

''' Implementation of teo different functions: 
1. abs_sort(list) : This takes in an unsorted list and returns a sorted list according to the absolute sorting rules detailed above. The original list which is passed in should be unchanged 
2. abs_sort_in_place(list): This performs the same sort but does so in place. This means that the original list, after the function is complete, should now be sorted. It does not return anything, the original list is the one that ends up sorted.'''

import time

# start = time.process_time()
def abs_sort(list):
    start = time.process_time() 
    new_list = list 
    for i in range(len(new_list)-1):
        for  j in range(len(new_list)-1):
            if (abs(new_list[j]) > abs(new_list[j+1])):
                new_list[j+1], new_list[j] = new_list[j], new_list[j+1]
            
            elif (abs(new_list[j]) == abs(new_list[j+1])) & (new_list[j] > new_list[j+1]):
                ""

            elif (abs(new_list[j]) == abs(new_list[j+1])) & (new_list[j] < new_list[j+1]):
                new_list[j+1],new_list[j] = new_list[j], new_list[j+1]
            
            else: 
                ""
    # I'm just printing this out for my sanity 
    # print(f'This is the abs_sort new_list: {new_list}')
    end = time.process_time()
    print("Time elapsed was " + str(end-start))
    return new_list
# This is the original list that will be passed through the function 
list = [5, -2, 10, -13, 2, 20]
abs_sort(list)


# This is the second part of the assignment 
def abs_sort_in_place(org_list):
    # org_list = org_list
    for i in range(len(org_list)-1):
        for  j in range(len(org_list)-1):
            if (abs(org_list[j]) > abs(org_list[j+1])):
                org_list[j+1], org_list[j] = org_list[j], org_list[j+1]
            
            elif (abs(org_list[j]) == abs(org_list[j+1])) & (org_list[j] > org_list[j+1]):
                ""

            elif (abs(org_list[j]) == abs(org_list[j+1])) & (org_list[j] < org_list[j+1]):
                org_list[j+1],org_list[j] = org_list[j], org_list[j+1]
            
            else: 
                ""
    # I'm just printing this out for my sanity 
    # print(f'This is the abs_sort_in_place(org_list): {org_list}')
    return org_list

# this is the original list
org_list = [5, -2, 10, -13, 2, 20]
abs_sort_in_place(org_list)
# end = time.process_time()
# print("Time elapsed was " + str(end-start))