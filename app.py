import pandas as pd
import matplotlib.pyplot as plt

caminho_dados = "./datasets/2023_Viagem.csv"
caminho_saida_tabela = './output/tabela_2023.xlsx'
caminho_saida_grafico = './output/Viagens Por cargo público.png'
caminho_saida_grafico2 = './output/Despesa Média Por cargo público (2023).png'


pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# Lendo os dados
df_viagens = pd.read_csv(caminho_dados, encoding="Windows-1252", sep=";", decimal=",")

# Criando nova coluna de despesas
df_viagens['Despesas'] = df_viagens['Valor diárias'] + df_viagens['Valor passagens'] + df_viagens['Valor outros gastos']

# Ajustando de valores nulos na coluna de cargo
df_viagens['Cargo'] = df_viagens['Cargo'].fillna("NÃO IDENTIFICADO")

# Convertendo Colunas de datas
df_viagens['Período - Data de início'] = pd.to_datetime(df_viagens['Período - Data de início'], format="%d/%m/%Y")
df_viagens['Período - Data de fim'] = pd.to_datetime(df_viagens['Período - Data de fim'], format="%d/%m/%Y")

# Criando novas colunas de dados
df_viagens['Mês da viagem'] = df_viagens['Período - Data de início'].dt.month_name()
df_viagens['Dias de viagem'] = (df_viagens['Período - Data de fim'] - df_viagens['Período - Data de início']).dt.days

# Criando tabela consolidada
df_viagens_consolidado = (
  df_viagens
 .groupby('Cargo')
 .agg(
    despesa_media=('Despesas', 'mean'),
    duracao_media=('Dias de viagem', 'mean'),
    despesas_totais=('Despesas', 'sum'),
    destinos_mais_frequentes=('Destinos', pd.Series.mode),
    n_viagens=('Nome', 'count')
    )
 .reset_index()
)

# Filtrando tabela de dados por cargos relevantes(> 1% das viagens)
df_cargos = df_viagens['Cargo'].value_counts(normalize=True).reset_index()
df_cargos.columns = ['Cargo', 'Proporcao']
cargos_relevantes = df_cargos.loc[df_cargos['Proporcao'] > 0.01, 'Cargo']
filtro = df_viagens_consolidado['Cargo'].isin(cargos_relevantes)

# Tabela Final - Consolidade e Filtrada
df_final = df_viagens_consolidado[filtro].sort_values(by = 'n_viagens', ascending=False)

# Salvando tabela Final
df_final.to_excel(caminho_saida_tabela, index=False)

# Criando a figura 1
fig, ax = plt.subplots(figsize=(16,6))

# Plotando o Gráfico 1
ax.barh(df_final['Cargo'], df_final['n_viagens'],color='#49deac')
ax.invert_yaxis()

# Ajustando o gráfico 1
ax.set_facecolor('#3b3b47')
fig.suptitle('Viagens Por cargo público (2023)')
plt.figtext(0.79, 0.89, 'Fonte: Portal da Transparência', fontsize=8)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.yticks(fontsize = 8)
plt.xlabel('Número de viagens')

# salvando o gráfico 2
plt.savefig(caminho_saida_grafico, bbox_inches='tight')

# Criando a Figura 2
fig, ax = plt.subplots(figsize=(16,6))

# Plotando o Gráfico 2
ax.barh(df_final['Cargo'], df_final['despesa_media'],color='#42f560')
ax.invert_yaxis()

# Ajustando o gráfico 2
ax.set_facecolor('#3b3b47')
fig.suptitle('Despesa Média Por cargo público (2023)')
plt.figtext(0.79, 0.89, 'Fonte: Portal da Transparência', fontsize=8)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.yticks(fontsize = 8)
plt.xlabel('Despesa Média')

# salvando o gráfico 2
plt.savefig(caminho_saida_grafico2, bbox_inches='tight')