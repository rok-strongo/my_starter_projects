def caesar(choice, alpha, shift, word):

    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if alpha == '1':
        m_alfa = 26
        low_alfabet = eng_lower_alphabet
        upp_alfabet = eng_upper_alphabet
    elif alpha == '2':
        m_alfa = 32
        low_alfabet = rus_lower_alphabet
        upp_alfabet = rus_upper_alphabet
    s_new = ''
    for i in range(len(word)):
        if word[i].isalpha():
            if word[i] == word[i].lower():
                num = low_alfabet.index(word[i])
            if word[i] == word[i].upper():
                num = upp_alfabet.index(word[i])
            if choice == '1':
                index = (num + shift) % m_alfa
            elif choice == '2':
                index = (num - shift) % m_alfa

            if word[i] == word[i].lower():
                s_new += low_alfabet[index]
            if word[i] == word[i].upper():
                s_new += upp_alfabet[index]
        else:
            s_new += word[i]
    return s_new


n = input('Введите направление шифрование - 1, дешифрование - 2: ')
while n not in ('1', '2'):
    print('Не верно, повторите ввод.')
    n = input('Введите направление шифрование - 1, дешифрование - 2: ')
language = input('Введите язык алфавита английский - 1, русский - 2: ')
while language not in ('1', '2'):
    print('Не верно, повторите ввод.')
    language = input('Введите язык алфавита английский - 1, русский - 2: ')
step = input('Введите шаг сдвига: ')
while not step.isdigit():
    print('Шаг сдвига должен быть числом. Повторите ввод ')
    step = input('Введите шаг сдвига: ')
step = int(step)
text = input('Введите фразу... ')

print(caesar(n, language, step, text))

