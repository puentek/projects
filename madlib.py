import re 
import sys
data_info = open(sys.argv[1])

if data_info:
    # here lets take in the info we want from the input file
    next_data= data_info.read()
    # now we are splitting the info of the data we got 
    seperate_data = next_data.split(" ")
    for i in range(len(seperate_data)):
        if '[' in seperate_data[i]:
            # now here we seperate the [] 
            rem_bk = seperate_data[i].replace("[", "")
            rem_bk = rem_bk.replace("]", "")

            input_first = input(str("Please provide " + " "+ rem_bk))
            # here I just used a line from week 4 validhtml 
            data_3 = re.sub('\[.*?\]', str(input_first),data_2,1)
            data_2 = data_3
data_info.close()


# steps 

# 1. print multi line file that reads and print to another file 
# 2. Find and print things in brackets 
# 3. Save all things to a list and print out list 
# 4. Prompt user for replacement 
# 5. Save input to a new list 
# 5.1. Replace stuff w/ brackets w/ hardcoded things
# 6 Replace w/ things from user 







