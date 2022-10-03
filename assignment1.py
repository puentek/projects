# import platform

# print( platform.python_version() )

# class Save:
#     def _init_(self):
#         self.goal = input('Welcome to the savings calculator, what is your savings goal?:')
#         self.save_already = input('enter what you have save_already: ')
#         self.save_week = input('enter how much you save every week: ')
#     def calc(self):
#         # x = (self.goal -self.save_already)/52
        
#         print(self.goal)
#         print(self.save_already)
#         print(self.save_week)
#         # print(x)



# save = Save()
# save.calc()
# print(f"I have calculated that it will take {x} weeks to hit your savings goal.")





# print(f"Welcome to the savings calculator, what is your savings goal?: {save_goal}")
# print(f"How much do you have saved already?: {save_already}")
# print(f"How much are you saving every week?: {save_week}")
# print(f"I have calculated that it will take {x} weeks to hit your savings goal.")


print('Welcome to the savings calculator, what is your savings goal?: ')
save_goal = str(input())
print(f"How much do you have saved already?:")
save_already = str(input())
print("How much are you saving every week?: ")
save_week = str(input())
x = round((float(save_goal)-float(save_already))/float(save_week))
print(f"I have calculated that it will take {x} weeks to hit your savings goal.")