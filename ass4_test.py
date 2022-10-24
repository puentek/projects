import re 
# txt = ['''<a><b><c></c></b></a>''',
#  '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
#  '''<foo><bar></bop></bar></foo>''',
#  '''<foo><bar></bar></foo></foo>''',
#  '''<foo><bar></foo></bar>''']

example_set = ['''<a><b><c></c></b></a>''',
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
    
    wait = example_set[k].split('>')
    for j in range(len(wait)):
        wait[i] = wait[j]+'>'

    new_ex.append(wait)
# issue here printing extra >  
# print(new_ex)

    for k in range(len(new_ex)):
        char = re.compile(r'<.*>') 
        # now lets look for the matching object aka mo
        # having an issue here 
        mo = char.search(new_ex[k])
        mg = mo.group()
        # print(mg)
        if char not in mg:
            error= False 
            new_ex.append(error)
        else:
            success = True
            new_ex.append(success)





    # print(new_ex)
# print(new_ex)


# clean_list = []
# list = example_set
# char = re.compile(r'<.*>')
# mo = char.search(list[1])
# mg = mo.group() 
# print(mg)

# clean_list.append()
    

