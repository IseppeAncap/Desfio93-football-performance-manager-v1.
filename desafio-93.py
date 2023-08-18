
# Definição de cores para outupt
reset = '\033[0m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta= '\033[35m'
ciano = '\033[36m'
## 1ª ETAPA - Mensagem de boas-vindas, Título e Explicação.
print(f'{azul}Seja Bem Vindo')
print(f'{magenta}{""::>20}{amarelo}Football Performance Manager{reset}{magenta} {""::>20}{reset}')
print(f'{"":^15}Gerenciador de Desempenho no Futebol')
print(f'---'*24)
print(f'Explicação: Esse pograma coleta alguns dados do jogador e analiza seu desempenho dentro das partidas,',end='')
print(f'apresenta estas estáticas usa dicionário com estutura principal e uma',end=' ') 
print(f'lista para armazenar o números de Gols.')
print()
## 2ª ETAPA - Inicialização do dicionário e coleta de dados.
desempenho = {'nome': 0,'partidas': 0, 'gols': [], 'total': 0}
# Coleta do nome do jogador
desempenho['nome'] = str(input(f'Nome do Jogador: '))
# Coleta do número de partidas jogadas
desempenho ['partidas'] = int(input(f'Quantas partidas {desempenho["nome"]} Jogou ? '))
# Loop para coletar a quantidade de gols feitos em cada partida
for p in  range(desempenho['partidas']):
    desempenho['gols'].append(int(input(f'Quantos Gols ele fez na partida {p+1}ª?: ')))
desempenho['total']= sum(desempenho['gols'])# método para calcular,o total de gols. 
print('-=-'*15)
## 3ª ETAPA - Saída 1ª: Exibição dos dados do jogador.
for k, v in desempenho.items():
    print(f'{".":>20}O Campo {ciano}{k}{reset} têm o valor: {ciano}{v} {reset}.')
print('-=-=-'*15)
print(f'O Jogador {vermelho}{desempenho["nome"]}{reset} jogou {verde}{desempenho["partidas"]} {reset}partidas')
print()
## 4ª ETAPA - Saída 2ª: Exibição das estatísticas sobre gols marcados em cada partida.
for p, v in enumerate (desempenho['gols'],1):
    if v ==0:
        print(f'{"=>":>20} Na partida {amarelo}{p}ª{reset} {desempenho["nome"]} não marcou nenhum! 😞😞')
    else:
        print(f'{"=>":>20} Na partida {amarelo}{p}ª{reset} {desempenho["nome"]} marcou 🥅 {v*" ⚽"} {amarelo}{v}{reset} { "Gol"if v == 1 else "GOLS"}')
print('-=-=-'*15)
print(f'O Jogador {vermelho}{desempenho["nome"]}{reset} marcou um total {verde}{desempenho["total"]}{reset} {"Gols"if desempenho["total"]>1 else "Gol"}!\n🥅 {desempenho["total"]*" ⚽ "}')
print()
print(f'Fim do Programa. Obrigado pro utiliza nosso Serviços!!')


'''
Desafio 93: Gerenciador de Desempenho de Jogador de Futebol

Objetivo:

O objetivo deste desafio é criar um programa que gerencie o desempenho de um jogador de futebol ao longo de um campeonato. 
O programa irá coletar informações sobre o jogador, como nome, número de partidas jogadas e a quantidade 
de gols marcados em cada partida. 
Todas essas informações serão armazenadas de forma organizada em um dicionário, 
que também incluirá o total de gols feitos pelo jogador no campeonato.
Passo a passo - Gerenciador de Desempenho no Futebol
---------------------------------------------------

## 1ª ETAPA - Mensagem de boas-vindas, Título e Explicação.

    .Nesta etapa, é exibida uma mensagem de boas-vindas ao usuário, seguida por um título estilizado e uma explicação breve sobre o programa.
--------------------------------------------------------------------------
## 2ª ETAPA - Inicialização do dicionário e coleta de dados.
    
    .Nesta etapa, o dicionário "desempenho" é inicializado com chaves e valores iniciais definidos como zero e listas vazias.
    .Em seguida, o programa solicita ao usuário o nome do jogador e a quantidade de partidas jogadas.
    .Usando um loop for, o programa itera sobre o número de partidas informado e solicita a quantidade de gols marcados em cada partida.
    .Os valores dos gols são armazenados em uma lista usando o método append na chave ['gols'].
    .O método sum é utilizado para calcular a soma total de gols, que é atribuída à chave ['total'].
-------------------------------------------------------------------------
## 3ª ETAPA - Saída 1ª: Exibição dos dados do jogador.

    .Nesta etapa, o programa utiliza um loop for para iterar sobre o dicionário "desempenho" e exibir cada par de chave e valor de forma organizada.
-----------------------------------------------------------------------------------------------------------------------------
## 4ª ETAPA - Saída 2ª: Exibição das estatísticas sobre gols marcados em cada partida.
    
    ATENÇAO: Aqui iteramos sobre um estrutura de lista []    
    .Nesta etapa, o programa exibe informações detalhadas sobre as partidas e gols marcados pelo jogador.
    .Exibi nome do jogador e o total números partidas.
    .Usando um loop for e a função enumerate, o programa itera sobre a lista de gols, atribuindo uma posição a cada partida.
    .Se a quantidade de gols for zero, o programa exibe uma mensagem indicando que nenhum gol foi marcado.
    .Caso contrário, o programa exibe a quantidade de gols marcados, acompanhada de emojis e tratamento de plural.
    .No final, o programa exibe o total de gols marcados,faz um novo tartamento para o plural usando if 
    dentro do print else utilizando emojis, seguido de uma mensagem de encerramento.
'''