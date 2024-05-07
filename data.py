import pandas as pd

questions = [
    ['images/doctor.png', 'Futbolista', 'Médico', 'Panadero', 'Cocinero', 2],
    ['images/chef.png', 'Camarero', 'Panadero', 'Cocinero', 'Enfermero', 3]
]

#pandas dataframe creation
df = pd.DataFrame(questions, columns=['image', 'option 1', 'option 2', 'option 3', 'option 4', 'answer'])
#saving dataframe
df.to_excel('questions.xlsx', index=False)
print('questions ok')
