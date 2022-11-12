from pprint import pp 
import requests
import json 
import html 
import random 


# lets load some data !! 
# Here lets make sure to have url of different categories
# url_1 = "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=multiple"
# dict_urls = {}
dict = { 11: "Entertainment: film", 21: "Sports", 27: "Animals" }

print("Welcome to Trivia Bot 5000, Please Select a Category of Trivia: \n 11. Entertainment: film \n 21. Sports \n 27. Animals  ")
category_selected = input()
print(f'You picked {dict[int(category_selected)]}, how many questions do you want?')
num_questions = input()
url_trivia= (f'https://opentdb.com/api.php?amount={str(num_questions)}&category={str(category_selected)}&difficulty=easy&type=multiple')
url_trivia_link = url_trivia

headers = {'Accept': 'application/vnd.opentdb.v3+json'}
r =  requests.get(url_trivia_link,headers=headers)
response_dict = r.json()


repo_dicts = response_dict['results']

repo_dict = repo_dicts[1]
correct_count = 0
# a = int(num_questions)
# b = 0
# for a in range(int(num_questions)):
#     print(f"Question: {html.unescape(repo_dict['question'])}")

for repo_dict in repo_dicts:
    print(f"Question: {html.unescape(repo_dict['question'])}")
    choices = html.unescape(repo_dict['incorrect_answers'])
    choices.append(html.unescape(repo_dict['correct_answer']))
    dict_choices = {"1": choices[0], "2": choices[1], 
                "3": choices[2], "4": choices[3]}
    values = list(dict_choices.values())

    for count, value in enumerate(values,start=1): 
        print(count, value)

    your_choice = input()

    def get_key(val):
        for key, value in dict_choices.items():
            if val == value:
                return key

        return "key doesn't exist"
    
    # correct_count = 0

    if str(your_choice) == str(get_key(choices[3])):
        print("That is correct")
        correct_count = correct_count + 1
        # print(f"correct_count: {correct_count}")

    else:
        print(f"That is incorrect. The correct answer is : {choices[3]}")
    
print(f"Your game is over, you got {str(correct_count)} out of {str(num_questions)} correct")
print("Thanks for playing!!")

# def w7(num_questions):
#     a = int(num_questions)
#     b = int(num_questions)+1
     
#     if a < b: 
#         p = print(f"Question: {html.unescape(repo_dict['question'])}")    
#         a = a-1
#         return p
#         # print(a)
#     elif a == 0: 
#         print('you are done')
#     # else:
#     #     print("fix")
#     # a = a-1
#     # print(a)

# print(w7(num_questions))

# while a != b: 



    # for ac in range(int(num_questions)):
# while a != b:
     
#     print(f"Question: {html.unescape(repo_dict['question'])}")
#     choices = html.unescape(repo_dict['incorrect_answers'])
#     choices.append(html.unescape(repo_dict['correct_answer']))
#     dict_choices = {"1": choices[0], "2": choices[1], 
#                 "3": choices[2], "4": choices[3]}
#     values = list(dict_choices.values())

#     for count, value in enumerate(values,start=1): 
#         print(count, value)

#     your_choice = input()

#     def get_key(val):
#         for key, value in dict_choices.items():
#             if val == value:
#                 return key

#         return "key doesn't exist"

#     if str(your_choice) == str(get_key(choices[3])):
#         print("That is correct")
#     else:
#         print(f"That is incorrect. The correct answer is : {choices[3]}")
    
#     a = a-1
    
    
