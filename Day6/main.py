print("SECURE LOGIN")
print()
# getting user input
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "Jane" and password == "abcd":
    #do somthing
    print("Hello, Jane. The weather is great outside, enjoy your day!")
elif username == "Raha" and password == "efgh":
    # do something 
    print("Welcome Raha,remember to smile!")
elif username == "Kate" and password == "ijklm":
   # do something
    print("Welcome back Kate!")
else:
    # do something
    print("INVALID LOGIN!")