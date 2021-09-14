import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

qntPw = int(input('Укажите количество паролей для генерации:'))
lenPw = int(input('Укажите длину одного пароля:'))
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if digOn.lower() == 'y':
    chars += digits
if ABCon.lower() == 'y':
    chars += uppercase_letters
if abcOn.lower() == 'y':
    chars += lowercase_letters
if chOn.lower() == 'y':
    chars += punctuation
if excOn.lower()  == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generated_password(lenPw, chars):
    password = ''
    for j in range(lenPw):
        password += random.choice(chars)
    return password

for _ in range(qntPw):
    print(generated_password(lenPw, chars))
