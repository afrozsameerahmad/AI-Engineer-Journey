'''

Extract username and domain from an email address.

'''


email = input("Enter your email: ")
pos = email.find("@")
print("Username:", email[:pos])
print("Domain:", email[pos+1:])