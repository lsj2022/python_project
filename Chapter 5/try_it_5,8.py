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


#5-10. Checking Usernames: Do the following to create a program that simulates
#how websites ensure that everyone has a unique username.
#Make a list of five or more usernames called current_users

current_users =['james','ron','tom','linda','karen']
new_users =['mary','jenny','Linda', 'joe', 'karen']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.lower(),"use a different name")
    else:
        print(new_user.lower(),'username available')


#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
#as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

numbers= ['1','2','3','4','5','6', '7','8','9']
for number in numbers:
    if "1" in number:
        print(number+ "st")
    elif "2" in number:
        print( number + "nd")
    elif "3" in number:
        print(number + "rd")
    else:
        print(number + "th")



