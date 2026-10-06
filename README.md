# Análise de Desempenho no eFootball 

Projeto de portfólio de análise de dados desenvolvido em Python com o objetivo de investigar quais indicadores de desempenho aparecem associados às vitórias em partidas de eFootball.

## Pergunta

Quais indicadores aparecem associados às vitórias?

## Dados

Foram analisadas 22 partidas, considerando os seguintes indicadores:

- Gols marcados
- Gols sofridos
- Finalizações
- Posse de bola
- Passes
- Passes certos
- Desarmes
- Resultado da partida

## Principais resultados

- 12 vitórias, 2 empates e 8 derrotas.
- Taxa de vitórias: 54,5%.
- Nas vitórias, a média foi de 8,75 finalizações e 120,25 passes certos.
- Nas derrotas, a média foi de 4,75 finalizações e 88,25 passes certos.
- Partidas com 120+ passes certos: 8 partidas, todas terminaram em vitória.
- Partidas com 50%+ de posse: 11 partidas, 9 vitórias e 2 empates.
- Partidas com 8+ finalizações: 7 partidas, 6 vitórias e 1 empate.
- Quando 2 ou 3 dos principais indicadores foram atingidos, ocorreram 9 vitórias e 1 empate em 10 partidas, sem derrotas.

## Indicadores

Os três principais indicadores analisados foram:

1. 120+ passes certos
2. 8+ finalizações
3. 50%+ de posse

Cada partida recebeu uma pontuação de 0 a 3 de acordo com a quantidade de indicadores atingidos.

## Comparação entre vitórias e derrotas

| Indicador | Vitórias | Derrotas |
|---|---:|---:|
| Finalizações | 8,75 | 4,75 |
| Posse | 49,0% | 44,0% |
| Passes certos | 120,25 | 88,25 |
| Desarmes | 5,33 | 5,75 |

Os dados sugerem uma associação entre melhores resultados e maior volume ofensivo, maior circulação de bola e maior posse.

Os desarmes, por outro lado, não apresentaram associação clara com as vitórias.

## Conclusão

A análise sugere que, dentro da amostra estudada, as vitórias aparecem associadas principalmente a:

- Maior quantidade de finalizações
- Maior número de passes certos
- Maior posse de bola

O indicador que apresentou a associação mais forte foi o número de passes certos: nas 8 partidas com 120 ou mais passes certos, todas terminaram em vitória.

A combinação de pelo menos 2 dos 3 indicadores principais também apresentou um padrão positivo: 9 vitórias e 1 empate em 10 partidas.

## Visualizações

O projeto possui cinco visualizações:

- `01_resultados.png` — distribuição dos resultados.
- `02_finalizacoes.png` — média de finalizações por resultado.
- `03_passes_certos.png` — média de passes certos por resultado.
- `04_posse.png` — média de posse de bola por resultado.
- `05_taxa_vitoria_indicadores.png` — taxa de vitória conforme a quantidade de indicadores atingidos.

Os gráficos estão disponíveis na pasta `graficos/`.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Visual Studio Code

## O que este projeto demonstra

Este projeto demonstra habilidades de:

- Organização e análise de dados
- Análise exploratória
- Comparação de indicadores
- Criação de métricas
- Visualização de dados
- Interpretação de resultados
- Documentação de projeto
- Versionamento com Git e GitHub

## Limitações

A análise possui uma amostra de apenas 22 partidas e apresenta padrões de dados repetidos.

Os resultados são descritivos e indicam associações dentro da amostra analisada. Eles não permitem afirmar causalidade nem garantir que os mesmos padrões ocorrerão em outras partidas.

## Estrutura do projeto

```text
Analise-de-Dados-e-football/
│
├── analises_efootball.py
├── partidas.csv
├── README.md
│
└── graficos/
    ├── 01_resultados.png
    ├── 02_finalizacoes.png
    ├── 03_passes_certos.png
    ├── 04_posse.png
    └── 05_taxa_vitoria_indicadores.png
