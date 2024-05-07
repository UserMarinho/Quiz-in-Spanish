import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random 

df = pd.read_excel('questions.xlsx')
questions = df.sample(n=2).values.tolist()

#definig colors 
background_color = '#ECECEC'
text_color = "#333333"
button_color = '#4CAF50'
button_text_color = '#FFFFFF'

#window configuration 
window = tk.Tk()
window.title('Quiz')
window.geometry('400x450')
window.config(bg=background_color)
window.option_add('*Font', 'Arial')

#image
q = questions[random.randint(0, 1)]
text_label = tk.Label(window, text='¿qué es esto?', bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
text_label.pack(pady=10)
image = PhotoImage(file=q[0])
image_label = tk.Label(window, image=image, bg=background_color)
image_label.pack(pady=20)

#answer options
correct_asnwer = tk.IntVar()
option1_btn = tk.Button(window, text=q[1], width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option1_btn.pack(pady=10)
option2_btn = tk.Button(window, text=q[2], width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option2_btn.pack(pady=10)
option3_btn = tk.Button(window, text=q[3], width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option3_btn.pack(pady=10)
option4_btn = tk.Button(window, text=q[4], width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option4_btn.pack(pady=10)
play_again_btn = tk.Button(window, text='Jugar de nuevo', width=30, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'))


window.mainloop()
