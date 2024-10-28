# Trabalho 1 - Estatísitca e Probabildiade
# Alunos: Hálison  
# Lista 1

# Questão 1 a)

import random

def GiraDados():
    ''' Função auxiliar que simula o lançamento de dois dado.
      --> int, int '''
    x = (random.randint(1,6))
    y = (random.randint(1,6))

    return x, y

def Craps():
    ''' Essa é a função principal do jogo, que lida com as situações de lançar 2 dados, processar a soma desses dados,
    verificar as condições de vitória e derrota.
    Além de, informar caso o jogador vença ou perca.
      --> list '''

    #primeira rodada:
    dado1, dado2 = GiraDados()
    soma = dado1 + dado2
    primeiro_resultado = soma

    saida = [soma]

    if soma in (2, 3, 12):
        return saida, ('Perdeu na primeira rodada')
    
    elif soma in (7, 11):
        return saida, ('Venceu na primeira rodada')


    while True:

        dado1, dado2 = GiraDados()
        soma = dado1 + dado2
        saida.append(soma)

        if soma == 7:
            return saida, ('Derrota')

        elif soma == primeiro_resultado:
            return saida, ('Vitória')

# Questão 1 b)

##>>> Craps()
##[9, 9, 'Vitória']
##>>> Craps()
##[11, 'Venceu na primeira rodada']
##>>> Craps()
##[8, 5, 6, 11, 6, 6, 10, 4, 6, 8, 'Vitória']
##>>> Craps()
##[10, 8, 7, 'Derrota']
##>>> Craps()
##[6, 8, 5, 5, 6, 'Vitória']


# Questão 1 c)

def simula_craps(x):
    ''' Essa é a função que simula x vezes o jogo de Craps e retorna o número de vitórias
    e de derrotas.
    int --> list '''

    vitorias = 0
    derrotas = 0

    while x>0:

        dado1, dado2 = GiraDados()
        soma = dado1 + dado2
        primeiro_resultado = soma

        if soma in (2, 3, 12):
            derrotas +=1

        elif soma in (7, 11):
            vitorias +=1

        else:
            
            # Precisa continuar rodando até sair 7 ou repetir a soma inicial
            while True:
                dado1, dado2 = GiraDados()
                soma = dado1 + dado2

                if soma == 7:
                    derrotas +=1
                    break

                elif soma == primeiro_resultado:
                    vitorias +=1
                    break
        x -= 1

    media = vitorias / (vitorias + derrotas)

    print( 'num. de vitórias = ', vitorias, 'num. de derrotas = ', derrotas)

    print( 'a proporção de vitórias é ', media )

