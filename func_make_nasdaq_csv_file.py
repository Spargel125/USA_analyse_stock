#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from tqdm import tqdm
import os


# In[3]:


def get_stock(folderpath):
    """
        folderpathはフォルダーを作成する場所．
        symbol/symbol.csvの形で指定
    """
    symbols = get_nasdaq_symbols()
    #data = {}
    error_symbols = []
    i = 0
    for s in tqdm(symbols.index):
#         if i <= 3600:
#             i = i+1
#             continue
        try:
            os.mkdir('../USA_Stock/'+str(s))
            data = web.DataReader(s,"yahoo")
            data.to_csv('../USA_Stock/'+s+'/'+s+'.csv')
        except:
            error_symbols.append(s)
#         i = i+1


# In[4]:


def add_stock(folderpath):
    """
    folderpathはフォルダーを作成する場所．
    symbol/symbol.csvの形で指定
    """
    print(folderpath)
    return 0


# In[ ]:




