from tkinter import *
from words import RandomWordsGenerator

score = 0

random_words_generator = RandomWordsGenerator()
words = random_words_generator.random_words

print(words)
root = Tk()
root.config(background='white')

score_label = Label(root, text=f'Score: {score}', background='white',)
score_label.pack()

label = Label(root, background='white',
              text='Typing Speed Calculator!', font=('Arial', 30, 'bold'))
label.pack()

explanation_label = Label(root, background='white',
                          text='Type the word on the screen as fast and accurate as you can!')
explanation_label.pack()

focus_word = Label(root, background='light blue',
                   text=words[0], font=('Arial', 20, 'bold'))
focus_word.pack()
words_to_type = Label(root, background='light blue',
                      text=words[1:10], wraplength=1000)
words_to_type.pack()

entry = Entry()
entry.pack()
entry.focus()


def next_word(event):
    global score, words
    typed_word = entry.get().strip().lower()
    current_word = words[0]
    if typed_word == current_word.lower():
        score += 1
    words.remove(current_word)
    score_label.config(text=f'Score: {score}')
    focus_word.config(text=words[0])
    words_to_type.config(text=words[1:10])
    entry.delete(0, END)


root.bind('<space>', next_word)
# root.bind('<return>', next_word)

root.mainloop()
