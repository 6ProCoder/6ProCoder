import Tkinter as tk
x = '    O    '
listt=[x]
for i in listt:
    listt.append(x)
    if  i[0:4] !='PAME':

# Create a new Tkinter window
        root = tk.Tk()
        root.geometry('165x65')
# Set the title of the window
        root.title('Grifos')

# Create a label
        label = tk.Label(root, text='mPoreis nA Me brEis?')
        label.pack()

# Create a text box
        text_box = tk.Entry(root)
        text_box.pack()

# Create a button
        def on_button_click():
            x = text_box.get()
            listt.append(x)
            if x == 'PAME':
                try:
                    for p in range(40):
                        listt.pop()
                        listt.pop()
                except IndexError:
                    print("Ante, Pame")
            return x

        button = tk.Button(root, text=x, command=on_button_click)
        button.pack()
# Start the Tkinter event loop
        root.mainloop()

