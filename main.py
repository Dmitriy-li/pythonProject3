first = int(input('Enter number: '))
second = int(input('Enter number: '))
third = int(input('Enter number: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)