import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random 

df = pd.read_excel('questions.xlsx')
questions = df.sample(n=1).values.tolist()

#definig colors 
background_color = '#ECECEC'
text_color = "#333333"
button_color = '#4CAF50'

#window configuration 
window = tk.Tk()
window.title('Quiz')
window.geometry('400x450')
window.config(bg=background_color)
window.option_add('*Font', 'Arial')

window.mainloop()
