import re
# Task for this code
# 1. make sure the stuff w/out the <> is not printed just returned 
    #  This would look something like this: 
    # ['<a>', '<b>', '<c>', '</c>', '</b>', '<d>', '</d>', '</a>']
# 2. make sure the string is valid 

#  This is supposed to be the output you should be getting 
# [('<a><b><c></c></b></a>', True),
#  ('<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>', True),
#  ('<foo><bar></bop></bar></foo>', False),
#  ('<foo><bar></bar></foo></foo>', False),
#  ('<foo><bar></foo></bar>', False)
# ]

example_set = ['''<a><b><c></c></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></foo></bar>''']

# assignment requirements do not delete asd, srings returned in the end don't have to be deleted
# def valid_html(test_strings):
#     

# new_ex = []
# for k in range(len(example_set)):
    
#     wait = example_set[k].split('>')
    
#     wait = wait[:-1]
#     # print(wait)
#     for i in range(len(wait)):
#         wait[i] = wait[i]+'>'
    

#     new_ex.append(wait)
# print(new_ex)

# # char = re.compile(r'<.*>') 
# #         # now lets look for the matching object aka mo
# #         # having an issue here 
# # mo = char.search(new_ex[k])
# # mg = mo.group()
#         # print(mg)
                                            
# new_ex = []
# for i in range(len(example_set)):
#     wait = example_set[i].split('>')
#     wait = wait[:-1]
#     for j in range(len(wait)):
#         wait[j] = wait[j]+'>'
#     new_ex.append(wait)
        
#     # iterate through elements 1 by 1
#     #   identify the front slash
#     #   say you find the slash at pos 5
#     #   check position 4 if it has the pairing opening tag
#     #   if its there, procecss next tag
#     #   if not, Return False
#     #   

#     process_string = []
#     copy_new_ex = new_ex.copy()
#     # ['<a>', '<b>', '<c>', '</c>', '</b>', '</a>] 
#     # len>0
#     # loop -> find / break (3)
#     # remove the elements (2, 3)
#     # ['<a>', '<b>', '</b>', '</a>] 
#     # len > 0
#     # loop -> find / break (2)
#     # remove the elements (1, 2)
#     # ['<a>', '</a>] 
#     # len > 0
#     # loop -> find / break (1)
#     # remove the elements (0, 1)
#     # [] 
    
# #while len(new_ex) >0:
#     # for k in range(len(new_ex[i])):
#     while len(new_ex) > 0: 
#         # char = re.compile(r'<.*>')
#         # mo = char.search(new_ex[i])
#         # mg = mo.group()

#         slash = re.compile(r'</?.*>')
#         # slash = re.compile(r'</.*?>')
#         ms = slash.search(new_ex[i])
#         mg_s = ms.group()
#         # match_letter= re.compile(r'[a-z]..')
#         # match_let = '[a-z]'
#         # print(f'mo_group: {mg}')
#         # print(f'ms: {mg_s}')

#         if ms is not None:
#             # print(f'update_ms: {ms}')
#             # print(new_ex[i][k],new_ex[i][k-1])
#             tup_mg_mgs = new_ex[i],new_ex[i-1]
#             # this removes the slash 
#             ch = '/'
#             tup_mg_mgs = [elem.replace(ch,'') for elem in tup_mg_mgs]
#             # print(tup_mg_mgs)
#             # print(tup_mg_mgs[0], tup_mg_mgs[-1])
#             if tup_mg_mgs[0] == tup_mg_mgs[-1]:
#                 # remove pait in the list : how to do that 
#                 # remove both elements 
#                 new_ex[i].pop(k)
#                 new_ex[i].pop(k-1)
#                 print(new_ex[i],k)
#                 # new_ex = 

#         # process_string.append((copy_new_ex,True))
                
#                 # print(process_string)

#             else: 
#                 process_string.append((copy_new_ex,False))
                
#                 # process_string.append(False)
#         print(len(new_ex[i]))
#     process_string.append((copy_new_ex,True))    
#     print(process_string)
    



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
        mg = mo.group()

        slash = re.compile(r'</?.*>')
        # slash = re.compile(r'</.*?>')
        ms = slash.search(new_ex[i][k])
        mg_s = ms.group()
        # match_letter= re.compile(r'[a-z]..')
        # match_let = '[a-z]'
        # print(f'mo_group: {mg}')
        # print(f'ms: {mg_s}')

        if ms is not None:
            # print(f'update_ms: {ms}')
            # print(new_ex[i][k],new_ex[i][k-1])
            tup_mg_mgs = new_ex[i][k],new_ex[i][k-1]
            # this removes the slash 
            ch = '/'
            tup_mg_mgs = [elem.replace(ch,'') for elem in tup_mg_mgs]
            # print(tup_mg_mgs)
            # print(tup_mg_mgs[0])
            if tup_mg_mgs[0] == tup_mg_mgs[1]:
                process_string.append(copy_new_ex)
                process_string.append(True)
                # print(process_string)
# 
            else: 
                # process_string.append(copy_new_ex)
                process_string.append(copy_new_ex)
                process_string.append(False)
                # print(process_string)
    

