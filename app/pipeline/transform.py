import pandas as pd
from typing import List 

"""
função para transformar uma lista de dataframes em um único dataframe
"""

def contact_data_frames(df_list: List(pd.DataFrame)):
    return pd.concat(df_list, ignore_index=True)