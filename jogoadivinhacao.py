print('**********************************')
print('Bem vindo. ai JOGO DE ADIVINHAÇÃ0')
print('**********************************')

#Definindo o número secreto
numeroSecreto = 18

#Definindo o número de tentativas
numeroTentativas = 3

while(numeroTentativas > 0):
    
#Recebendo o chute do jogador
    chuteString = input('Digite um número: ')
    print('Você digitou o número: ',chuteString)
    chute = int(chuteString)

#Declarando as condições 
    if numeroSecreto == chute:
        print('Você acertou!!!!')
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um nùmero menor')
    else:
        print('Você errou!!! O número secreto é um número maior')

        numeroTentativas = numeroTentativas - 1

    #Aula Elif 26.02.24