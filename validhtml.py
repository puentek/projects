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



i = 0
ex0 = example_set[i+1]
spt= '>, '.join(ex0.split('>'))
print(spt)


# def valid_html(test_strings):
#     for i in range(example_set):
        # print(example_set[i])

