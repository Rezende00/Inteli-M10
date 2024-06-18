import random
import scipy.stats as stats
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
    jogos_preferidos = [jogo for jogo in jogos if jogo.genero in usuario.preferencias_genero]
    return random.choice(jogos_preferidos) if jogos_preferidos else None

def segmentar_usuarios(usuarios, critério):
    segmentos = {}
    for usuario in usuarios:
        chave = getattr(usuario, critério)
        if chave not in segmentos:
            segmentos[chave] = []
        segmentos[chave].append(usuario)
    return segmentos

def executar_teste_ab(usuarios, jogos, alteracao, critério_segmentacao):
    resultados = {'antes': [], 'depois': []}
    segmentos = segmentar_usuarios(usuarios, critério_segmentacao)
    for segmento, usuarios_segmento in segmentos.items():
        for usuario in usuarios_segmento:
            resultados['antes'].append(escolher_jogo(usuario, jogos).nome)

        alteracao(jogos)

        for usuario in usuarios_segmento:
            resultados['depois'].append(escolher_jogo(usuario, jogos).nome)

        # Reverte a alteração para o próximo segmento
        alteracao(jogos, revert=True)
    return resultados

def calcular_tamanho_amostra(poder, efeito, alfa=0.05):
    # Esta função utiliza a biblioteca scipy.stats para calcular o tamanho da amostra
    tamanho_amostra = stats.power.tt_solve_power(effect_size=efeito, alpha=alfa, power=poder)
    return tamanho_amostra

def analisar_resultados(resultados):
    antes = resultados['antes']
    depois = resultados['depois']
    # Utilize testes estatísticos aqui para comparar os resultados antes e depois
    # Por exemplo, um teste t de amostras independentes
    t_stat, p_val = stats.ttest_ind(antes, depois)
    return t_stat, p_val

# Função para alterar os jogos no teste A/B
def alteracao(jogos, revert=False):
    for jogo in jogos:
        if jogo.nome == "Fable":
            jogo.genero = "Aventura" if not revert else "Ação"

# Código principal
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

# Simule o cálculo do tamanho da amostra necessário
poder = 0.8
efeito = 0.5
tamanho_amostra = calcular_tamanho_amostra(poder, efeito)

print(f"Tamanho da amostra necessário: {tamanho_amostra}")

# Executar teste A/B
resultados = executar_teste_ab(usuarios, jogos, alteracao, 'genero')

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

# Análise dos resultados
t_stat, p_val = analisar_resultados(resultados)
print(f"Resultado do teste t: {t_stat}, p-valor: {p_val}")