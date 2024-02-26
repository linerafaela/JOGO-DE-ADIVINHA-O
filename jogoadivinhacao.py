print('**********************************')
print('Bem vindo. ai JOGO DE ADIVINHAÇÃ0')
print('**********************************')

numeroSecreto = 18

chuteString = input('Digite um número: ')

print('Você digitou o número: ',chuteString)

chute = int(chuteString)

if numeroSecreto == chute:
    print('Você acertou!!!!')
elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um nùmero menor')
else:
    print('Você errou!!! O número secreto é um número maior')

    #Aula Elif 26.02.24