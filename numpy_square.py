import numpy as np 
import sys

system_p = open('array-final-2d.txt','r')
int_array = np.loadtxt(system_p, dtype=int, delimiter= ",")

# this creates the 50x50 matrix
mat_fifty= int_array.reshape(50,50)

# just a dash of spanish for labeling 
tres_tres = []
tres_matrix = []

for i in range(0,48):
    for j in range(0,48):
        tres_tres =tres_tres+ [mat_fifty[i:i+3, j:j++3]]

        tres_matrix_sum = np.sum([mat_fifty[i:i+3,j:j+3]])
        tres_matrix.append(tres_matrix_sum)

print(f'MAXIMUM SUM: {max(tres_matrix)}')
# print(len(tres_matrix))
print(np.argmax(tres_matrix))
loc = np.argmax(tres_matrix)//48, np.argmax(tres_matrix)%48
print(f'Location occurs at x-coord: {loc[0]}, y-coord: {loc[1]}')
# print(np.argmax(tres_matrix)//48, np.argmax(tres_matrix)%48)
# print(tres_tres[48*42+42])


# Ok yay now lets do the second part and get the most frequent sum that occurs

def get_most_freq(list_vals):
    tracker = 0
    tim_occur= list_vals[0]

    for i in list_vals:
        curr_freq = list_vals.count(i)
        if (curr_freq > tracker):
            tracker = curr_freq
            tim_occur = i
            # comment out line that shows how many times this sum occurs
            # if you want to see the number of time uncomment the line below
            # print(tracker)
    print(f'The number of times the most common sum occurs is: {tracker}')

    return tim_occur

freq_sum = get_most_freq(tres_matrix)
print(f'The most freq sum is: {freq_sum}')
# print(f'This occurs: {get_most_freq.tracker}')
