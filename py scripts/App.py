#%%
" == Dépendaces == "
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from PIL import Image, ImageTk


#%%
" == APP == "

" App setup "
root=tk.Tk()
root.title('pr_collec')
root.geometry  ("500x400")
root.pack_propagate(False) #don't resize the windows bc of widgets
#root.resizable(0,0)       # on peut pas resize
ico = Image.open('C:/Users/proui/Pictures/bass.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)



# Frame for the TreeView
frame1=tk.LabelFrame(root,text='Collec data')
frame1.place(height=250,width=500)
pro_text=tk.Label(frame1,text="profile").place(rely=0,relx=0)
profile=tk.Entry(frame1,width=20).place(rely=0,relx=0.2)

# Frame for open file dialog = CONTAINER
file_frame=tk.LabelFrame(root,text="Scan enter")
file_frame.place(height=100,width=500,rely=0.65,relx=0)

#bottoms    
# En command sur les boutons on peut mettre des fonctions qu'on a codées !
#button1=tk.Button(file_frame,text="Browse a file") #needs a command

# syntaxe plus uniforme et pas besoin de 2 lignes 
button1=tk.Entry(file_frame,width=35).place(rely=0.65,relx=0)
up1=tk.Label(file_frame,text="Title").place(rely=0.40,relx=0)

button2=tk.Entry(file_frame,width=10).place(rely=0.65,relx=0.5)
up2=tk.Label(file_frame,text="Scan").place(rely=0.40,relx=0.5)

button3=tk.Entry(file_frame,width=5).place(rely=0.65,relx=0.71)
up3=tk.Label(file_frame,text="Favorite").place(rely=0.40,relx=0.7)

button4=tk.Button(file_frame,text="add").place(rely=0.6,relx=0.82) # command
button5=tk.Button(file_frame,text="cancel").place(rely=0.6,relx=0.9) # command




"""
button1=tk.Button(file_frame,text="Load file") #needs a command
button1.place(rely=0.65,relx=0.3)
"""

label_file=ttk.Label(file_frame,text="No file selected")
label_file.place(rely=0,relx=0)
label_file["text"]="tessssst"

# Scan listing viewer
tv1=ttk.Treeview(frame1)
tv1.place(relheight=1,relwidth=1) #fill the whole container w the treeview

# Scrolling : command = quand j'active ça "update les vues"
treescrolly=tk.Scrollbar(frame1,orient="vertical",command=tv1.yview)
treescrollx=tk.Scrollbar(frame1,orient="horizontal",command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom",fill="x")
treescrolly.pack(side="right",fill="y")

root.mainloop()

#%%
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()
tk.Label(master, 
         text="First Name").grid(row=0)
tk.Label(master, 
         text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()