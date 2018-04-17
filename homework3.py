
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import os
import sqlite3


# In[12]:


def create_dataframe(filepath):
    
    if not os.path.exists(filepath):
        raise ValueError()
        
    cnxn = sqlite3.connect(filepath)
    
    us = pd.read_sql_query("select * from USVideos", cnxn)
    us["language"] = "us"

    gb = pd.read_sql_query("select * from GBVideos", cnxn)
    gb["language"] = "gb"

    fr = pd.read_sql_query("select * from FRVideos", cnxn)
    fr["language"] = "fr"

    de = pd.read_sql_query("select * from DEVideos", cnxn)
    de["language"] = "de"

    ca = pd.read_sql_query("select * from CAVideos", cnxn)
    ca["language"] = "ca"

    final_table = pd.concat([us, gb, fr, de, ca], axis=0)[["category_id", "video_id", "language"]]
    
    return final_table
    


# In[26]:


def test_create_dataframe(df):
    def _testCols():
        if df.shape[1]==3:
            return ["video_id", "category_id", "language"] in df.columns.values
        else:
            return False
    
    def _testKeys():
        n = max(df.drop_duplicates().groupby(["video_id", "category_id"]).size())
        return n == 1
    def _numRows():
        return df.shape[0] > 9
    
    return _numRows() and _testCols() and _testKeys()

