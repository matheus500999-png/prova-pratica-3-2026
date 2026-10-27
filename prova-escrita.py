1
import pandas as pd
import numpy as np
0
df = pd.read_csv('vendas_loja.csv')

print(df.head())
print(df.shape)
df.info()

2
print(df.describe())

media = df['preco'].mean()
print("A média do preço é:", media)

3
precos = df['preco'].to_numpy()

print("Média:", np.nanmean(precos))
print("Maior preço:", np.nanmax(precos))
print("Menor preço:", np.nanmin(precos))
print("Quantidade:", precos.size)

4
print(df.isnull().sum())

df['preco'] = df['preco'].fillna(df['preco'].mean())
df['quantidade'] = df['quantidade'].fillna(0)

print(df.isnull().sum())

5
print(df.shape)
print(df.duplicated().sum())

df = df.drop_duplicates()

print(df.shape)

6
df['total'] = df['preco'] * df['quantidade']

print(df[['produto', 'preco', 'quantidade', 'total']])

7
vendas = df[df['total'] >= 500]

print(vendas)
print(len(vendas))

8
vendas_sul = df[(df['regiao'] == 'Sul') & (df['quantidade'] > 5)]

print(vendas_sul)