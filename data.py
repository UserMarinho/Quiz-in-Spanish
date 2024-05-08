import pandas as pd

questions = [
    ['Con unos zapatos grandes y la cara muy pintada, soy el que hace reír a toda la chiquillada.', 'Futbolista', 'Payaso', 'Panadero', 'Cocinero', 2],
    ['Preparo ricos manjares, mi lugar es la cocina de restaurantes y hoteles. Veamos quién me adivina.', 'Camarero', 'Panadero', 'Cocinero', 'Enfermero', 3]
]

#pandas dataframe creation
df = pd.DataFrame(questions, columns=['image', 'option 1', 'option 2', 'option 3', 'option 4', 'answer'])
#saving dataframe
df.to_excel('questions.xlsx', index=False)
print('questions ok')
