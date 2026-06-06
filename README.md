# SIGIC - Simulação de rede da colônia Aurora Siger

**Desenvolvido por:** Pedro Henrique Canavezi — RM 570298

## Objetivo

Simular a rede de módulos de uma colônia fictícia. O projeto representa os módulos como um grafo, permite testar buscas, calcular caminhos de menor custo, estimar perdas energéticas e analisar o impacto de falhas.

## Como executar

Requisitos:
- Python 3.6 ou superior
- Nenhuma biblioteca externa

Passos:
1. Abra um terminal
2. Entre na pasta do projeto:
   `cd c:\Users\pedro\Documents\GitHub\sistema-sigic-aurora-siger`
3. Execute:
   `python codigo_fonte.py`

## Estrutura de arquivos

- `codigo_fonte.py` — código principal
- `README.md` — documentação do projeto
- `link_video.txt` — local para link do vídeo
- `rede_colonia.pdf` — diagrama da rede
- `documentacao_complementar.pdf` — documentação técnica adicional
- `arquivos_auxiliares/dados_modulos.txt` — tabela de atributos dos módulos
- `arquivos_auxiliares/descricao_rede.txt` — descrição das conexões e topologia

## Módulos da colônia

| Módulo | Consumo (kW) | Prioridade | Capacidade | Comunicação |
|--------|--------------|-----------|-----------|------------|
| Habitação | 18.0 | 9 | 22u | Alta |
| Centro de Controle | 15.5 | 10 | 18u | Muito Alta |
| Armazenamento de Energia | 12.0 | 8 | 40u | Média |
| Agricultura | 17.0 | 7 | 28u | Média |
| Laboratório Científico | 13.5 | 6 | 20u | Alta |
| Comunicação | 10.0 | 8 | 15u | Muito Alta |
| Suporte Médico | 14.0 | 9 | 18u | Alta |
| Produção de Oxigênio | 20.0 | 10 | 30u | Alta |

## Algoritmos usados

- **BFS**: percorre a rede em largura a partir de um módulo inicial
- **DFS**: percorre a rede em profundidade a partir de um módulo inicial
- **Dijkstra**: encontra o caminho de menor custo entre dois módulos

## Estruturas de dados usadas

- **Listas**: nomes de módulos, conexões e filas/pilhas das buscas
- **Dicionários**: atributos de módulos, índice dos módulos e lista de adjacência
- **Tuplas**: conexões fixas com peso
- **Matriz de adjacência**: representação de conexão entre módulos

## Modelagem matemática

A perda energética é estimada por:

`perda = distância × consumo_destino × taxa_perda`

- `distância`: peso da aresta entre módulos
- `consumo_destino`: consumo do módulo de destino em kW
- `taxa_perda`: constante fixa (0.02)

É uma modelagem simples para comparar rotas e mostrar como o peso da conexão afeta as perdas.

## ESG

O programa faz uma análise básica de eficiência e governança:

- calcula consumo total e médio
- mostra perdas estimadas por conexão
- identifica módulos com pouca redundância
- sugere ações simples para manter módulos críticos ativos

## Exemplo curto de uso

1. Inicie o programa com `python codigo_fonte.py`
2. Use a opção **4** para ver a ordem de visita em BFS
3. Use a opção **6** para calcular caminho mínimo entre dois módulos
4. Use a opção **8** para simular falha em um módulo

## Notas

Este projeto é uma simulação acadêmica de rede de módulos. Não controla hardware real e não usa bibliotecas externas.
