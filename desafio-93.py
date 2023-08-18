
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
