import pandas as pd
from geocode import cep_to_coords

# Reading a list of CEPs from an Excel file
# Source: https://terminaldeinformacao.com/2019/01/12/tabela-com-lista-de-ceps-do-brasil/
df = pd.read_excel('../../data/Lista_de_CEPs.xlsx', dtype='str')
df = df[df['Tipo de Faixa'] == 'Total do município']
# df = pd.read_csv('../../data/ceps.txt', usecols=['cep', 'cidade'], nrows=100)

cep_column = 'CEP Inicial'

df[cep_column] = df[cep_column].astype(str)
unique_ceps = df[cep_column].unique()

df['lat'] = float('nan')
df['lon'] = float('nan')
for cep in unique_ceps:
    try:
        coords = cep_to_coords(cep)
        df.loc[df[cep_column] == cep, 'lat'] = coords[0]
        df.loc[df[cep_column] == cep, 'lon'] = coords[1]
    except Exception as e:
        print(cep)
        print(coords)
        print(e)

df.to_excel('../../data/list_with_coords.xlsx', index=False)
