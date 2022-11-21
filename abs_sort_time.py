from time import process_time
import random
list = []
org_list = []
# Change n to whatever number you want 
n = 2000 
for i in range(n):
    list.append(random.randint(-200,300))

start = process_time() 

# Replace the below code with your program to time it
new_list = list 
for i in range(len(new_list)-1):
    # start = time.process_time() 
    for  j in range(len(new_list)-1):
        if (abs(new_list[j]) > abs(new_list[j+1])):
            new_list[j+1], new_list[j] = new_list[j], new_list[j+1]
        
        elif (abs(new_list[j]) == abs(new_list[j+1])) & (new_list[j] > new_list[j+1]):
            ""

        elif (abs(new_list[j]) == abs(new_list[j+1])) & (new_list[j] < new_list[j+1]):
            new_list[j+1],new_list[j] = new_list[j], new_list[j+1]
        
        else: 
            ""
print(new_list)

end = process_time() 
print("Time elapsed for new_list was " + str(end-start))


from time import process_time
import random
org_list = []
n = 1000
for i in range(n):
    org_list.append(random.randint(-200,300))

start_org = process_time() 
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
    # return org_list
print(org_list)
# Replace the above code with your program to time it

end_org = process_time() 
print("Time elapsed for org_list was " + str(end_org-start_org))