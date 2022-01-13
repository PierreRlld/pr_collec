# %%
from data_extract import *

#%%
class work():
    def __init__(self,title,start=1):
        self.name=title
        self.features=features(title)
        self.scan=self.features['scan']
        self.author=self.features['author']
        self.synopsis=self.features['synopsis']
        self.related=self.features['related']
        self.tags=self.features['tags']

        self.current=start                  # à quel scan on est
    
    def update(self,step=1):   #maj scan ; base step = 1
        self.current=self.current + step