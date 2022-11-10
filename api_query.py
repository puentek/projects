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
# print(url_trivia_link)
# str(input())
headers = {'Accept': 'application/vnd.opentdb.v3+json'}
r =  requests.get(url_trivia_link,headers=headers)
# Here lets check if this works 
# print(f'Status code: {r.status_code}')
response_dict = r.json()

# Process results 
print(response_dict.keys())

# print(f"Response Code: {response_dict['response_code']}")
# print(f"Results Info : {response_dict['results']}")

repo_dicts = response_dict['results']
# print(f"Results returned: {len(repo_dicts)}")

repo_dict = repo_dicts[1]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\n Selected information about the questions")
print(f"Question: {html.unescape(repo_dict['question'])}")
# print(f"Pick from the choices: {repo_dict['incorrect_answers']} {repo_dict['correct_answer']} ")
# print(repo_dict['incorrect_answers'], repo_dict['correct_answer'])



choices = html.unescape(repo_dict['incorrect_answers'])
choices.append(html.unescape(repo_dict['correct_answer']))
# # wrong = repo_dict['incorrect_answers']
# # print(choices)
# random.shuffle(choices)
# for count, wr in enumerate(choices,start=1): 
#     print(count, wr)


dict_choices = {"1": choices[0], "2": choices[1], 
                "3": choices[2], "4": choices[3]}
values = list(dict_choices.values())
random.shuffle(values)
# for value in values:
#     print(value)
for count, value in enumerate(values,start=1): 
    print(count, value)

# your_choice = input()

# if your_choice != repo_dict['correct_answer']:


# right = repo_dict['correct_answer']
# for count, rt in enumerate(right,start=1): 
#     print()

# html.unescape
