
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd


# In[16]:


import unittest
import homework3 as hw3


# In[40]:


class test_create_dataframe(unittest.TestCase):
    
    def setUp(self):
        
        self.df         = hw3.create_dataframe("class.db")
        self.n, self.d  = self.df.shape
        self.colnames   = self.df.columns
    
    def test_col_names(self):
        self.assertEqual(self.d, 3)
        self.assertTrue(all(self.colnames.isin(["category_id", "video_id", "language"])))
        
        
    def test_num_rows(self):
        self.assertEqual(self.n, 75005)
                        
    def test_keys(self):
        n1 = max(self.df.drop_duplicates().groupby(["video_id", "category_id"]).size())
        n2 = max(self.df.drop_duplicates().groupby(["video_id"]).size())
        n3 = max(self.df.drop_duplicates().groupby(["category_id"]).size())
        n4 = max(self.df.drop_duplicates().groupby(["video_id", "category_id", "language"]).size())

        self.assertFalse(n1==1 or n2==1 or n3==1)
        self.assertTrue(n4==1)
        
    def test_error(self):
        with self.assertRaises(ValueError):
            hw3.create_dataframe("fakepath")

if __name__ == '__main__':
    unittest.main()

