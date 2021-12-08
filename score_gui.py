import tkinter as tk


text_grid_list = []
def populate(frame):
    '''Put in some fake data'''
    for row in range(2):
        row_data = []
        text_id = tk.Text(frame, width=20, height=1)
        text_id.grid(row=row+1, column=0)
        row_data.append(text_id)

        text_name = tk.Text(frame, width=20, height=1)
        text_name.grid(row=row + 1, column=1)
        row_data.append(text_name)

        text_country = tk.Text(frame, width=20, height=1)
        text_country.grid(row=row + 1, column=2)
        row_data.append(text_country)

        text_score_1= tk.Text(frame, width=20, height=1)
        text_score_1.grid(row=row + 1, column=3)
        row_data.append(text_score_1)

        text_grid_list.append(row_data)




        # tk.Text(frame, width=10, height=1).grid(row=row+1, column=1)
        # tk.Text(frame, width=10, height=1).grid(row=row+1, column=2)
        # tk.Text(frame, width=10, height=1).grid(row=row+1, column=3)
        # tk.Text(frame, width=10, height=1).grid(row=row+1, column=4)
        # tk.Text(frame, width=10, height=1).grid(row=row+1, column=5)
        # tk.Text(frame, width=10, height=1).grid(row=row+1, column=6)

        # tk.Entry(frame, bd =5).grid(row=row, column=0)
        # tk.Entry(frame, bd=5).grid(row=row, column=1)
        # tk.Entry(frame, bd=5).grid(row=row, column=2)
        # tk.Entry(frame, bd=5).grid(row=row, column=3)

        # tk.Label(frame, text="%s" % row, width=3, borderwidth="1",
        #          relief="solid").grid(row=row, column=0)
        # t="this is the second column for row %s" %row
        # tk.Label(frame, text=t).grid(row=row, column=1)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def find_winners():
    print("find winners")
    print(text_grid_list)
    print(text_grid_list[0][0].get("1.0", tk.END))

root = tk.Tk()

tk.Label(root,text="Event name").pack(side="top")
tk.Text(root, width=20, height=1).pack(side="top")


canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")

tk.Button(root, text="Find winners", command=find_winners).pack(side="bottom")

vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

tk.Label(frame, text= "Player Id", width=10, height=1).grid(row=0, column=0)
tk.Label(frame, text= "Name", width=20, height=1).grid(row=0, column=0)
tk.Label(frame, text= "Country", width=10, height=1).grid(row=0, column=1)
tk.Label(frame, text= "Score 1", width=10, height=1).grid(row=0, column=2)
tk.Label(frame, text= "Score 2", width=10, height=1).grid(row=0, column=3)
tk.Label(frame, text= "Score 3", width=10, height=1).grid(row=0, column=4)
tk.Label(frame, text= "Score 4", width=10, height=1).grid(row=0, column=5)
tk.Label(frame, text= "Score 5", width=10, height=1).grid(row=0, column=6)
populate(frame)




root.mainloop()