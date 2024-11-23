def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

n = int(input('Enter an integer between 3 and 20: '))

result = get_password(n)
print('Password:', result)