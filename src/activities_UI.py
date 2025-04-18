import tkinter
from tkinter import Tk, ttk, constants, messagebox
import users_commands
import activities_commands

class Activities:
    def __init__(self, root, sportstracker, state):
        self._root = root
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self._state = state
        self._frame = None
        self.sportstracker = sportstracker

        self.activities_start()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def add_activity(self):
        result = users_commands.get_id(self._state["session_username"], self._state["session_password"])
        user_id = result[0]
        activity = self.activity_entry.get()
        tracker = self.tracker_entry.get()
        training_type = self.training_type_entry.get()
        activities_commands.add_activity(activity, tracker, training_type, user_id)
        messagebox.showinfo(title="Activity added", message="You successfully added an activity")

    def return_command(self):
        self.sportstracker(self._state)

    def activities_start(self):

        self._frame = tkinter.Frame(bg=self.gray)
        
        activities_frame = tkinter.LabelFrame(self._frame, text="Activities")
        activities_frame.grid(row=0, column=0, padx=20, pady=20)

        activity_label = tkinter.Label(activities_frame, text="Activity", font=("Arial", 16))
        activity_entry = ttk.Entry(activities_frame)
        self.activity_entry = activity_entry

        tracker_label = tkinter.Label(activities_frame, text="Tracker", font=("Arial", 16))
        tracker_spinbox = ttk.Spinbox(activities_frame, from_=0, to=1000)
        self.tracker_entry = tracker_spinbox
        
        training_type_label = tkinter.Label(activities_frame, text="Training type", font=("Arial", 16))
        training_type_combobox = ttk.Combobox(activities_frame, values=["", "Endurance", "Strength", "Mobility", "Fitness"])
        self.training_type_entry = training_type_combobox

        add_activity_button = tkinter.Button(self._frame, text="Add activity", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.add_activity)
        return_button = tkinter.Button(self._frame, text="Return to sportstracker", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.return_command)

        activity_label.grid(row=0, column=0)
        activity_entry.grid(row=1, column=0, padx=10)

        tracker_label.grid(row=0, column=1)
        tracker_spinbox.grid(row=1, column=1, padx=10)

        training_type_label.grid(row=0, column=2)
        training_type_combobox.grid(row=1, column=2, padx=10)

        add_activity_button.grid(row=2, column=0, pady=10)
        return_button.grid(row=3, column=0, pady=10)
