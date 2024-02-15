print('**********************************')
print('Bem vindo. ai JOGO DE ADIVINHAÇÃ0')
print('**********************************')

numeroSecreto = 18

chute = input('Digite um número')

print('Você digitou o número',chute)

if numeroSecreto == chute:
    print('Você acertou!!!!')

else:
    print('Você errou!!!')