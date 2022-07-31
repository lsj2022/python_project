#create a list from 1-50; then print only the even numbers; then print out the list in reverse

numbers= list(range(1,51))
print(numbers)
numbers= list(range(2,51,2))
print(numbers)
print(sorted(numbers, reverse=True))