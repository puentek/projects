

number = str(input("Enter a number: "))
num= int(number)
nm = num+1
start = 0
while (start <= num):
    
    if start%3 == 0 and start%5 ==0:
        # print(start)
        print(str(start)+ ' Fizz Buzz')
    
    elif start%5 ==0: 
       print(str(start)+ ' Buzz')

    elif start% 3 == 0:
         print(str(start)+ ' Fizz')
        
    else: 
        print(str(start))
    start += 1 
    # num +=1
print("Done!")

