print('**********************************')
print('Bem vindo. ai JOGO DE ADIVINHAÇÃ0')
print('**********************************')

numeroSecreto = 18

chuteString = input('Digite um número: ')

print('Você digitou o número: ',chuteString)

chute = int (chuteString)

if numeroSecreto == chute:
    print('Você acertou!!!!')

else:
    print('Você errou!!!')