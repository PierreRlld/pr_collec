#%%
" == Dépendances == "
import time
import tkinter as tk 
from tkinter import ttk, messagebox, filedialog, font
from ttkthemes import ThemedTk
import pandas as pd
from PIL import Image, ImageTk
start=time.time()
from profiles import *
end=time.time()
print(end-start)

#%%
" == APP == "

" /Setup " 
root=tk.Tk()
root.title('pr_collec')
root.geometry  ("500x400")
root.configure(background="#c5c3c6")
root.pack_propagate(False) #don't resize the windows bc of widgets
root.resizable(0,0)       # on peut pas resize
#ico = Image.open('C:/Users/proui/Pictures/bass.png')
#photo = ImageTk.PhotoImage(ico)
#root.wm_iconphoto(False, photo)
title_font=tk.font.Font(family="Helvetica",size=9,weight="bold")
text_font=tk.font.Font(family="Helvetica",size=9)

bg_color="#cccccc"

"/test"
def test_f():
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
            text='Show',).grid(row=3, 
                                                        column=1, 
                                                        sticky=tk.W, 
                                                        pady=4)
    master.mainloop()


" /Profile section "
def update_profile():
    pseudo=profile(str(name_entry.get()))
    if pseudo.name!="":
        frame1["text"]="  "+pseudo.name+"  "
    else:
        frame1["text"]="  Enter name  "


profile_frame=tk.LabelFrame(root,text='  Profile  ',fg="#212529",background=bg_color,font=title_font)
profile_frame.place(height=50,width=500,rely=0,relx=0)

name_label=tk.Label(profile_frame,text='Name',fg="#212529",background=bg_color,font=text_font).place(rely=0.05,relx=0.1)
name_entry=tk.Entry(profile_frame,bg="white",width=25)
name_entry.place(rely=0.05,relx=0.2)    # obligatoirement 2 lignes pour utiliser get_profile()
prof_upd_but=tk.Button(profile_frame,text="update profile",bg="#e1dee9",fg="black",command=update_profile).place(rely=0,relx=0.55)
test=tk.Button(profile_frame,text="test",command=test_f).place(rely=0,relx=0)

" /TreeView : collec_data "
frame1=tk.LabelFrame(root,text="  Enter a name  ",background=bg_color,fg="#212529",font=title_font)
frame1.place(height=250,width=500,rely=0.15,relx=0)

# Scan listing viewer
tv1=ttk.Treeview(frame1)
tv1.place(relheight=1,relwidth=1) #fill the whole container w the treeview
# Scrolling : command = quand j'active ça "update les vues"
treescrolly=tk.Scrollbar(frame1,orient="vertical",command=tv1.yview)
treescrollx=tk.Scrollbar(frame1,orient="horizontal",command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom",fill="x")
treescrolly.pack(side="right",fill="y")

" > Partie Data TreeView "



" /Scan enter "
def add_scan():
    pass

def cancel_scan():
    pass

file_frame=tk.LabelFrame(root,text="  Scan enter  ",background="#c5c3c6")
file_frame.place(height=75,width=500,rely=0.8,relx=0)
   
# En command sur les boutons on peut mettre des fonctions qu'on a codées !
#button1=tk.Button(file_frame,text="Browse a file") #needs a command
# syntaxe plus uniforme et pas besoin de 2 lignes 
button1=tk.Entry(file_frame,width=35).place(rely=0.4,relx=0)
up1=tk.Label(file_frame,text="Title",background="#c5c3c6").place(rely=0.0,relx=0)

button2=tk.Entry(file_frame,width=10).place(rely=0.4,relx=0.5)
up2=tk.Label(file_frame,text="Scan",background="#c5c3c6").place(rely=0.0,relx=0.5)

button3=tk.Entry(file_frame,width=5).place(rely=0.4,relx=0.71)
up3=tk.Label(file_frame,text="Favorite",background="#c5c3c6").place(rely=0.0,relx=0.7)

button4=tk.Button(file_frame,text="add").place(rely=0.3,relx=0.82) # command

button5=tk.Button(file_frame,text="cancel").place(rely=0.3,relx=0.9) # command

"""
button1=tk.Button(file_frame,text="Load file") #needs a command
button1.place(rely=0.65,relx=0.3)
#
label_file=ttk.Label(file_frame,text="No file selected")
label_file.place(rely=0,relx=0)
label_file["text"]="tessssst"
"""



root.mainloop()

#%%
" === Test === "
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


#%%
from tkinter import ttk
s=ttk.Style()
s.theme_names()
('clam', 'alt', 'default', 'classic')