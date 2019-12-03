# import pandas as pd
# from geocode import cep_to_coords

# # Reading a list of CEPs from an Excel file
# # Source: https://terminaldeinformacao.com/2019/01/12/tabela-com-lista-de-ceps-do-brasil/
# df = pd.read_csv('../../data/cnes_without_lat.csv', dtype='str')
# # df = df[df['Tipo de Faixa'] == 'Total do município']
# # df = pd.read_csv('../../data/ceps.txt', usecols=['cep', 'cidade'], nrows=100)

# cep_column = 'CO_CEP'

# df[cep_column] = df[cep_column].astype(str)
# unique_ceps = df[cep_column].unique()

# df['lat'] = float('nan')
# df['lon'] = float('nan')
# for ind, elem in enumerate(unique_ceps):
#     try:
#         coords = cep_to_coords(elem)
#         df.loc[df[cep_column] == elem, 'lon'] = coords[0]
#         df.loc[df[cep_column] == elem, 'lat'] = coords[1]
#     except Exception as e:
#         print(elem)
#         print(coords)
#         print(e)

#     print('{}%...'.format(ind*100/len(unique_ceps)))

# df.to_csv('../../data/cnes_with_coords.csv', index=False)
