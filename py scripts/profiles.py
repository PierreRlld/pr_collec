# %%
" === Dépendances === "
from data_extract import *
import pandas as pd

#%%
class work():
    def __init__(self,name,title,start=1):      # argument name pour prendre en compte une dépendance à la personne considérée cf Test
        self.title=title.capitalize()
        self.features=features(title)
        self.scan=self.features['scan']
        self.author=self.features['author']
        self.synopsis=self.features['synopsis']
        self.related=self.features['related']
        self.tags=self.features['tags']

        self.current=start                  # à quel scan on est

#%%
class profile():

    def __init__(self,name): # attribus de la classe profile 
        self.name=name
        self.collec={}      # dictionnaire qui va stocker les lectures en cours = objet de type work


    def add_collec(self,title):                             
        self.collec[title]=[work(self.name,title),False]    
# Prends en paramètre le nom d'utilisateur !!
# dictionnaire self.collec contient {nom oeuvre : [ <type work>, statut favoris] 
# on précise pas start dans work(..) on suppose qu'on commence au scan 1

    def rem_collec(self,title):
        del self.collec[title]
        return None

    def fav(self,title,action):     # définition du status de favoris
        if action=='add':
            self.collec[title][1]=True
        elif action=='del':
            self.collec[title][1]=False


    def collecTab(self):
        #keys et values : opérations sur dictionnaire (les values sont des types work)
        dic={'Title':list(self.collec.keys()), 'Current':[work[0].current for work in list(self.collec.values())], 'Favorite':[x[1] for x in list(self.collec.values())] }
        return pd.DataFrame(dic) 


    def favTab(self):
        dic={'Title':[x for x in list(self.collec.keys()) if self.collec[x][1]==True], 'Current':[work[0].current for work in list(self.collec.values()) if work[1]==True]}
        return pd.DataFrame(dic)

# ================= #

def Update(profile,title,n):    # définir à quel scan on est à partir du numéro
    profile.collec[title][0].current=n

def UpdateAdd(profile,title,step=1):    #maj scan avec un nombre de scan de lu ; base step = 1
    profile.collec[title][0].current+=step



#%%
" =========================================================== "
" ======================== TEST ============================= "
" =========================================================== "

nobu=profile('Nobu')
nobu.add_collec('One piece')
#nobu.collec['One piece'].update(10)
Update(nobu,'One piece',15)
nobu.add_collec('Naruto')
UpdateAdd(nobu,'Naruto',4)
nobu.fav('Naruto','add')

print('Favorite tab\n')
nobu.favTab()
#nobu.rem_collec('One piece')

#%%
print('Total tab\n')
nobu.collecTab()

#%%
" =========================================================== "
" ======================== OLD TEST ============================= "
" =========================================================== "
nobu.collec['Naruto'].update(35)
nobu.collecTab()
#%%
# Test class work avec dépendance au nom d'utilisateur 

op=work('Nobu','One piece')
op.update(10)
op.current

op2=work('Pierre','One piece')
op2.update(20)
op2.current

print(op.current,op2.current)
#%%
test1={'One piece':work('nobu','One piEce'),'Naruto':work('nobu','naruto')}
dftest=pd.DataFrame({'Title':list(test1.keys()), 'Current':[work.current for work in list(test1.values())] })
dftest

#%%
test2={}
test2['n1']='premier'
test2['n2é']='deux'
list(test2.keys())
