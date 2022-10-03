
# Code created by Karina Puente 10/03/22
'''1. Prompt the user to enter a numerical limit. (Recall the input function from chapter 1)
   2. For the numbers 1 up to the number the user entered, the following should happen.
        1. Always print out the current number
        2.If the number is divisible by 3 also print "Fizz"
        3. If the number is divisible by 5 also print "Buzz"
        4.If the number is divisible by 3 and 5 also print "Fizz Buzz"
   3.Once you have finished all the numbers output "Done!"

    **You will write two different versions of this assignment, one accomplishes the task using a "while" loop, the other uses a "for" loop. '''

number = str(input("Enter a number: "))
N= int(number)
for num in range(1,N+1):
    if num%3 == 0 and num%5 ==0:
        print(str(num)+ ' Fizz Buzz')

    elif num%5 ==0: 
       print(str(num)+ ' Buzz')

    elif num% 3 == 0:
         print(str(num)+ ' Fizz')
        
    else: 
        print(str(num))
print("Done!")