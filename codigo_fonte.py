"""SIGIC - Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia Aurora Siger"""

# Lista de módulos da colônia
modulos = [
    'Habitação',
    'Centro de Controle',
    'Armazenamento de Energia',
    'Agricultura',
    'Laboratório Científico',
    'Comunicação',
    'Suporte Médico',
    'Produção de Oxigênio'
]

# Dicionário com dados de cada módulo: consumo, prioridade, armazenamento,
# necessidade de comunicação e status operacional.
modulo_info = {
    'Habitação': {
        'consumo': 18.0,
        'prioridade': 9,
        'capacidade': 22,
        'comunicacao': 'Alta',
        'status': 'Ativo'
    },
    'Centro de Controle': {
        'consumo': 15.5,
        'prioridade': 10,
        'capacidade': 18,
        'comunicacao': 'Muito alta',
        'status': 'Ativo'
    },
    'Armazenamento de Energia': {
        'consumo': 12.0,
        'prioridade': 8,
        'capacidade': 40,
        'comunicacao': 'Média',
        'status': 'Ativo'
    },
    'Agricultura': {
        'consumo': 17.0,
        'prioridade': 7,
        'capacidade': 28,
        'comunicacao': 'Média',
        'status': 'Ativo'
    },
    'Laboratório Científico': {
        'consumo': 13.5,
        'prioridade': 6,
        'capacidade': 20,
        'comunicacao': 'Alta',
        'status': 'Ativo'
    },
    'Comunicação': {
        'consumo': 10.0,
        'prioridade': 8,
        'capacidade': 15,
        'comunicacao': 'Muito alta',
        'status': 'Ativo'
    },
    'Suporte Médico': {
        'consumo': 14.0,
        'prioridade': 9,
        'capacidade': 18,
        'comunicacao': 'Alta',
        'status': 'Ativo'
    },
    'Produção de Oxigênio': {
        'consumo': 20.0,
        'prioridade': 10,
        'capacidade': 30,
        'comunicacao': 'Alta',
        'status': 'Ativo'
    }
}

# Conexões fixas representadas por tuplas: (origem, destino, peso)
fixed_connections = (
    ('Habitação', 'Centro de Controle', 6.0),
    ('Habitação', 'Armazenamento de Energia', 8.0),
    ('Centro de Controle', 'Armazenamento de Energia', 4.0),
    ('Centro de Controle', 'Comunicação', 3.0),
    ('Armazenamento de Energia', 'Agricultura', 7.0),
    ('Armazenamento de Energia', 'Produção de Oxigênio', 5.0),
    ('Agricultura', 'Laboratório Científico', 5.5),
    ('Comunicação', 'Laboratório Científico', 6.0),
    ('Comunicação', 'Suporte Médico', 4.5),
    ('Suporte Médico', 'Produção de Oxigênio', 6.5)
)

# Lista de conexões para fácil navegação e exibição.
conexoes = list(fixed_connections)

# Mapa de índice para a matriz de adjacência.
indice_modulo = {nome: idx for idx, nome in enumerate(modulos)}

# Matriz de adjacência com zeros quando não há conexão direta.
matriz_adjacencia = [[0 for _ in modulos] for _ in modulos]
for origem, destino, peso in conexoes:
    i = indice_modulo[origem]
    j = indice_modulo[destino]
    matriz_adjacencia[i][j] = peso
    matriz_adjacencia[j][i] = peso

# Lista de adjacência para representações de grafo e algoritmos.
adjacencia = {nome: [] for nome in modulos}
for origem, destino, peso in conexoes:
    adjacencia[origem].append((destino, peso))
    adjacencia[destino].append((origem, peso))


def mostrar_modulos():
    print('\nMódulos da Aurora Siger:')
    for nome in modulos:
        info = modulo_info[nome]
        print(f"- {nome}: consumo={info['consumo']} kW, prioridade={info['prioridade']},"
              f" capacidade={info['capacidade']}u, comunicação={info['comunicacao']}, status={info['status']}")


def mostrar_conexoes():
    print('\nConexões da rede (peso = distância / custo energético):')
    for origem, destino, peso in conexoes:
        print(f"- {origem} <-> {destino}: peso {peso}")


def mostrar_matriz():
    print('\nMatriz de adjacência (0 = sem conexão direta):')
    cabecalho = ' ' * 18 + ' '.join(f"{nome[:5]:>5}" for nome in modulos)
    print(cabecalho)
    for i, linha in enumerate(matriz_adjacencia):
        nome = f"{modulos[i]:<17}"
        valores = ' '.join(f"{valor:5.1f}" for valor in linha)
        print(nome + valores)


def bfs(inicio):
    visitado = []
    fila = [inicio]
    while fila:
        atual = fila.pop(0)
        if atual not in visitado:
            visitado.append(atual)
            vizinhos = [viz for viz, _ in adjacencia[atual] if modulo_info[viz]['status'] == 'Ativo']
            for viz in vizinhos:
                if viz not in visitado and viz not in fila:
                    fila.append(viz)
    return visitado


def dfs(inicio):
    visitado = []
    pilha = [inicio]
    while pilha:
        atual = pilha.pop()
        if atual not in visitado:
            visitado.append(atual)
            vizinhos = [viz for viz, _ in adjacencia[atual] if modulo_info[viz]['status'] == 'Ativo']
            for viz in sorted(vizinhos, reverse=True):
                if viz not in visitado:
                    pilha.append(viz)
    return visitado


def dijkstra(inicio, destino):
    distancias = {nome: float('inf') for nome in modulos}
    anterior = {nome: None for nome in modulos}
    distancias[inicio] = 0
    nao_visitado = set(modulos)

    while nao_visitado:
        atual = min(nao_visitado, key=lambda nodo: distancias[nodo])
        nao_visitado.remove(atual)

        if distancias[atual] == float('inf'):
            break
        if atual == destino:
            break

        for vizinho, peso in adjacencia[atual]:
            if modulo_info[vizinho]['status'] != 'Ativo':
                continue
            if vizinho in nao_visitado:
                nova_dist = distancias[atual] + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    anterior[vizinho] = atual

    caminho = []
    atual = destino
    while atual:
        caminho.insert(0, atual)
        atual = anterior[atual]

    return caminho, distancias[destino]


def calcular_perda_energetica(distancia, consumo_destino, taxa_perda=0.02):
    # perda = distancia * consumo_destino * taxa_perda
    # distancia: distância física entre módulos (ou peso da conexão)
    # consumo_destino: consumo energético do módulo de destino em kW
    # taxa_perda: percentual de perda de energia por unidade de distância
    return distancia * consumo_destino * taxa_perda


def calcular_perda_rota(caminho):
    total = 0.0
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        peso = next(peso for viz, peso in adjacencia[origem] if viz == destino)
        total += calcular_perda_energetica(peso, modulo_info[destino]['consumo'])
    return total


def consultar_modulo(nome):
    if nome not in modulo_info:
        print(f"Módulo '{nome}' não encontrado.")
        return
    info = modulo_info[nome]
    print(f"\nDados do módulo: {nome}")
    for chave, valor in info.items():
        print(f"- {chave.capitalize()}: {valor}")


def simular_falha(nome):
    if nome not in modulo_info:
        print(f"Módulo '{nome}' não encontrado.")
        return
    if modulo_info[nome]['status'] != 'Ativo':
        print(f"O módulo {nome} já está com status '{modulo_info[nome]['status']}'.")
        return
    modulo_info[nome]['status'] = 'Falha'
    print(f"\nFalha simulada no módulo {nome}. Status atualizado para 'Falha'.")
    origem = 'Armazenamento de Energia'
    if modulo_info[origem]['status'] != 'Ativo':
        print('O módulo de armazenamento de energia não está ativo para análise de conectividade.')
        return

    caminho, distancia = dijkstra(origem, nome)
    if distancia == float('inf'):
        print(f"O módulo {nome} ficou isolado da fonte de energia.")
    else:
        print(f"Mesmo com falha, há um caminho possível até {nome}: {' -> '.join(caminho)}")

    conexoes_criticas = identificar_criticas()
    if conexoes_criticas:
        print('\nConexões críticas identificadas:')
        for item in conexoes_criticas:
            print(f"- {item}")
    else:
        print('\nNão foram encontradas conexões críticas diretas no momento.')


def identificar_criticas():
    criticas = []
    for nome in modulos:
        if modulo_info[nome]['prioridade'] >= 9:
            grau = len([viz for viz, _ in adjacencia[nome] if modulo_info[viz]['status'] == 'Ativo'])
            if grau <= 1:
                criticas.append(f"Módulo crítico sem redundância: {nome}")
    for origem, destino, peso in conexoes:
        if modulo_info[origem]['prioridade'] >= 9 and modulo_info[destino]['prioridade'] >= 8:
            criticas.append(f"Aresta crítica: {origem} <-> {destino} (peso {peso})")
    return criticas


def analisar_eficiencia():
    print('\nAnálise de eficiência energética e governança ESG:')
    consumo_total = sum(info['consumo'] for info in modulo_info.values())
    consumo_medio = consumo_total / len(modulos)
    print(f"- Consumo total estimado: {consumo_total:.1f} kW")
    print(f"- Consumo médio por módulo: {consumo_medio:.1f} kW")

    recomendacoes = [
        'Priorizar suporte de vida, oxigênio e centro de controle em situações de emergência.',
        'Reduzir desperdício desligando temporariamente módulos em manutenção.',
        'Evitar rotas longas quando houver caminho mais eficiente.',
        'Manter redundância para módulos críticos e pontos de energia.',
        'Planejar expansão com base na capacidade de armazenamento existente.'
    ]
    print('\nRecomendações de sustentabilidade e governança:')
    for rec in recomendacoes:
        print(f"- {rec}")

    print('\nPerdas energéticas estimadas nas conexões:')
    for origem, destino, peso in conexoes:
        perda = calcular_perda_energetica(peso, modulo_info[destino]['consumo'])
        print(f"- {origem} -> {destino}: perda ≈ {perda:.2f} kW")

    criticas = identificar_criticas()
    if criticas:
        print('\nMódulos/conexões críticos detectados:')
        for item in criticas:
            print(f"- {item}")
    else:
        print('\nA rede atual apresenta redundância satisfatória para os módulos listados.')


def escolher_modulo(mensagem):
    print(mensagem)
    for idx, nome in enumerate(modulos, start=1):
        print(f"{idx} - {nome}")
    try:
        escolha = int(input('Digite o número do módulo: ').strip())
        if 1 <= escolha <= len(modulos):
            return modulos[escolha - 1]
    except ValueError:
        pass
    print('Entrada inválida.')
    return None


def menu():
    while True:
        print('\n=== Sistema SIGIC - Aurora Siger ===')
        print('1 - Visualizar módulos da colônia')
        print('2 - Visualizar conexões da rede')
        print('3 - Mostrar matriz de adjacência')
        print('4 - Executar BFS')
        print('5 - Executar DFS')
        print('6 - Calcular caminho mínimo com Dijkstra')
        print('7 - Consultar módulo específico')
        print('8 - Simular falha operacional')
        print('9 - Analisar eficiência energética e ESG')
        print('0 - Sair')
        escolha = input('Escolha uma opção: ').strip()

        if escolha == '1':
            mostrar_modulos()
        elif escolha == '2':
            mostrar_conexoes()
        elif escolha == '3':
            mostrar_matriz()
        elif escolha == '4':
            inicio = escolher_modulo('Escolha o módulo de início para BFS:')
            if inicio:
                ordem = bfs(inicio)
                print(f"Ordem de visita em BFS: {' -> '.join(ordem)}")
        elif escolha == '5':
            inicio = escolher_modulo('Escolha o módulo de início para DFS:')
            if inicio:
                ordem = dfs(inicio)
                print(f"Ordem de visita em DFS: {' -> '.join(ordem)}")
        elif escolha == '6':
            inicio = escolher_modulo('Escolha o módulo de origem para Dijkstra:')
            destino = escolher_modulo('Escolha o módulo de destino para Dijkstra:')
            if inicio and destino:
                caminho, distancia = dijkstra(inicio, destino)
                if distancia == float('inf'):
                    print('Não há caminho disponível entre os módulos selecionados.')
                else:
                    print(f"Caminho mínimo: {' -> '.join(caminho)}")
                    print(f"Custo total estimado: {distancia:.1f}")
                    perda_total = calcular_perda_rota(caminho)
                    print(f"Perda energética estimada no caminho: {perda_total:.2f} kW")
        elif escolha == '7':
            nome = input('Digite o nome exato do módulo: ').strip()
            consultar_modulo(nome)
        elif escolha == '8':
            nome = input('Digite o nome exato do módulo em falha: ').strip()
            simular_falha(nome)
        elif escolha == '9':
            analisar_eficiencia()
        elif escolha == '0':
            print('Saindo do sistema. Até breve!')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    print('Bem-vindo ao SIGIC - Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia Aurora Siger')
    menu()
