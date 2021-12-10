import tkinter as tk
from tkinter import messagebox


text_grid_list = []
def populate(frame):
    for row in range(50):
        row_data = []

        tk.Label(frame, text=str(row+1), width=2, height=1).grid(row=row+1, column=0)

        text_id = tk.Text(frame, width=15, height=1)
        text_id.grid(row=row+1, column=1)
        row_data.append(text_id)

        text_name = tk.Text(frame, width=25, height=1)
        text_name.grid(row=row + 1, column=2)
        row_data.append(text_name)

        text_country = tk.Text(frame, width=15, height=1)
        text_country.grid(row=row + 1, column=3)
        row_data.append(text_country)

        text_score_1= tk.Text(frame, width=10, height=1)
        text_score_1.grid(row=row + 1, column=4)
        row_data.append(text_score_1)

        text_score_2 = tk.Text(frame, width=10, height=1)
        text_score_2.grid(row=row + 1, column=5)
        row_data.append(text_score_2)

        text_score_3 = tk.Text(frame, width=10, height=1)
        text_score_3.grid(row=row + 1, column=6)
        row_data.append(text_score_3)

        text_score_4 = tk.Text(frame, width=10, height=1)
        text_score_4.grid(row=row + 1, column=7)
        row_data.append(text_score_4)

        text_score_5 = tk.Text(frame, width=10, height=1)
        text_score_5.grid(row=row + 1, column=8)
        row_data.append(text_score_5)

        text_grid_list.append(row_data)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def find_winners():
    try:
        id_list = []
        names_list = []
        country_list = []
        final_score_list = []
        for r in text_grid_list:
            id = r[0].get("1.0", tk.END).strip().replace("\n","")
            name = r[1].get("1.0", tk.END).strip().replace("\n","")
            country = r[2].get("1.0", tk.END).strip().replace("\n","")
            s1 = r[3].get("1.0", tk.END).strip().replace("\n","")
            s2 = r[4].get("1.0", tk.END).strip().replace("\n","")
            s3 = r[5].get("1.0", tk.END).strip().replace("\n","")
            s4 = r[6].get("1.0", tk.END).strip().replace("\n","")
            s5 = r[7].get("1.0", tk.END).strip().replace("\n","")
            if(id != ""):
                id_list.append(id)
                names_list.append(name)
                country_list.append(country)
                final_score = round((float(s1)+float(s2)+float(s3)+float(s4)+float(s5)-max(float(s1),float(s2),float(s3),float(s4),float(s5))-min(float(s1),float(s2),float(s3),float(s4),float(s5)))/3,2)
                final_score_list.append(final_score)

        final_data = []
        length = len(id_list)
        count=0
        while(length>count):
            data=[]
            max_score = max(final_score_list)
            index_max = final_score_list.index(max_score)
            data.append(id_list[index_max])
            data.append(names_list[index_max])
            data.append(country_list[index_max])
            data.append(final_score_list[index_max])
            final_data.append(data)
            del id_list[index_max]
            del names_list[index_max]
            del country_list[index_max]
            del final_score_list[index_max]

            count+=1

        print(final_data)

        message_text = ""

        c = 0
        for m_row in final_data:
            c+=1
            row_text = str(c) + " -> "
            for data in m_row:
                row_text = row_text + "  " + str(data)
            message_text = message_text + row_text + "\n"

        messagebox.showinfo("Final Scores", message_text)

        try:
            event_name = event_text.get("1.0", tk.END).strip().replace("\n","")
            if(len(event_name)>215):
                event_name = event_name[:215]
            file = open(event_name+".txt", "w")
            file.write(event_name + "\n\n" + message_text)

        except:
            print("Error in saving data into file")
            messagebox.showerror("Data file Error", "Error in saving data into file")

    except:
        print("Error in entered data")
        messagebox.showerror("Invalid Input", "Error in entered data")


root = tk.Tk()
root.geometry("950x736")
root.title("Taekwondo Scoring App")
root.resizable(0, 0)

tk.Label(root,text="Event name").pack(side="top")
event_text = tk.Text(root, width=110, height=1)
event_text.pack(side="top")

canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")

tk.Button(root, width=20, height=2, text="Find winners", command=find_winners).pack(side="bottom")

vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

tk.Label(frame, text= "", width=2, height=1).grid(row=0, column=0)
tk.Label(frame, text= "Player Id", width=17, height=1).grid(row=0, column=1)
tk.Label(frame, text= "Name", width=29, height=1).grid(row=0, column=2)
tk.Label(frame, text= "Country", width=17, height=1).grid(row=0, column=3)
tk.Label(frame, text= "Score 1", width=12, height=1).grid(row=0, column=4)
tk.Label(frame, text= "Score 2", width=12, height=1).grid(row=0, column=5)
tk.Label(frame, text= "Score 3", width=12, height=1).grid(row=0, column=6)
tk.Label(frame, text= "Score 4", width=12, height=1).grid(row=0, column=7)
tk.Label(frame, text= "Score 5", width=12, height=1).grid(row=0, column=8)
populate(frame)

root.mainloop()