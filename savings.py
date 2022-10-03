

print('Welcome to the savings calculator, what is your savings goal?: ')
save_goal = str(input())
print(f"How much do you have saved already?:")
save_already = str(input())
print("How much are you saving every week?: ")
save_week = str(input())
x = round((float(save_goal)-float(save_already))/float(save_week))
print(f"I have calculated that it will take {x} weeks to hit your savings goal.")