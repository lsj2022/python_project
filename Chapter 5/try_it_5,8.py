# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:

usernames = []
if usernames:
    for username in usernames:
        if "admin" in username:
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello",username,"thank you for logging in again")
else:
    print("we need more users!")