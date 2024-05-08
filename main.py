import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random 

df = pd.read_excel('questions.xlsx')
questions = df.sample(n=2).values.tolist()
score = 0
current_question = 0

def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL)
    option2_btn.config(text=option2, state=tk.NORMAL)
    option3_btn.config(text=option3, state=tk.NORMAL)
    option4_btn.config(text=option4, state=tk.NORMAL)


#definig colors 
background_color = '#ECECEC'
text_color = "#333333"
button_color = '#4CAF50'
button_text_color = '#FFFFFF'

#window configuration 
window = tk.Tk()
window.title('Quiz')
window.geometry('400x500')
window.config(bg=background_color)
window.option_add('*Font', 'Arial')

#question 
text_label = tk.Label(window, text='¿Lo qué soy?', bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
text_label.pack(pady=10)
image = PhotoImage(file='mistery.png')
image_label = tk.Label(window, image=image, bg=background_color)
image_label.pack(pady=20)
question_label = tk.Label(window, text='',wraplength=380 ,bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
question_label.pack(pady=10)

#answer options
correct_asnwer = tk.IntVar()
option1_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option1_btn.pack(pady=10)
option2_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option2_btn.pack(pady=10)
option3_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option3_btn.pack(pady=10)
option4_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option4_btn.pack(pady=10)
play_again_btn = tk.Button(window, text='Jugar de nuevo', width=30, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'))

display_question()

window.mainloop()
