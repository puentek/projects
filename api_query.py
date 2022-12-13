
import requests
import json 
import html 
import random 


dict = { 9: "General Knowledge", 28: "Vehicles", 30: "Science: Gadgets" }
print("Welcome to Trivia Bot 5000, Please Select a Category of Trivia: \n 1. General Knowledge \n 2. Vehicles \n 3. Science: Gadgets  ")
category_selected = input()
if int(category_selected) == 1:
    converted_selection = 9
elif int(category_selected) == 2:
    converted_selection = 28
else:
    converted_selection = 30

print(f'You picked {dict[int(converted_selection)]}, how many questions do you want?')
num_questions = input()
url_trivia= (f'https://opentdb.com/api.php?amount={str(num_questions)}&category={str(converted_selection)}&difficulty=easy&type=multiple')
url_trivia_link = url_trivia
headers = {'Accept': 'application/vnd.opentdb.v3+json'}
r =  requests.get(url_trivia_link,headers=headers)
response_dict = r.json()
repo_dicts = response_dict['results']
repo_dict = repo_dicts[1]
correct_count = 0

for repo_dict in repo_dicts:
    print(f"Question: {html.unescape(repo_dict['question'])}")

    choices = html.unescape(repo_dict['incorrect_answers'])
    
    correct_ans = html.unescape(repo_dict['correct_answer'])
    choices.append(correct_ans)

    dict_choices = {"1": choices[0], "2": choices[1], 
                "3": choices[2], "4": choices[3]}
    values = list(dict_choices.values())
    
    random.shuffle(values)
    for count, value in enumerate(values,start=1): 
        print(count, value)

    your_choice = input()

    def get_key(val):
        for key, value in dict_choices.items():
            if val == value:
                return key

        return "key doesn't exist"
    
    # correct_count = 0

    if values[int(your_choice)-1] == correct_ans:
        print("That is correct")
        correct_count = correct_count + 1
        # print(f"correct_count: {correct_count}")

    else:
        print(f"That is incorrect. The correct answer is : {choices[3]}")
    
print(f"Your game is over, you got {str(correct_count)} out of {str(num_questions)} correct")
print("Thanks for playing!!")





