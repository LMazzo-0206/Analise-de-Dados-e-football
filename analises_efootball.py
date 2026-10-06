import pandas as pd 
dados = pd.read_csv("partidas.csv")
dados.columns = dados.columns.str.strip()
print(dados) 

dados["resultado"] = dados.apply(
    lambda linha: "Vitoria" if linha["gols_marcados"] > linha["gols_sofridos"]
    else "Derrota" if linha["gols_marcados"] < linha["gols_sofridos"]
    else "Empate",
    axis=1
)

print(dados)

contagem_resultados = dados["resultado"].value_counts()
print(contagem_resultados)

import pandas as pd

# Carregar os dados
df = pd.read_csv("partidas.csv")
df.columns = df.columns.str.strip()

# Criar automaticamente o resultado de cada partida
df["resultado"] = df.apply(
    lambda linha: "Vitoria" if linha["gols_marcados"] > linha["gols_sofridos"]
    else "Derrota" if linha["gols_marcados"] < linha["gols_sofridos"]
    else "Empate",
    axis=1
)

print("=== DADOS DAS PARTIDAS ===")
print(df.to_string(index=False))

print("\n=== TOTAL DE GOLS ===")

print("Gols marcados:", df["gols_marcados"].sum())
print("Gols sofridos:", df["gols_sofridos"].sum())


print("\n=== MÉDIA DE DESEMPENHO ===")

print("Finalizações:", df["finalizacoes"].mean())
print("Posse:", df["posse"].mean())
print("Passes:", df["passes"].mean())
print("Passes certos:", df["passes_certos"].mean())
print("Desarmes:", df["desarmes"].mean())


print("\n=== EVOLUÇÃO ===")

meio = len(df) // 2

primeira_metade = df.iloc[:meio]
segunda_metade = df.iloc[meio:]

print("\nPrimeiras 11 partidas:")
print(primeira_metade.mean(numeric_only=True))

print("\nÚltimas 11 partidas:")
print(segunda_metade.mean(numeric_only=True))


print("\n=== DESEMPENHO POR RESULTADO ===")

for resultado in ["Vitoria", "Empate", "Derrota"]:

    grupo = df[df["resultado"] == resultado]

    print(f"\n{resultado}: {len(grupo)} partidas")

    print("Gols marcados:", grupo["gols_marcados"].mean())
    print("Gols sofridos:", grupo["gols_sofridos"].mean())
    print("Finalizações:", grupo["finalizacoes"].mean())
    print("Posse:", grupo["posse"].mean())
    print("Passes:", grupo["passes"].mean())
    print("Passes certos:", grupo["passes_certos"].mean())
    print("Desarmes:", grupo["desarmes"].mean())

print("\n=== VITÓRIA x DERROTA ===")

vitorias = df[df["resultado"] == "Vitoria"]
derrotas = df[df["resultado"] == "Derrota"]

estatisticas = [
    "gols_marcados",
    "gols_sofridos",
    "finalizacoes",
    "posse",
    "passes",
    "passes_certos",
    "desarmes"
]

for estatistica in estatisticas:

    media_vitoria = vitorias[estatistica].mean()
    media_derrota = derrotas[estatistica].mean()
    diferenca = media_vitoria - media_derrota

    print(f"\n{estatistica}")
    print(f"Vitórias: {media_vitoria:.2f}")
    print(f"Derrotas: {media_derrota:.2f}")
    print(f"Diferença: {diferenca:+.2f}")

    print("\n=== VITORIA x DERROTA ===")

vitorias = df[df["resultado"] == "Vitoria"]
derrotas = df[df["resultado"] == "Derrota"]

print("\nVITORIAS:")
print("Finalizações:", vitorias["finalizacoes"].mean())
print("Posse:", vitorias["posse"].mean())
print("Passes certos:", vitorias["passes_certos"].mean())
print("Desarmes:", vitorias["desarmes"].mean())

print("\nDERROTAS:")
print("Finalizações:", derrotas["finalizacoes"].mean())
print("Posse:", derrotas["posse"].mean())
print("Passes certos:", derrotas["passes_certos"].mean())
print("Desarmes:", derrotas["desarmes"].mean())

print("\n=== MELHORES E PIORES PARTIDAS ===")

df["saldo_gols"] = df["gols_marcados"] - df["gols_sofridos"]

print("\n--- 5 MELHORES PARTIDAS ---")

melhores = df.sort_values(
    by=["saldo_gols", "finalizacoes"],
    ascending=[False, False]
).head(5)

print(
    melhores[
        [
            "partida",
            "resultado",
            "gols_marcados",
            "gols_sofridos",
            "finalizacoes",
            "posse",
            "passes_certos",
            "desarmes"
        ]
    ].to_string(index=False)
)

print("\n--- 5 PIORES PARTIDAS ---")

piores = df.sort_values(
    by=["saldo_gols", "finalizacoes"],
    ascending=[True, True]
).head(5)

print(
    piores[
        [
            "partida",
            "resultado",
            "gols_marcados",
            "gols_sofridos",
            "finalizacoes",
            "posse",
            "passes_certos",
            "desarmes"
        ]
    ].to_string(index=False)
)

print("\n=== PERFIL DAS VITORIAS ===")

media_geral = df.mean(numeric_only=True)

vitorias = df[df["resultado"] == "Vitoria"]

print("\nMedia geral:")
print("Finalizações:", round(media_geral["finalizacoes"], 2))
print("Posse:", round(media_geral["posse"], 2))
print("Passes certos:", round(media_geral["passes_certos"], 2))
print("Desarmes:", round(media_geral["desarmes"], 2))

print("\nMédia nas vitórias:")
print("Finalizações:", round(vitorias["finalizacoes"].mean(), 2))
print("Posse:", round(vitorias["posse"].mean(), 2))
print("Passes certos:", round(vitorias["passes_certos"].mean(), 2))
print("Desarmes:", round(vitorias["desarmes"].mean(), 2))

print("\nDiferença vitória x média geral:")
print(
    "Finalizações:",
    round(vitorias["finalizacoes"].mean() - media_geral["finalizacoes"], 2)
)

print(
    "Posse:",
    round(vitorias["posse"].mean() - media_geral["posse"], 2)
)

print(
    "Passes certos:",
    round(vitorias["passes_certos"].mean() - media_geral["passes_certos"], 2)
)

print(
    "Desarmes:",
    round(vitorias["desarmes"].mean() - media_geral["desarmes"], 2)
)
print("\n=== PERFIL DAS DERROTAS ===")

print("\nMédia geral:")
print("Finalizações:", round(df["finalizacoes"].mean(), 2))
print("Posse:", round(df["posse"].mean(), 2))
print("Passes certos:", round(df["passes_certos"].mean(), 2))
print("Desarmes:", round(df["desarmes"].mean(), 2))

print("\nMédia nas derrotas:")
derrotas = df[df["resultado"] == "Derrota"]

print("Finalizações:", round(derrotas["finalizacoes"].mean(), 2))
print("Posse:", round(derrotas["posse"].mean(), 2))
print("Passes certos:", round(derrotas["passes_certos"].mean(), 2))
print("Desarmes:", round(derrotas["desarmes"].mean(), 2))

print("\nDiferença derrota x média geral:")
print("Finalizações:", round(derrotas["finalizacoes"].mean() - df["finalizacoes"].mean(), 2))
print("Posse:", round(derrotas["posse"].mean() - df["posse"].mean(), 2))
print("Passes certos:", round(derrotas["passes_certos"].mean() - df["passes_certos"].mean(), 2))
print("Desarmes:", round(derrotas["desarmes"].mean() - df["desarmes"].mean(), 2))

print("\n=== FAIXAS DE DESEMPENHO ===")

# FINALIZAÇÕES
grupo = df[df["finalizacoes"] >= 8]
print("\nFinalizações >= 8:")
print("Partidas:", len(grupo))
print(grupo["resultado"].value_counts())

# PASSES CERTOS
grupo = df[df["passes_certos"] >= 120]
print("\nPasses certos >= 120:")
print("Partidas:", len(grupo))
print(grupo["resultado"].value_counts())

# POSSE
grupo = df[df["posse"] >= 50]
print("\nPosse >= 50%:")
print("Partidas:", len(grupo))
print(grupo["resultado"].value_counts())

# DESARMES
grupo = df[df["desarmes"] >= 6]
print("\nDesarmes >= 6:")
print("Partidas:", len(grupo))
print(grupo["resultado"].value_counts()) 

print("\n=== COMBINACAO DE INDICADORES ===")

grupo = df[
    (df["passes_certos"] >= 120) &
    (df["finalizacoes"] >= 8)
]

print("\n120+ passes certos E 8+ finalizações:")
print("Partidas:", len(grupo))
print(grupo["resultado"].value_counts())

grupo = df[
    (df["passes_certos"] >= 120) &
    (df["posse"] >= 50)
]

print("\n120+ passes certos E 50%+ posse:")
print("Partidas:", len(grupo))
print(grupo["resultado"].value_counts())

grupo = df[
    (df["passes_certos"] >= 120) &
    (df["finalizacoes"] >= 8) &
    (df["posse"] >= 50)
]

print("\n120+ passes certos E 8+ finalizações E 50%+ posse:")
print("Partidas:", len(grupo))
print(grupo["resultado"].value_counts())

print("\n=== PONTUAÇÃO DOS INDICADORES ===")

df["indicadores"] = (
    (df["passes_certos"] >= 120).astype(int) +
    (df["finalizacoes"] >= 8).astype(int) +
    (df["posse"] >= 50).astype(int)
)

print(df[["partida", "resultado", "indicadores"]])

print("\n=== RESULTADO POR NÚMERO DE INDICADORES ===")
print(
    pd.crosstab(
        df["indicadores"],
        df["resultado"]
    )
)
print("\n=== EFICIÊNCIA DOS PASSES ===")

df["precisao_passes"] = (
    df["passes_certos"] / df["passes"] * 100
)

print(
    df[
        ["partida", "resultado", "passes",
         "passes_certos", "precisao_passes"]
    ]
)

print("\n=== PRECISÃO MÉDIA POR RESULTADO ===")

print(
    df.groupby("resultado")["precisao_passes"].mean()
) 

import matplotlib.pyplot as plt

from pathlib import Path

PASTA_GRAFICOS = Path(__file__).parent / "graficos"
PASTA_GRAFICOS.mkdir(exist_ok=True)

plt.figure(figsize=(7, 5))

contagem_resultados.plot(kind="bar")

plt.title("Distribuição dos resultados")
plt.xlabel("Resultado")
plt.ylabel("Número de partidas")

plt.tight_layout()

plt.figure(figsize=(7, 5))

contagem_resultados.plot(kind="bar")

plt.title("Distribuição dos resultados")
plt.xlabel("Resultado")
plt.ylabel("Número de partidas")

plt.tight_layout()

plt.savefig("graficos/01_resultados.png")

plt.show()

plt.figure(figsize=(8, 5))

dados.groupby("resultado")["finalizacoes"].mean().plot(kind="bar")

plt.title("Média de finalizações por resultado")
plt.xlabel("Resultado")
plt.ylabel("Média de finalizações")

plt.tight_layout()

plt.savefig("graficos/02_finalizacoes.png")

plt.show()

plt.figure(figsize=(8, 5))

dados.groupby("resultado")["passes_certos"].mean().plot(kind="bar")

plt.title("Média de passes certos por resultado")
plt.xlabel("Resultado")
plt.ylabel("Média de passes certos")

plt.tight_layout()

plt.savefig("graficos/03_passes_certos.png")

plt.show()

plt.figure(figsize=(8, 5))

dados.groupby("resultado")["posse"].mean().plot(kind="bar")

plt.title("Média de posse de bola por resultado")
plt.xlabel("Resultado")
plt.ylabel("Média de posse (%)")

plt.tight_layout()

plt.savefig("graficos/04_posse.png")

plt.show()

# Indicadores principais

dados["indicadores"] = (
    (dados["passes_certos"] >= 120).astype(int)
    + (dados["finalizacoes"] >= 8).astype(int)
    + (dados["posse"] >= 50).astype(int)
)

taxa_vitoria_indicadores = (
    dados.groupby("indicadores")["resultado"]
    .apply(lambda x: (x == "Vitoria").mean() * 100)
)

plt.figure(figsize=(8, 5))

taxa_vitoria_indicadores.plot(kind="bar")

plt.title("Taxa de vitória conforme os indicadores atingidos")
plt.xlabel("Número de indicadores atingidos")
plt.ylabel("Taxa de vitória (%)")

plt.tight_layout()

plt.savefig("graficos/05_taxa_vitoria_indicadores.png")

plt.show()