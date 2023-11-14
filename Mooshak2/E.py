direita = True
pontuacao = 0
Saltos, NrLajes = map(int,input().split())
pos = 0
jogo = []

for i in range(NrLajes):
    jogo.append(int(input()))
    pos += 1          # cria uma lista com Saltos de tamanho
    if pos == Saltos: # que tem os valores de jogo[0,Saltos]
        if direita:   
            pontuacao += max(jogo)
            pos -= jogo.index(max(jogo)) + 1 # muda a pos para o valor maximo (e ajusta)
            del jogo[0:jogo.index(max(jogo)) + 1] # apaga tudo até a essa laje
            direita = False
        else:
            pontuacao -= min(jogo)
            pos -= jogo.index(min(jogo)) + 1
            del jogo[0:jogo.index(min(jogo)) + 1]
            direita = True
if pos > 0:
    if direita:
        pontuacao+= max(jogo)
print(pontuacao)