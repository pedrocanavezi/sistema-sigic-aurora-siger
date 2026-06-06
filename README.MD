# SIGIC — Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia Aurora Siger

## Informações do Projeto

**Nome do Projeto:** SIGIC — Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia Aurora Siger

**Desenvolvido por:** Pedro Henrique Canavezi — RM 570298

---

## Descrição do Sistema

O SIGIC é um sistema computacional que representa e otimiza a infraestrutura de uma colônia marciana fictícia chamada **Aurora Siger**. A colônia é modelada como um **grafo**, onde:

- **Vértices** representam os módulos (habitação, energia, comunicação, etc.)
- **Arestas** representam as conexões entre módulos com pesos relacionados a distância e custo energético
- **Algoritmos de redes** (BFS, DFS e Dijkstra) são usados para explorar, analisar e otimizar o funcionamento da rede

O sistema roda no **terminal** com um menu de navegação intuitivo que permite visualizar a infraestrutura, consultar módulos, executar algoritmos de roteamento, simular falhas e analisar eficiência energética.

---

## Estrutura dos Arquivos

```
sistema-sigic-aurora-siger/
├── codigo_fonte.py                    # Arquivo principal do sistema
├── README.md                          # Este arquivo
├── link_video.txt                     # Placeholder para link do vídeo no YouTube
├── rede_colonia.pdf                   # Diagrama da rede (formato PDF)
├── documentacao_complementar.pdf      # Documentação técnica (formato PDF)
└── arquivos_auxiliares/
    ├── dados_modulos.txt              # Tabela dos módulos e seus atributos
    └── descricao_rede.txt             # Descrição das conexões e topologia
```

---

## Como Executar

### Requisitos
- Python 3.6 ou superior
- Sem dependências externas (bibliotecas padrão apenas)

### Passos para Executar

1. Abra um terminal (cmd, PowerShell ou bash)
2. Navegue até a pasta do projeto:
   ```bash
   cd /caminho/para/sistema-sigic-aurora-siger
   ```
3. Execute o arquivo principal:
   ```bash
   python codigo_fonte.py
   ```
4. Um menu será exibido no terminal. Escolha uma opção digitando o número correspondente (1-9 ou 0 para sair)

---

## Funcionalidades Principais

O sistema oferece as seguintes funcionalidades acessíveis via menu:

1. **Visualizar Módulos da Colônia** — Exibe todos os 8 módulos com seus atributos (consumo, prioridade, capacidade, status)
2. **Visualizar Conexões da Rede** — Lista todas as arestas e seus pesos
3. **Mostrar Matriz de Adjacência** — Exibe a representação em matriz das conexões
4. **Executar BFS** — Busca em largura a partir de um módulo inicial
5. **Executar DFS** — Busca em profundidade a partir de um módulo inicial
6. **Calcular Caminho Mínimo com Dijkstra** — Encontra a rota otimizada entre dois módulos
7. **Consultar Módulo Específico** — Mostra informações detalhadas de um módulo
8. **Simular Falha Operacional** — Marca um módulo como em falha e analisa o impacto na rede
9. **Analisar Eficiência Energética e ESG** — Gera relatório de sustentabilidade e recomendações
10. **Sair** — Encerra o programa

---

## Algoritmos Utilizados

### 1. BFS (Busca em Largura)
- **Objetivo:** Explorar a rede em nível por nível a partir de um módulo de origem
- **Uso:** Identificar módulos próximos ou acessíveis rapidamente
- **Implementação:** Usa fila (estrutura FIFO)

### 2. DFS (Busca em Profundidade)
- **Objetivo:** Explorar a rede seguindo um caminho profundo antes de voltar
- **Uso:** Detectar ciclos ou explorar ramos completos da rede
- **Implementação:** Usa pilha (estrutura LIFO)

### 3. Dijkstra
- **Objetivo:** Encontrar o caminho de menor custo entre dois módulos
- **Uso:** Otimizar rotas de distribuição de energia minimizando perdas
- **Implementação:** Seleciona o nó não visitado com menor distância acumulada a cada iteração

---

## Estruturas de Dados Utilizadas

### 1. **Listas**
- `modulos`: armazena os nomes de todos os 8 módulos da colônia
- `conexoes`: armazena todas as tuplas de conexões

### 2. **Dicionários**
- `modulo_info`: mapeia cada módulo para seus atributos (consumo, prioridade, capacidade, comunicação, status)
- `indice_modulo`: mapeia nomes de módulos para índices na matriz de adjacência
- `adjacencia`: implementa a lista de adjacência do grafo

### 3. **Tuplas**
- `fixed_connections`: conjunto imutável de todas as conexões (origem, destino, peso)
- Cada tupla em `fixed_connections` representa uma aresta com pesos

### 4. **Matrizes (Listas de Listas)**
- `matriz_adjacencia`: matriz 8x8 representando as conexões e pesos entre todos os pares de módulos

---

## Modelagem Matemática: Perda Energética

### Fórmula

$$\text{perda} = \text{distância} \times \text{consumo\_destino} \times \text{taxa\_perda}$$

### Variáveis

- **distância** (ou peso da aresta): distância física/lógica entre dois módulos (em unidades arbitrárias)
- **consumo_destino**: consumo energético do módulo que recebe energia (em kW)
- **taxa_perda**: taxa fixa de perda de energia por unidade de distância (padrão: 0.02 ou 2% por unidade)

### Interpretação

A fórmula calcula a energia perdida durante a transmissão ao longo de uma conexão. Quanto maior a distância ou consumo do destino, maior a perda. Essa modelagem permite:
- Otimizar rotas para minimizar desperdícios
- Planejar expansão de forma eficiente
- Identificar conexões problemáticas

---

## Sustentabilidade e Governança (ESG)

O sistema implementa análise de sustentabilidade através de:

### Recomendações Geradas Automaticamente

1. **Priorização de Sistemas Críticos**
   - Priorizar módulos de suporte de vida (Produção de Oxigênio, Suporte Médico)
   - Garantir operação contínua do Centro de Controle
   - Manter Habitação sempre operacional

2. **Redução de Desperdício Energético**
   - Usar Dijkstra para encontrar rotas com menor custo
   - Evitar conexões longas quando há alternativas curtas
   - Calcular e monitorar perdas em cada rota

3. **Redundância em Módulos Críticos**
   - Detectar módulos críticos sem redundância
   - Alertar para conexões que colocam a rede em risco
   - Sugerir expansão de ligações para maior resiliência

4. **Planejamento de Expansão**
   - Analisar capacidade total de armazenamento
   - Verificar carga média por módulo
   - Recomendar distribuição equilibrada de novos módulos

5. **Governança Tecnológica**
   - Registrar todas as falhas antes de decisões automáticas
   - Exibir análise clara de impacto antes de isolamento de módulos
   - Permitir consulta de estados antes de simulações

---

## Exemplos de Uso

### Exemplo 1: Encontrar Rota Ótima de Energia

Suponha que você quer enviar energia do módulo **Armazenamento de Energia** para o módulo **Suporte Médico**:

1. Escolha menu opção **6** (Dijkstra)
2. Selecione "Armazenamento de Energia" como origem
3. Selecione "Suporte Médico" como destino
4. O sistema exibe:
   - Caminho: `Armazenamento de Energia -> Comunicação -> Suporte Médico`
   - Custo: 8.5 (soma dos pesos das arestas)
   - Perda: ~2.15 kW (calculada pela fórmula de perda)

### Exemplo 2: Explorar a Rede com BFS

Para explorar a rede a partir da **Habitação**:

1. Escolha menu opção **4** (BFS)
2. Selecione "Habitação"
3. O sistema exibe a ordem de visita em largura:
   `Habitação -> Centro de Controle -> Armazenamento de Energia -> Comunicação -> Agricultura -> Produção de Oxigênio -> Laboratório Científico -> Suporte Médico`

### Exemplo 3: Simular Falha e Analisar Impacto

Para simular uma falha no módulo **Centro de Controle**:

1. Escolha menu opção **8** (Simular Falha)
2. Digite "Centro de Controle"
3. O sistema:
   - Marca o módulo como "Falha"
   - Verifica conectividade com a rede de energia
   - Exibe conexões críticas que foram afetadas
   - Sugere isolamento controlado

---

## Estrutura Técnica do Código

O arquivo `codigo_fonte.py` é organizado em seções:

1. **Definição da Rede**
   - Listas de módulos
   - Dicionário de atributos
   - Tuplas de conexões
   - Matriz e lista de adjacência

2. **Funções de Visualização**
   - `mostrar_modulos()`, `mostrar_conexoes()`, `mostrar_matriz()`

3. **Algoritmos de Busca**
   - `bfs()`, `dfs()`, `dijkstra()`

4. **Funções de Análise**
   - `calcular_perda_energetica()`, `calcular_perda_rota()`
   - `consultar_modulo()`, `simular_falha()`
   - `identificar_criticas()`, `analisar_eficiencia()`

5. **Interface de Usuário**
   - `escolher_modulo()`, `menu()`
   - Entrada/saída no terminal

---

## Detalhes da Colônia Aurora Siger

A colônia é composta por **8 módulos essenciais**:

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

---

## Integração com Disciplinas

O projeto integra conteúdos de várias disciplinas:

- **Algoritmos e Grafos:** Implementação de BFS, DFS e Dijkstra
- **Estruturas de Dados:** Listas, matrizes, tuplas, dicionários
- **Programação em Python:** Sintaxe, funções, estruturas de controle
- **Modelagem Matemática:** Fórmula de perda energética
- **Cálculo Diferencial:** Análise de crescimento e otimização
- **Sustentabilidade ESG:** Análise de eficiência e governança tecnológica

---

## Licença e Informações

- **Instituição:** Aurora Siger (Simulação Marciana)
- **Tipo:** Trabalho acadêmico — Disciplina de Algoritmos e Estruturas de Dados
- **Data de Criação:** 2026
- **Versão:** 1.0

---

**Nota:** Para demonstração em vídeo, execute o programa e navegue pelo menu, demonstrando cada funcionalidade com exemplos práticos.
