# IF-ELSE 

'''
Why we need IF-ELSE 
When we write program from top to bottom 
program have two option either  it exexute line by line but sometimes in program it have two options either execute 1st part either 2nd
thats why we need IF-ELSE

EXAMPLE- Login page when you create login page if credentials is true user can login but when  credentials is not matched show error

in this if condtion is true it ececute the if part and if condition is false the else part execute
'''


'''
Syntax of if-else 

#if condition:
    #code to execute when condition is true
#else:
    #code to execute when condition is false
    
'''


'''
Simple login program using if - else 

'''
email = input("Enter your email : ")
password = input("Enter your password : ")

if email=="sameer@gmail.com" and password=="12345":
    print("Login Successfully ")
    
elif email=="sameer@gmail.com" and password!="12345":
    print("Invalid password ")
    password = input("Enter your password again : ")
    if password=="12345":
        print("Login Successfully ")
    else:
        print("Beta Tumse Na Ho Payega ")   
        
elif email!="sameer@gmail.com" and password=="12345":
    if email=="sameer@gmail.com":
        print("Login Successfully ")
    else:
        print("Beta Tumse Na Ho Payega ")
        
else:
    print("Invalid email or password ")