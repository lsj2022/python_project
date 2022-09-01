#how the input() function works:

message = input("Tell me something, and I will repeat it back to you:")
print(message)

# writing clear prompts:

name= input("please enter your name:")
print(f"\nHello, {name}!")

prompt = "if you tell us who you are, we can personalize the message you see."
prompt += '\nWhat is your first name?'

name = input(prompt)
print(f"\nHello, {name}!")














