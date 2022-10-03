

number = str(input("Enter a number: "))
num= int(number)


while (num >0):
    
    if num%3 == 0 and num%5 ==0:
        print(str(num)+ ' Fizz Buzz')
    
    elif num%5 ==0: 
       print(str(num)+ ' Buzz')

    elif num% 3 == 0:
         print(str(num)+ ' Fizz')
        
    else: 
        print(str(num)) 
    num -=1
print("Done!")