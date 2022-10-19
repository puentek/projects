txt = ['''<a><b><c></c></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></foo></bar>''']
commas_added = '>, '.join(txt[0].split('>'))
print(commas_added)


# joined_string = ",". join(example_set[0])
# print(joined_string) 
# print(len(example_set))

# res = (format (example_set[0], ', d'))
# print(str(res))