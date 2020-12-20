# write tkinter as Tkinter to be Python 2.x compatible
import tkinter as tk

root = tk.Tk()

img = tk.PhotoImage(file='figures/1_0_kingdom_map.gif')
panel = tk.Label(root,image=img)
panel.pack()

# castle_button = tk.Button(panel)
# castle_button.pack()

root.mainloop()