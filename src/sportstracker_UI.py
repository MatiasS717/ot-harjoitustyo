import tkinter
from tkinter import Tk, ttk, constants, messagebox
import users_commands
import activities_commands

class Sportstracker:
    def __init__(self, root, activities, state):
        self._root = root
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self._state = state
        self._frame = None
        self.activities = activities

        self.sportstracker_start()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def activities_start(self):
        self.activities(self._state)

    def sportstracker_start(self):

        self._frame = tkinter.Frame(bg=self.gray)

        heading_label = tkinter.Label(self._frame, text="Sportstracker", bg=self.gray, fg=self.white, font=("Arial", 20))
        user_label = tkinter.Label(self._frame, text="User:", bg=self.gray, fg=self.white, font=("Arial", 16))
        activities_label = tkinter.Label(self._frame, text="Activities", bg=self.gray, fg=self.pink, font=("Arial", 16))
        activity_label = tkinter.Label(self._frame, text="Activity", bg=self.gray, fg=self.white, font=("Arial", 16))
        tracker_label = tkinter.Label(self._frame, text="Tracker", bg=self.gray, fg=self.white, font=("Arial", 16))
        training_type_label = tkinter.Label(self._frame, text="Training type", bg=self.gray, fg=self.white, font=("Arial", 16))

        heading_label.grid(row=0, column=0)
        user_label.grid(row=1, column=0)
        activities_label.grid(row=2, column=1)
        activity_label.grid(row=3, column=0)
        tracker_label.grid(row=3, column=1)
        training_type_label.grid(row=3, column=2)

        username_label = tkinter.Label(self._frame, text=self._state["session_username"], bg=self.gray, fg=self.white, font=("Arial", 16))
        username_label.grid(row=1, column=1)

        result = users_commands.get_id(self._state["session_username"], self._state["session_password"])
        user_id = result[0]
        activities = activities_commands.get_activities(user_id)
        x = 4

        for activity in activities:
            list_activity_label = tkinter.Label(self._frame, text=activity[1], bg=self.gray, fg=self.white, font=("Arial", 14))
            list_tracker_label = tkinter.Label(self._frame, text=activity[2], bg=self.gray, fg=self.white, font=("Arial", 14))
            list_training_type_label = tkinter.Label(self._frame, text=activity[3], bg=self.gray, fg=self.white, font=("Arial", 14))

            list_activity_label.grid(row=x, column=0)
            list_tracker_label.grid(row=x, column=1)
            list_training_type_label.grid(row=x, column=2)

            x += 1
        
        new_activity_button = tkinter.Button(self._frame, text="New activity", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.activities_start)
        new_activity_button.grid(row=x, column=1, pady=10)