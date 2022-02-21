# %%
" === Dépendances === "
import urllib
import bs4
import pandas as pd
from urllib import request
import re
from urllib.request import Request, urlopen
import string
hdr={'User-agent':'Mozilla/5.0'}           # erreur : https://stackoverflow.com/questions/13055208/httperror-http-error-403-forbidden

# %%
" === Scraping === "

def nb_pages():
    base_url="https://www.anime-planet.com/manga/all?page=1"
    base_request=urlopen(Request(base_url,headers=hdr))
    base_page = bs4.BeautifulSoup(base_request, "lxml") #qui est bien une page html maintenant 
    
    maxpage=0
    page=base_page.find('ul',{"class":"nav"}).findAll('li')

    for li in page:
        try:
            p=int(li.find('a').text)
            maxpage=max(p,maxpage)
        except:
            pass
    return maxpage

def mangas_page(n):

    base_url="https://www.anime-planet.com/manga/all?page="                         
    base_request=urlopen(Request(base_url+str(n),headers=hdr))
    base_page = bs4.BeautifulSoup(base_request, "lxml")  

    mangas_list=[]
    base_layer=base_page.find('ul',{"class":"cardDeck cardGrid"})   #on cherche 'ul' dont la classe est 'cardDeck cardGrid'
    m_list_base=base_layer.findAll('li',{'data-type':"manga"})

    for li in m_list_base:
        mangas_list.append(li.find('h3').text)
    return mangas_list

# %%
" === Features extraction === "
def basepage(title):
    title=title.replace(' ','-')
    base_url="https://www.anime-planet.com/manga/"
    base_request=urlopen(Request(base_url+str(title),headers=hdr))
    base_page = bs4.BeautifulSoup(base_request, "lxml")  
    return base_page

def TextURL(text):
    if "’s" in text:
        text=text.replace("’s",'s')
    if ' - ' in text:
        text=text.replace(' - ','-')
    for punc in string.punctuation:
        if punc !='-':
            text=text.replace(punc,'')
    text=text.replace(' ','-')
    return text

# ================================================== #

def features(title):
    base_page=basepage(title)
    feat={}

    feat['title']=title
    feat['scan']=base_page.find('div',{"class":"pure-1 md-1-5"}).text.split(';')[-1].replace('\n','').replace('Ch: ','').replace('+','').replace(' ','')
    
    # Synopsis
    try:
        feat['synopsis']=base_page.find('div',{"class":'synopsisManga'}).text
    except:
        feat['synopsis']=None

    # Author
    try:    
        staff=base_page.find('section',{'class':'EntryPage__content__section EntryPage__content__section__staff castaff'})
        feat['author']=staff.find('strong',{'class':'CharacterCard__title rounded-card__title'}).text   # auteur toujours en 1er dans le staff
    except:
        feat['author']=None

    # Related
    try:
        related=base_page.find('div',{'id':'tabs--relations--manga'})
        feat['related']=related.find('p').text
    except:
        feat['related']=None

    # Tags
    try:
        tags=base_page.find('div',{'class':'tags'}).findAll('a')
        feat['tags']=[tag.text.replace("\n",'') for tag in tags]
    except:
        feat['tags']=None

    return feat

# %%
""""
testpage=basepage('Ooh La La')
print(testpage.find('div',{"class":"pure-1 md-1-5"}).text.split(';')[-1])
"""

# %%
" === Création CSV === "
featuresList=['Title','Scan','Synopsis','Author','Related','Tags']
df=pd.DataFrame(data=[],columns=featuresList)
#df
dataL=[]

" Test d'erreur "
c=0
erreur=[]
t1=mangas_page(5)
for el in t1:
    try:
        a=list(features(TextURL(el)).values())
    except:
        erreur.append(el)
erreur

#%% 

#TextURL('Get Out of My House!')
features(TextURL('Naruto'))