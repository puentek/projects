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

new_ex = []
for k in range(len(example_set)):
    
    wait = example_set[k].split('>')
    
    wait = wait[:-1]
    # print(wait)
    for i in range(len(wait)):
        wait[i] = wait[i]+'>'
    

    new_ex.append(wait)
print(new_ex)

# char = re.compile(r'<.*>') 
#         # now lets look for the matching object aka mo
#         # having an issue here 
# mo = char.search(new_ex[k])
# mg = mo.group()
        # print(mg)
                                            


