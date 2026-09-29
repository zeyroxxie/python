# Name:
# Student Number:

# This file is provided to you as a starting point for the "log_viewer.py" program of Assignment 2
# of Programming Principles in Semester 2, 2026.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# Import the required modules.
import tkinter # Used to create the GUI.
import tkinter.messagebox # Used to show pop-up information windows.
import json # Used to convert between JSON-formatted text and Python variables.

class ProgramGUI:
    def __init__(self):
        # Create the main window (Constructor Point 1).
        self.main = tkinter.Tk()
        self.main.title('Word Find Log Viewer')
        self.main.resizable(False, False)

        # Load the logs from the text file (Constructor Point 2).
        try:
            file = open('logs.txt', 'r')
            self.logs = json.load(file)
            file.close()
        except Exception:
            tkinter.messagebox.showerror('Error', 'Missing/Invalid file')
            self.main.destroy()
            return

        # If the file contains no logs, there is nothing to display, so end the program.
        if len(self.logs) == 0:
            tkinter.messagebox.showerror('Error', 'There are no logs to display.')
            self.main.destroy()
            return

        # Keep track of which log is being displayed (Constructor Point 3).
        self.current_log = 0

        # Create the widgets (Constructor Point 4).
        # The top frame holds the "Letters:", "Words:" and "Score:" labels and their values, in a grid.
        self.top_frame = tkinter.Frame(self.main)

        tkinter.Label(self.top_frame, text='Letters:', font='Arial 10 bold').grid(row=0, column=0, sticky='E', padx=5, pady=5)
        tkinter.Label(self.top_frame, text='Words:', font='Arial 10 bold').grid(row=1, column=0, sticky='E', padx=5, pady=5)
        tkinter.Label(self.top_frame, text='Score:', font='Arial 10 bold').grid(row=2, column=0, sticky='E', padx=5, pady=5)

        # These labels show the log data.  Their text is set in the show_log() method.
        self.letters_label = tkinter.Label(self.top_frame)
        self.words_label = tkinter.Label(self.top_frame)
        self.score_label = tkinter.Label(self.top_frame)
        self.letters_label.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.words_label.grid(row=1, column=1, sticky='W', padx=5, pady=5)
        self.score_label.grid(row=2, column=1, sticky='W', padx=5, pady=5)

        # The bottom frame holds the "Previous" and "Next" buttons, with the log number between them.
        self.bottom_frame = tkinter.Frame(self.main)

        self.previous_button = tkinter.Button(self.bottom_frame, text='Previous', width=12, font='Arial 10 bold', command=self.previous_log)
        self.position_label = tkinter.Label(self.bottom_frame)
        self.next_button = tkinter.Button(self.bottom_frame, text='Next', width=12, font='Arial 10 bold', command=self.next_log)

        self.previous_button.pack(side='left', padx=5)
        self.position_label.pack(side='left', padx=5)
        self.next_button.pack(side='left', padx=5)

        self.top_frame.pack(padx=10, pady=5, anchor='w')
        self.bottom_frame.pack(padx=10, pady=10)

        # Show the first log and start the main loop (Constructor Point 5).
        self.show_log()
        tkinter.mainloop()



    # This method displays the current log
    def show_log(self):
        log = self.logs[self.current_log]

        # Use .join() to turn the lists of letters and words into comma-separated strings.
        self.letters_label.configure(text=', '.join(log['letters']))
        self.words_label.configure(text=', '.join(log['words']))
        self.score_label.configure(text=str(log['score']))
        self.position_label.configure(text='Log ' + str(self.current_log + 1) + '/' + str(len(self.logs)))



    # This method shows the previous log, or a messagebox if the first log is already being shown.
    def previous_log(self):
        if self.current_log == 0:
            tkinter.messagebox.showerror('No previous log', 'Already viewing first log.')
        else:
            self.current_log -= 1
            self.show_log()



    # This method shows the next log, or a messagebox if the last log is already being shown.
    def next_log(self):
        if self.current_log == len(self.logs) - 1:
            tkinter.messagebox.showerror('No next log', 'Already viewing last log.')
        else:
            self.current_log += 1
            self.show_log()



gui = ProgramGUI()
