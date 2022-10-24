from email.errors import NoBoundaryInMultipartDefect
import re 
# txt = ['''<a><b><c></c></b></a>''',
#  '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
#  '''<foo><bar></bop></bar></foo>''',
#  '''<foo><bar></bar></foo></foo>''',
#  '''<foo><bar></foo></bar>''']

example_set = ['''<a><b></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></foo></bar>''']


# use regular expressions; re.split
#  search for the tag and return what was found; 
# 
# . is any or no character 
#  * is 0 or more occurences of them 


new_ex = []
for i in range(len(example_set)):
    wait = example_set[i].split('>')
    wait = wait[:-1]
    for j in range(len(wait)):
        wait[j] = wait[j]+'>'
    new_ex.append(wait)
        
    # iterate through elements 1 by 1
    #   identify the front slash
    #   say you find the slash at pos 5
    #   check position 4 if it has the pairing opening tag
    #   if its there, procecss next tag
    #   if not, Return False
    #   

    process_string = []
    copy_new_ex = new_ex

    for k in range(len(new_ex[i])):
        char = re.compile(r'<.*>')
        mo = char.search(new_ex[i][k])
        slash = re.compile(r'</.*>')
        ms = slash.search(new_ex[i][k])
        match_let = '[a-z]'
        print(f'mo: {mo}')
        print(f'ms: {ms}')
        #
        if ms is not None: 
            # mo = char.search(new_ex[i][k])
            # if mo[k] == mo[k-1]:
            # print(f'mo: {mo}')
            print(f'update_ms: {ms}')
            print(new_ex[i][k],new_ex[i][k-1])
            #  have to check if the letter is the same 
            # Issue in having the / there

            if new_ex[i][k] == new_ex[i][k-1]:
                process_string.append(True)


            # process_string = new_ex
            new_ex = new_ex[:-1]
            
            for l in range(len(new_ex[i][k])):
                new_ex = new_ex[:-1]
            process_string.append(True)

            
        else: 
            process_string.append(False)

# example_set.append(process_string)
            


            # print(char) 
            # print(new_ex[i][k])
            # now lets look for the matching object aka mo
            # # mo_s = slash.search(new_ex[i][k])
            # mo = char.search(new_ex[i][k])
            # process_string = mo.group
            # process_string= process_string[:-1]
              


        # mo_s = slash.search(new_ex[i][k])
        # mg = mo.group()


        # print(mg)
        # # if char not in mg:
        #     # error= False 
        #     process_string.append(new_ex[i][k],False)
        #     print(process_string)
        # else:
        #     # success = True
        #     process_string.append(new_ex[i][k],True)
        #     print(process_string)
        
            # return process_string





    # print(new_ex)
# print(new_ex)


# clean_list = []
# list = example_set
# char = re.compile(r'<.*>')
# mo = char.search(list[1])
# mg = mo.group() 
# print(mg)

# clean_list.append()
    

