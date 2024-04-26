import pandas as pd

def tab_dist(dados):

    # Dados de exemplo

    # Determinar os limites dos intervalos de classe
    limite_inferior = min(dados) - 0.5
    limite_superior = max(dados) + 0.5
    largura_intervalo = 10
    intervalos = [i for i in range(int(limite_inferior), int(limite_superior) + largura_intervalo, largura_intervalo)]

    # Classificar os dados nos intervalos de classe
    frequencias = pd.cut(dados, bins=intervalos, right=False).value_counts().sort_index()

    # Criar a tabela de distribuição de frequência
    tabela_distribuicao = pd.DataFrame({'Intervalo de Classe': frequencias.index,
                                        'Frequência': frequencias.values})

    # Adicionar coluna de frequência relativa
    tabela_distribuicao['Frequência Relativa (%)'] = (tabela_distribuicao['Frequência'] / len(dados)) * 100

    # Adicionar coluna de frequência acumulada
    tabela_distribuicao['Frequência Acumulada'] = tabela_distribuicao['Frequência'].cumsum()

    return tabela_distribuicao