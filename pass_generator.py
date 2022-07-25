import random
symbols = ('abcdfghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"№;%:?=-/')

def password(length):
    password = ''
    for i in range(length):
        password += random.choice(symbols)
    print(password)

length = int(input('Count of the symbols: '))

password(length)
