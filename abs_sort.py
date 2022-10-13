

''' Implementation of teo different functions: 
1. abs_sort(list) : This takes in an unsorted list and returns a sorted list according to the absolute sorting rules detailed above. The original list which is passed in should be unchanged 
2. abs_sort_in_place(list): This performs the same sort but does so in place. This means that the original list, after the function is complete, should now be sorted. It does not return anything, the original list is the one that ends up sorted.'''


# list = [5, -2, 10, -13, 2, 20]

# def swap_num(num1, num2):

def abs_sort(list):
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
    print(new_list)
    return new_list

abs_sort([5, -2, 10, -13, 2, 20])