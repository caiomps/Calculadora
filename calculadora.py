print('Somos uma calculadora virtual')
print('Primeiro digite os dois numeros e depois escolha uma opcao')
print('''[ 1 ] Soma
[ 2 ] Subtracao
[ 3 ] Divisao
[ 4 ] Multiplicacao
[ 5 ] Tabuada Do Numero
[ 6 ] Sair''')

op = 0
while op != 6:
    op = int(input('Digite uma opcao: '))
    num1 = int(input('Digite o Primeiro numero: '))
    num2 = int(input('Digite o Segundo numero: '))
    soma = num1 + num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    subtracao = num1 - num2

    if op == 1:
        print('A soma de {} + {} = {}'.format(num1, num2, soma))

    elif op == 2:
        print('A Subtracao de {} - {} = {}'.format(num1, num2, subtracao))

    elif op == 3:
        print('A Divisao de {} / {} = {}'.format(num1, num2, divisao))

    elif op == 4:
        print('A Multiplicacao de {} * {} = {}'.format(num1, num2, multiplicacao))

    elif op == 5:
        num = float(input('Digite o primeiro numero: '))
        for nu in range(1, 11):
            tabuada = num * nu
            print('{} x {} = {}'.format(num1, nu, tabuada))
    else:
        print('ESCOLHA UMA OPCAO DE 1 A 7!!!')

print('FIM!!! Obrigado, VOLTE SEMPRE!!! ')