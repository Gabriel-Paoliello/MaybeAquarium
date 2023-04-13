# ----------- Possível ordem de funcionalidades a serem criadas  ----------- #

# -- TUDO ISSO É UMA SUGESTÃO E PODE SER ALTERADO DE ACORDO COM OS AMIGUINHOS -- #

# -- Início -- #
- Criar classes para classificar espécies e indivíduos
- Criar indivíduos na tela, talvez começar com 10 no mundo
- Criar sentido/radar para cada indivíduo


# -- Movimentações -- #
- Modificar cores de acordo com a velocidade, sentido e idade (fixo até o cálculo da idade)
- Criar movimentação dos indivíduos (diferentes direções, cálculo para sortear aleatoriamente a direção sem ficar muito bagunçado)
- Impedir que o indivíduos saiam da tela (tudo bem o sentido sair, mas o indivíduo deve mudar de direção imediatamente)
- Testar movimentações para não ficar estranho


# -- Tempo no jogo -- #
- Idealizar um "tick time" que defina o tempo de execução do jogo sem a necessidade de depender do fps/processamento da máquina utilizada 


# -- Fome -- #
- Realizar geração de comida aleatória pelo mapa
- Aplicar fome e morte, desaparecer se a fome chegar a 0 (Deixar pronto para deixar uma carcaça, caso apliquem espécies carniceiras no futuro)
- Aplicar movimentação a comida (Se encontrar uma comida no raio, tentar caminhar até essa comida. Se tocar nela, comida desaparece e barra de fome aumenta)
- Balancear e testar o cálculo de comida + indivíduos + velocidade + sentido e garantir que não está deixando todos extintos


# -- Idade e Reprodução -- #
- Aplicar idade e modificar a cor dependendo da idade (Alterar algum dos RGB para isso)
- Aplicar reprodução (Se dois indivíduos que cumpram com os critérios de reprodução [Talvez fome > 5],
- uma marca seria realizada em ambos com o "id" dos dois specimens e as características de cada um seriam salvas,
- Ambos tentam ir para a direção do outro.
- Na movimentação para o outro, se tornam inalvejados para fome, idade e predadores [Para evitar bugs de morte no meio do processo] e geram um novo indivíduo na mesma posição.
- Os 3 indivíduos não conseguirão reproduzir por X tempo
- O specimen criado deverá ter as características aleatórias herdada dos pais (calculo explicado abaixo) )


-  Cálculo de reprodução (Discutir matemática com amiguinhos e ver a opinião de cálculo deles):
    - Supondo que o Familiar1 tenha 4 de velocidade, e o Familiar2 tenha 3 de velocidade,
    - o novo indivíduo deve ter aleatoriamente um valor entre (A+B/2)-1 e (A+B/2)+1, ou seja, entre 2.5 e 4.5


# -- Testes -- #
- Testar e balancear as regras para garantir que não sejam extintos e criar um ecossistema sustentável.


# -- Próximos passos -- #
- Achar uma forma de colocar online e funcional sem necessidade de manutenção. Cogitar possibilidade de adicionar e atualizar sem perder os dados existentes


# -- Próximos Próximos passos -- #
- Cogitar possibilidade de novas espécies serem adicionadas, com novas mecânicas e coisas criativas (Predadores, Indivíduos parados, reprodução por 3 indivíduos, movimentações diferenciadas, etc)
- Cogitar possibilidade de mostrar no site uma tela com os dados de idade, specimen, velocidade, etc em cada 