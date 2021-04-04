#desafio 003 da 06 aula


d = input('Digite algo ')

if d.isnumeric():
    print(('{} é um inteiro').format(d))

elif d.isalpha():
    print(('{} é um texto').format(d))
    if d.upper():
        print(('{} está em minusculo').format(d))
    elif d.lower():
        print(('{} está em mauisculo').format(d))

else:
    print('nada')

#250320210459