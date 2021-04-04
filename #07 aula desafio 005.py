#desafio 05, 06 , 07 , 08 , 09, 10, 11, 12, 13
#Helder Lopes PYCHARM Python 3

#005 programa que mostra antecessor e sucessor de um numero inteiro
def numero():
    print("DESAFIO #005")
    n=input("Digite um número ")
    n=int(n)
    print("O antessessor é {}, o número é {} e o sucessor é {}".format(n-1,n,n+1 ))

#006 leia um numero e mostro dobro, triplo e raiz quadrada
def dtr():
    print("DESAFIO #006")
    d=input("Digite um numero ")
    d=int(d)
    print("O numero é {}, o dobro é {}, seu triplo é {} e a raiz quadrada é {:.2f}".format(d, d*2, d*3, d**(1/2)))

#007 leia duas notas de um aluno, calcule e mostre a média
def med():
    print("DESAFIO #007")
    n1=input("Digite a primeira nota ")
    n2=input("Digite a 2 nota ")
    print("A media do aluno é {:.2f}".format((float(n1)+float(n2))/2))

#008 ler valor em metros, converter para centimentos e milimetros
def con():
    print("DESAFIO #008")
    m=input("Digite o valor em metros que voce quer converter: ")
    m=int(m)

    print("O valor em metros é {}, em centimetros {} e em milimetros {} ".format(m,m*100,m*1000))

#009 leia numero inteiro e calcule e mostre sua tabuada
def tab():
    print("DESAFIO #009")
    n=input("qual numero voce quer calcular ? ")
    n=int(n)
    t=[1,2,3,4,5,6,7,8,9,10]
    print("-"*15)
    for i in t:
        print(("| {:<2} x {:<2} = {:<3} |").format(n, i, n*i))
    print("-"*15)

#010 leia quanto dinheito a pessoa tem na carteira e quanto dolares ela pode comprar d=3,27
def dol():
    print("DESAFIO #010")
    car=input("Quanto voce tem em sua carteira? R$")
    car=float(car)

    print("Voce tem R${:.2f} na carteira e pode comprar U${:.2f} (Cotação do dolar R$3.27)".format(car, car / 3.27))

#011 leia a altura e largura, calcule a area e a quantidade necessaria pra pintar sabendo que cada litro pinta 2 m²
def are():
    print("DESAFIO #011")
    l=input("Informa a largura da parede em metros ")
    l=float(l)
    a=input("Informe a altura da parede em metros ")
    a=float(a)

    print(("A área total da parede é {:.2f}m². Você vai precisar de {:.2f} litros de tinta.").format(l*a, (l*a)/2))

#012 leia o preço e mostre o preço com 5% de desconto
def pro():
    print("DESAFIO #012")
    pre=input("Informe o preço do produto R$ ")
    pre=float(pre)
    print(("O preço do produto com desconto de 5% fica: R$ {:.2f}").format(pre*(1-0.05)))

#013 leia o salario de um funcionario e mostre ele com 15% de aumento
def sal():
    print("DESAFIO #013")
    s=input("Informe o salario do funcionário R$ ")
    s=float(s)
    print("O salário R$ {} com o acrescimo de 15% fica em R$ {:.2f}".format(s, s*(1+0.15)))

#escolher um programa para funcionar
#menu
po=""

while po != 0:
    prog = [5, 6, 7, 8, 9, 10, 11, 12, 13]
    print("=" * 80)
    for p in prog:
        print("#{}".format(p), end='[ ]  ')
    print(">>[ 0 ]<< para sair")
    print("=" * 80)
    po=input("\nQual desafio voce quer acessar? ")

    po=int(po)

#condicionante para o menu
    # execucao do programa escolhido
    if po==5:
        numero();
    elif po==6:
        dtr()
    elif po==7:
        med()
    elif po==8:
        con()
    elif po==9:
        tab()
    elif po ==10:
        dol()
    elif po==11:
        are()
    elif po==12:
        pro()
    elif po==13:
        sal()
    else:
        print("Escolha uma opçãp")

#202104040427