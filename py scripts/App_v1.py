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

        self.profile_sec=Profile_frame(self.master)
        self.touchbar_sec=Touch_bar(self.master,self.profile_sec)
        

class Touch_bar:
    def __init__(self,master,pro_frame_bar):
        bar_font=tk.font.Font(family="Helvetica",size=9)
        self.colorbar="#5c4d7d"
        self.master=master
        self.pro_frame_bar=pro_frame_bar
        title_font=tk.font.Font(family="Helvetica",size=9)      #weight="bold"
        text_font=tk.font.Font(family="Helvetica",size=9)
        self.bar_frame=tk.Frame(self.master,bg=self.colorbar)
        self.bar_frame.place(height=45,width=600,rely=0,relx=0)

        #> home
        bar_home_but=tk.Button(self.bar_frame,text="Home",fg="white",font=bar_font,bg=self.colorbar,borderwidth=0)
        bar_home_but.place(rely=0.25,relx=0.2)

        bar1=Canvas(self.bar_frame,width=30,height=40,bg=self.colorbar,highlightthickness=0)
        bar1.create_line(5, 10, 5, 35,fill="white")
        bar1.place(rely=0,relx=0.3)
        #> favorites
        bar_fav_but=tk.Button(self.bar_frame,text="Favorites",fg="white",font=bar_font,bg=self.colorbar,borderwidth=0,command=self.favorites)
        bar_fav_but.place(rely=0.25,relx=0.37)

        bar2=Canvas(self.bar_frame,width=30,height=40,bg=self.colorbar,highlightthickness=0)
        bar2.create_line(5, 10, 5, 35,fill="white")
        bar2.place(rely=0,relx=0.5)
        #> log out
        bar_out_but=tk.Button(self.bar_frame,text="Log out",fg="white",font=bar_font,bg=self.colorbar,borderwidth=0,command=self.logout)
        bar_out_but.place(rely=0.25,relx=0.57)
        #> exit
        bar_exit_but=tk.Button(self.bar_frame,text="exit",fg="white",font=bar_font,bg=self.colorbar,borderwidth=0,command=self.exit)
        bar_exit_but.place(rely=0.25,relx=0.92)

    def logout(self):
        self.pro_frame_bar.profile_frame["text"]="          Logged out"

    def exit(self):
        self.master.destroy()
    
    def favorites(self):
        self.fav_inter=tk.Tk()
        self.favorite_page=Favorite_page(self.fav_inter)


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

    def update_profile(self):
        esppp='          '
        #profile_data=prifle(str(name_entry.get()))
        pseudo=str(self.name_entry.get())
        if pseudo!="":
            self.profile_frame["text"]=esppp+'Welcome '+pseudo
        elif pseudo=="kill":
            self.master.destroy()
        else:
            self.profile_frame["text"]=esppp+"Not logged in"

class Scan_frame:
    pass


class Favorite_page:                    # on redéfinie une page à la manière de la page de base
    def __init__(self, master):
        #title_font=tk.font.Font(family="Helvetica")
        self.master = master
        self.master.geometry("300x200")
        self.master.configure(background=bg_color)
        self.frame1 = tk.LabelFrame(self.master, text="           Favorites",fg="white",background=bg_color,borderwidth=0)
        self.frame1.place(height=25,width=300)


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