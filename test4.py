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
                print(process_string)
# 
            else: 
                # process_string.append(copy_new_ex)
                process_string.append(copy_new_ex)
                process_string.append(False)
                print(process_string)
    



            
            
