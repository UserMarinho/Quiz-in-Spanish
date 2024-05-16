import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import PhotoImage

df = pd.read_excel('_internal/questions.xlsx')
number_of_question = 5
questions = df.sample(n=number_of_question).values.tolist()
score = 0
current_question = 0

def check_up(answer):
    global score, current_question
    if answer == correct_answer.get():
        score += 1
    btns = [option1_btn, option2_btn, option3_btn, option4_btn]
    for btn in btns:
        btn.config(state=tk.DISABLED)
        if btn['text'] != questions[current_question][correct_answer.get()]:
            btn.config(bg='red')
    current_question += 1 
    if current_question < len(questions):
        window.after(500, display_question)
    else:
        window.after(500, show_result)


def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, bg=button_color, state=tk.NORMAL, command=lambda:check_up(1))
    option2_btn.config(text=option2, bg=button_color, state=tk.NORMAL, command=lambda:check_up(2))
    option3_btn.config(text=option3, bg=button_color, state=tk.NORMAL, command=lambda:check_up(3))
    option4_btn.config(text=option4, bg=button_color, state=tk.NORMAL, command=lambda:check_up(4))
    correct_answer.set(answer)

def show_result():
    messagebox.showinfo(title='Quiz finalizado', message=f'Pontuação final: {score}/{len(questions)}')
    btns = [option1_btn, option2_btn, option3_btn, option4_btn]
    for btn in btns:
        btn.config(state=tk.DISABLED)
    play_again_btn.pack(pady=10)

def play_again():
    global score, current_question, questions
    score = 0
    current_question = 0
    questions = df.sample(n=number_of_question).values.tolist()
    display_question()
    play_again_btn.forget()

#definig colors 
background_color = '#ECECEC'
text_color = "#333333"
button_color = '#4CAF50'
button_text_color = '#FFFFFF'

#window configuration 
window = tk.Tk()
window.title('Quiz')
window.geometry('400x500')
window.resizable(False, False)
window.config(bg=background_color)
window.option_add('*Font', 'Arial')

#question 
text_label = tk.Label(window, text='¿Lo que soy?', bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
text_label.pack(pady=10)
image = PhotoImage(file='_internal/images/mistery.png')
image_label = tk.Label(window, image=image, bg=background_color)
image_label.pack(pady=20)
question_label = tk.Label(window, text='',wraplength=380 ,bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
question_label.pack(pady=10)

#answer options
correct_answer = tk.IntVar()
option1_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option1_btn.pack(pady=10)
option2_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option2_btn.pack(pady=10)
option3_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option3_btn.pack(pady=10)
option4_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option4_btn.pack(pady=10)
play_again_btn = tk.Button(window, text='Jugar de nuevo', width=20, bg='yellow', fg='grey', font=('Arial', 10, 'bold'), command=play_again)

display_question()

window.mainloop()
