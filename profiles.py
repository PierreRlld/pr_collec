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
    
    def update(self,step=1):   #maj scan ; base step = 1
        self.current=self.current + step

#%%
class profile():

    def __init__(self,name): 
        self.name=name
        self.collec={}      # dictionnaire qui va stocker les lectures en cours + objet de type work
    
    def add_collec(self,title):
        self.collec[title]=work(self.name,title)

    def rem_collec(self,title):
        del self.collec[title]
        return None
    
    def collecTab(self):
        #keys et values : opérations sur dictionnaire (les values sont des types work)
        return pd.DataFrame({'Title':list(self.collec.keys()),'Current':[work.current for work in list(self.collec.values())]}) 


#%%
nobu=profile('Nobu')
nobu.add_collec('One piece')
nobu.collec['One piece'].update(10)
nobu.add_collec('Naruto')
nobu.rem_collec('One piece')
nobu.collecTab()
#%%
" =========================================================== "
" ======================== TEST ============================= "
" =========================================================== "

#%%
# Test class work avec dépendance au nom d'utilisateur 

op=work('Nobu','One piece')
op.update(10)
op.current

op2=work('pp','One piece')
op2.update(20)
op2.current

test=[op,op2]
#%%
test1={'One piece':work('nobu','One piEce'),'Naruto':work('nobu','naruto')}
dftest=pd.DataFrame({'Title':list(test1.keys()), 'Current':[work.current for work in list(test1.values())] })
dftest

#%%
test2={}
test2['n1']='premier'
test2['n2é']='deux'
list(test2.keys())
