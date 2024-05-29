import tkinter as tk 
import ttkbootstrap as ttk
import random 

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x135')
        self.window.title('WPM')

        # Read words from file
        self.words = open('words.txt', 'r').read().split('\n')
        self.random_word = random.choice(self.words)

        self.score_var = tk.StringVar(value='0')
        
        # Select a random word
        self.word = ttk.Label(self.window, text=self.random_word)
        self.entry = ttk.Entry(self.window, justify='center')
        self.counter = ttk.Label(self.window, textvariable=self.score_var)
        self.timer = ttk.Label(self.window, text='5')
        self.restart_button = ttk.Button(self.window, text='Restart', command=self.restart)

        # Pack the widgets
        self.word.pack()
        self.entry.pack()
        self.restart_button.pack()
        self.counter.pack()
        self.timer.pack()

        # Define initial states
        self.timeleft = 5
        self.countdown_running = False
        
        # Bind keys
        self.entry.bind('<Key>', self.textEntry)
        self.entry.bind('<Return>', self.textEntry)
        self.entry.bind('<space>', self.textEntry)

        # Run the Main GUI
        self.window.mainloop()

    def disable_entry(self):
        self.entry.config(state='disabled')
        self.entry.delete(0, tk.END)

    def enable_entry(self):
        self.entry.config(state='normal')

    def textEntry(self, event):
        # Check if the key pressed is space or enter
        if event.keysym == 'space' or event.keysym == 'Return':
            entered_word = self.entry.get().strip()
            # Check if the word is correct 
            if entered_word == self.random_word:
                current_score = int(self.score_var.get())
                self.score_var.set(str(current_score + 1))
                self.random_word = random.choice(self.words)  # Select a new random word
                self.word.config(text=self.random_word)  # Update the displayed word
                self.entry.delete(0, tk.END)

        # Start the countdown if it's not already running
        if not self.countdown_running:
            self.countdown_running = True
            self.countdown()
       
    def countdown(self):
        if self.timeleft > 0: 
            self.timeleft -= 1
            self.timer.config(text=self.timeleft)
            self.timer.after(1000, self.countdown)
        else:
            # Reset the flag when the countdown finishes
            self.countdown_running = False
            self.disable_entry()
            print(self.timeleft)

    def restart(self):
            self.entry.delete(0, tk.END)
            self.timeleft = 5
            self.score_var.set('0')
            self.random_word = random.choice(self.words)
            self.word.config(text=self.random_word)
            self.enable_entry()
            self.timer.config(text=self.timeleft)
            self.countdown_running = False
            print("Restart Pressed")
        
# Run
Main()
