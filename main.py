import pandas as pd

questions = [
    ['image', 'a', 'b', 'c', 'd', 'answer']
]

#creation of pandas dataframe
df = pd.DataFrame(questions, columns=['image', 'option 1', 'option 2', 'option 3', 'option 4', 'answer'])
#saving dataframe
df.to_excel('questions.xlsx', index=False)
print('questions ok')