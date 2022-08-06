# the if- elif- else chain

age = 12
if age <4:
    print('your admission cost is $0')
    price= 0
elif age < 18:
    print("Your admission cost is $25")
    price = 25
else:
    print("your admission cost is $40")
    price = 40

# using multiple elif blocks:
age = 66
if age <4:
    print('your admission cost is $0')
    price= 0
elif age < 18:
    print("Your admission cost is $25")
    price = 25
elif age < 65:
    price =40
else:
    price = 20
print(f'Your admission cost is ${price}.')



