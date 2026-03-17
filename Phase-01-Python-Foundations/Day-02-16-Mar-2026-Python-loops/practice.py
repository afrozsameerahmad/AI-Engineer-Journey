#  1- Find the sum of a 3 digit number entered by the user

#taking input from the user
num1 = int(input("Enter a number: "))
#when we divide a number by 10, the remainder is the last digit of the number. 345 % 10 = 5
a = num1%10
#when we divide a number by 10, the quotient is the number without the last digit. 345 // 10 = 34
num1 = num1//10

#when we divide a number by 10, the remainder is the last digit of the number. 34 % 10 = 4
b = num1%10
#when we divide a number by 10, the quotient is the number without the last digit. 34 // 10 = 3
num1 = num1//10

#when we divide a number by 10, the remainder is the last digit of the number. 3 % 10 = 3
c = num1%10
#sum of the digits
sum = a + b + c
print("The sum of the digits is: ", sum)




# 2- minimum of three numbers entered by the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1<num2 and num1<num3:
    print("The minimum number is: ", num1)
elif num2<num3:
    print("The minimum number is: ", num2)
else:
    print("The minimum number is: ", num3)



# 3- simple calculator using if-else

fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /,%, //): ")

if operator=="+":
    print("The sum is: ", fnum+snum)
elif operator=="-":
    print("The difference is: ", fnum-snum)
elif operator=="*":
    print("The product is: ", fnum*snum)
elif operator=="/":
    if snum!=0:
        print("The quotient is: ", fnum/snum)
    else:
        print("Error: Division by zero not allowed.")
elif operator=="%":
    if snum!=0:
        print("The modulus is: ", fnum%snum)
    else:
        print("Error: Division by zero not allowed.")
elif operator=="//":
    if snum!=0:
        print("The floor division is: ", fnum//snum)
    else:
        print("Error: Division by zero not allowed.")
else:
    print("Invalid operator entered.")
    

menu = input('''
Hi how i can help you
1.Enter 1 for pin change
2.Enter 2 for balance check
3.Enter 3 for money transfer
4.Enter 4 for exit
    ''')

if menu=="1":
    print("You have selected pin change")
elif menu=="2":
    print("You have selected balance check")
elif menu=="3":
    print("You have selected money transfer")
    
elif menu=="4":
    print("You have selected exit")
    
else:
    print("Invalid option selected")
    
    
    
    
    
'''
4- WHILE LOOP TO PRINT TABLE OF A NUMBER ENTERED BY THE USER

'''
num= int(input("Enter a number: "))
i=1
while i<=10:
    print(num, "x", i, "=", num*i)
    i+=1
    
    
    
'''
Sequence sum 1/1!+1/2!+1/3!+...+1/n!

'''
num = int(input("Enter a number: "))
factorial = 1
result = 0
for i in range(1,num+1):
    factorial = factorial * i
    result = result + 1/factorial
print("The result is: ", result)