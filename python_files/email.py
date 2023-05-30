from tokenize import String

email = input("enter your email")
username = email.split("@")[0]
print(f"your username is {username}")