# Name:
# Student Number:

# This file is the "log_viewer_additions.py" version of the "log_viewer.py" program of Assignment 2
# of Programming Principles in Semester 2, 2026.  It includes the optional additions and enhancements.


# Import the required modules.
import tkinter # Used to create the GUI.
import tkinter.messagebox # Used to show pop-up information windows.
import json # Used to convert between JSON-formatted text and Python variables.
import os # Used to delete the logs file.

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
        # The top frame holds the headings and the labels that show the log data, in a grid.
        self.top_frame = tkinter.Frame(self.main)

        # Addition: the user's name and the date of the game are also shown.
        headings = ['Name:', 'Date:', 'Letters:', 'Words:', 'Score:']
        for row in range(len(headings)):
            tkinter.Label(self.top_frame, text=headings[row], font='Arial 10 bold').grid(row=row, column=0, sticky='NE', padx=5, pady=4)

        # These labels show the log data.  Their text is set in the show_log() method.
        # Addition: "wraplength" splits a long word list across multiple lines, and the second column has a fixed
        # width (below), so that the window keeps the same width and the buttons do not jump about.
        self.name_label = tkinter.Label(self.top_frame, wraplength=400, justify='left')
        self.date_label = tkinter.Label(self.top_frame)
        self.letters_label = tkinter.Label(self.top_frame)
        self.words_label = tkinter.Label(self.top_frame, wraplength=400, justify='left')
        self.score_label = tkinter.Label(self.top_frame)

        value_labels = [self.name_label, self.date_label, self.letters_label, self.words_label, self.score_label]
        for row in range(len(value_labels)):
            value_labels[row].grid(row=row, column=1, sticky='W', padx=5, pady=4)

        # The second column always has the same width, which keeps the width of the window fixed.
        self.top_frame.columnconfigure(1, minsize=410)

        # The navigation frame holds the "First", "Previous", "Next" and "Last" buttons, with the log number in the middle.
        # Addition: "First" and "Last" buttons, using Unicode characters.
        self.nav_frame = tkinter.Frame(self.main)

        tkinter.Button(self.nav_frame, text='⏮', width=4, font='Arial 10 bold', command=self.first_log).pack(side='left', padx=3)
        tkinter.Button(self.nav_frame, text='Previous', width=10, font='Arial 10 bold', command=self.previous_log).pack(side='left', padx=3)
        self.position_label = tkinter.Label(self.nav_frame, width=10)
        self.position_label.pack(side='left', padx=3)
        tkinter.Button(self.nav_frame, text='Next', width=10, font='Arial 10 bold', command=self.next_log).pack(side='left', padx=3)
        tkinter.Button(self.nav_frame, text='⏭', width=4, font='Arial 10 bold', command=self.last_log).pack(side='left', padx=3)

        # The extra frame holds the "Statistics" and "Delete Logs" buttons.
        # Addition: "Statistics" and "Delete Logs" buttons.
        self.extra_frame = tkinter.Frame(self.main)

        tkinter.Button(self.extra_frame, text='Statistics', width=12, command=self.show_statistics).pack(side='left', padx=5)
        tkinter.Button(self.extra_frame, text='Delete Logs', width=12, command=self.delete_logs).pack(side='left', padx=5)

        # The button frames are packed at the bottom so that they stay in the same place.
        self.extra_frame.pack(side='bottom', pady=10)
        self.nav_frame.pack(side='bottom')
        self.top_frame.pack(padx=10, pady=5, anchor='w')

        # Show the first log and start the main loop (Constructor Point 5).
        self.show_log()
        tkinter.mainloop()



    # This method displays the current log
    def show_log(self):
        log = self.logs[self.current_log]

        # Logs saved by "word_find.py" do not have a name or date, so .get() is used to show "N/A" instead.
        self.name_label.configure(text=log.get('name', 'N/A'))
        self.date_label.configure(text=log.get('date', 'N/A'))

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



    # Addition: this method immediately shows the first log.
    def first_log(self):
        self.current_log = 0
        self.show_log()



    # Addition: this method immediately shows the last log.
    def last_log(self):
        self.current_log = len(self.logs) - 1
        self.show_log()



    # Addition: this method works out some statistics about the logs and shows them in a messagebox.
    def show_statistics(self):
        highest_score = self.logs[0]['score']
        total_score = 0
        most_words = len(self.logs[0]['words'])
        fewest_words = len(self.logs[0]['words'])

        for log in self.logs:
            total_score += log['score']
            if log['score'] > highest_score:
                highest_score = log['score']
            if len(log['words']) > most_words:
                most_words = len(log['words'])
            if len(log['words']) < fewest_words:
                fewest_words = len(log['words'])

        average_score = total_score / len(self.logs)

        message = 'Number of logs: ' + str(len(self.logs)) + '\n'
        message += 'Highest score: ' + str(highest_score) + '\n'
        message += 'Average score: ' + str(round(average_score, 1)) + '\n'
        message += 'Most words: ' + str(most_words) + '\n'
        message += 'Fewest words: ' + str(fewest_words)

        tkinter.messagebox.showinfo('Statistics', message)



    # Addition: this method deletes the logs file (after checking with the user) and ends the program.
    def delete_logs(self):
        if tkinter.messagebox.askyesno('Delete Logs', 'Are you sure you want to delete all of the logs?'):
            try:
                os.remove('logs.txt')
                tkinter.messagebox.showinfo('Logs Deleted', 'The logs have been deleted.')
            except Exception:
                tkinter.messagebox.showerror('Error', 'The logs could not be deleted.')
            self.main.destroy()



gui = ProgramGUI()
