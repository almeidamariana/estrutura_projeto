"""Módulo com todas as transformações necessárias para consolidar os dados de entrada."""
from typing import List

import pandas as pd


def contact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de dataframes em um único dataframe.
    """
    return pd.concat(data_frame_list, ignore_index=True)
