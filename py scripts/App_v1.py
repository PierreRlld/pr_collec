# Code App_v0.py using an object oriented approach
# https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application

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
import tkinter as tk 
from tkinter import ttk, messagebox, filedialog, font, Canvas

bg_color="#383b40" #"#cccccc"
glob_prof=""

class MainApplication:
    def __init__(self,master):  # master=tk.Tk()
        self.master=master
        self.master.geometry("600x700")
        #self.master.configure(background=bg_color)
        self.master.pack_propagate(False)
        self.master.resizable(0,0)

        self.touchbar_sec=Touch_bar(self.master)
        self.profile_sec=Profile_frame(self.master)

class Touch_bar:
    def __init__(self,master):
        bar_font=tk.font.Font(family="Helvetica",size=9)

        self.master=master
        title_font=tk.font.Font(family="Helvetica",size=9) #weight="bold"
        text_font=tk.font.Font(family="Helvetica",size=9)
        self.bar_frame=tk.Frame(self.master,bg="blue")
        self.bar_frame.place(height=45,width=600,rely=0,relx=0)

        bar_home_but=tk.Button(self.bar_frame,text="Home",fg="white",font=bar_font,bg="blue",borderwidth=0)
        bar_home_but.place(rely=0.25,relx=0.2)

        bar1=Canvas(self.bar_frame)
        bar1.create_line(15, 10, 50, 50,fill="pink")

class Profile_frame:

    def __init__(self,master):
        esppp='          '
        self.master=master
        title_font=tk.font.Font(family="Helvetica",size=9) #,weight="bold"
        text_font=tk.font.Font(family="Helvetica",size=9)
        self.profile_frame=tk.LabelFrame(self.master,text=esppp+'Welcome login please',fg="white",background=bg_color,font=title_font,borderwidth=0)
        self.profile_frame.place(height=75,width=600,rely=0.1,relx=0.0) #50

        name_label=tk.Label(self.profile_frame,text='Name',fg="white",background=bg_color,font=text_font).place(rely=0.2,relx=0.1)
        self.name_entry=tk.Entry(self.profile_frame,bg="#c9c9c9",width=25)
        self.name_entry.place(rely=0.2,relx=0.2)    # obligatoirement 2 lignes pour utiliser get_profile()
        prof_upd_but=tk.Button(self.profile_frame,text="update profile",bg="#383b40",fg="white",activebackground="#6e737a",command=self.update_profile,borderwidth=0).place(rely=0.2,relx=0.50)
        test=tk.Button(self.profile_frame,text="test").place(rely=0.2,relx=0)

    def update_profile(self):
        esppp='          '
        #profile_data=prifle(str(name_entry.get()))
        pseudo=str(self.name_entry.get())
        if pseudo!="":
            self.profile_frame["text"]=esppp+'Welcome '+pseudo
        else:
            self.profile_frame["text"]=esppp+"Not logged in"
        


#self.master.destroy()        

def main(): 
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()



#%%
" == exemple == "
import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400")
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()