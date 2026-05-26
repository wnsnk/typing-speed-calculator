from tkinter import *
from dictionary_cleaner import RandomWordsGenerator

TITLE_FONT = ('Arial', 30, 'bold')
SUBTITLE_FONT = ('Arial', 20, 'bold')
score = 0
total_words_typed = 0

countdown_seconds = 60
start_timer = False
clock_running = False
clock = None
clock_label = None
clock_timer = None


random_words_generator = RandomWordsGenerator()
words = random_words_generator.random_words

print(words)
root = Tk()
root.config(background='white')

score_label = Label(root, text=f'Score: {score}', background='white',)
score_label.pack()

label = Label(root, background='white',
              text='Typing Speed Calculator!', font=TITLE_FONT)
label.pack()

explanation_label = Label(root, background='white',
                          text='Type the word on the screen as fast and accurate as you can!')
explanation_label.pack()

focus_word = Label(root, background='light blue',
                   text=words[0], font=SUBTITLE_FONT)
focus_word.pack()
words_to_type = Label(root, background='light blue',
                      text=words[1:10], wraplength=1000)
words_to_type.pack()

entry = Entry()
entry.pack()
entry.focus()


def new_window():
    global clock, clock_label, clock_timer
    root.update_idletasks()
    x = root.winfo_x()
    y = root.winfo_y()

    clock = Toplevel(root, background='white')
    clock.geometry("+%d+%d" % (x + root.winfo_width(), y))
    clock.title('COUNTDOWN')
    clock_label = Label(clock, text='Time start!',
                        background='white', font=SUBTITLE_FONT, padx=20, pady=20)
    clock_label.pack()
    clock_timer = Label(clock, text=countdown_seconds,
                        padx=20, pady=20, background='white', font=TITLE_FONT)
    clock_timer.pack()
    clock.after(10, entry.focus_set)


def timer():
    global countdown_seconds, clock_running, clock, clock_label, clock_timer, start_timer
    if not clock_running:
        new_window()
        clock_running = True
    if countdown_seconds >= 0:
        clock_timer.config(text=countdown_seconds)
        countdown_seconds -= 1
        clock.after(1000, timer)
    if countdown_seconds == 0:
        focus_word.config(text=f'FINAL SCORE: {score}')
        words_to_type.config(
            text=f'Total words typed: {total_words_typed}\nTotal spelled correctly: {score}\nPercentage correct: {int((score / total_words_typed) * 100)}%')
        clock.destroy()
        clock.update()
        clock_running = False
        start_timer = False


def next_word(event):
    global score, words, start_timer, total_words_typed
    if not start_timer:
        timer()
    start_timer = True
    typed_word = entry.get().strip().lower()
    current_word = words[0]
    if typed_word == current_word.lower():
        score += 1
        total_words_typed += 1
    else:
        total_words_typed += 1

    words.remove(current_word)
    score_label.config(text=f'Score: {score}')
    focus_word.config(text=words[0])
    words_to_type.config(text=words[1:10])
    entry.delete(0, END)


root.bind('<space>', next_word)

root.mainloop()
