import tkinter as tk
import sys, types


def write(self,txt):
    text2.insert("end-1c", str(txt))


def on_enter():
    try:
        text2.delete("1.0", "end-1c")
        print(exec(text.get("1.0", "end-1c")))
    except:
        text2.delete("1.0", "end-1c")
        print("kono ekta ghapla hoise vai !!!")


# main window
sadman = tk.Tk()
# binding new method to the sadman object
sadman.write = types.MethodType(write, sadman)
sys.stdout = sadman

# input box
text = tk.Text(sadman)
text.pack()

# button
runButton = tk.Button(sadman, height=1, width=10, text="Run", command=on_enter)
runButton.pack()

# output text box
text2 = tk.Text(sadman)
text2.pack()


sadman.mainloop()