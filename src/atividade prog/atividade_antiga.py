# imports
import random
from collections import Counter # armazenar elementos em dicionário pra plota o grafico
import plotly.graph_objects as go # plota o grafico

# não mudei nada nas classes
class Usuario:
    def __init__(self, idade, genero, preferencias_genero, tempo_medio_jogo):
        self.idade = idade
        self.genero = genero
        self.preferencias_genero = preferencias_genero
        self.tempo_medio_jogo = tempo_medio_jogo

class Jogo:
    def __init__(self, nome, genero, faixa_etaria, tempo_medio_jogo):
        self.nome = nome
        self.genero = genero
        self.faixa_etaria = faixa_etaria
        self.tempo_medio_jogo = tempo_medio_jogo

def escolher_jogo(usuario, jogos):
    jogos_preferidos = [jogo for jogo in jogos if jogo.genero in usuario.preferencias_genero and usuario.idade >= jogo.faixa_etaria]
    return random.choice(jogos_preferidos).nome if jogos_preferidos else 'Nenhum'

def aplicar_teste_ab(jogos):
    for jogo in jogos:
        if jogo.nome == "Fable":
            jogo.faixa_etaria = 12  # redução da faixa etária mínima

def coletar_dados_teste_ab(usuarios, jogos):
    escolhas_antes = []
    escolhas_depois = []

    # Coletar dados antes da alteração
    for _ in range(1000):
        escolhas = [escolher_jogo(usuario, jogos) for usuario in usuarios]
        escolhas = [escolha for escolha in escolhas if escolha != 'Nenhum']
        escolhas_antes.append(escolhas)

    aplicar_teste_ab(jogos)

    # Coletar dados depois da alteração
    for _ in range(1000):
        escolhas = [escolher_jogo(usuario, jogos) for usuario in usuarios]
        escolhas = [escolha for escolha in escolhas if escolha != 'Nenhum']
        escolhas_depois.append(escolhas)

    return escolhas_antes, escolhas_depois

def analisar_resultados(escolhas_antes, escolhas_depois):
    contagem_antes = Counter([escolha for sublist in escolhas_antes for escolha in sublist])
    contagem_depois = Counter([escolha for sublist in escolhas_depois for escolha in sublist])

    return contagem_antes, contagem_depois

# aqui é onde irei plotar o gráfico e destrinchar o dicionário que fiz com a biblioteca collections.
def relatorio_resultados(contagem_antes, contagem_depois):
    nomes_jogos = list(set(contagem_antes.keys()).union(contagem_depois.keys()))
    valores_antes = [contagem_antes[nome] for nome in nomes_jogos]
    valores_depois = [contagem_depois[nome] for nome in nomes_jogos]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=nomes_jogos,
        y=valores_antes,
        name='Antes da Alteração',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=nomes_jogos,
        y=valores_depois,
        name='Depois da Alteração',
        marker_color='red'
    ))

    fig.update_layout(
        title='Preferência dos jogos ANTES e DEPOIS da alteração',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Número de escolhas',
            titlefont_size=16,
            tickfont_size=14,
        ),
        barmode='group',
        bargap=0.15,
        bargroupgap=0.1
    )

    fig.show()

# Aqui na simulação só adicionei valores e jogos que gosto 👌
# Simulação de dados de usuários e jogos:
usuarios = [Usuario(20, "Masculino", ["Ação"], 60),
            Usuario(16, "Feminino", ["Aventura"], 70),
            Usuario(15, "Masculino", ["RPG"], 120),
            Usuario(13, "Masculino", ["Aventura"], 78),
            Usuario(16, "Feminino", ["RPG"], 90)
            ]
jogos = [Jogo("Tekken", "Ação", 12, 55),
        Jogo("Shadow of the Colossus", "Aventura", 12, 60),
        Jogo("Fable", "RPG", 16, 100),
        Jogo("Rayman", "Aventura", 12, 65),
        Jogo("Final Fantasy", "RPG", 16, 80),
        ]

def main():
    escolhas_antes, escolhas_depois = coletar_dados_teste_ab(usuarios, jogos)
    contagem_antes, contagem_depois = analisar_resultados(escolhas_antes, escolhas_depois)
    relatorio_resultados(contagem_antes, contagem_depois)

if __name__ == "__main__":
    main()