"""Módulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os
from typing import List

import pandas as pd

path = "data/input"


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler e extrair os arquivos em Excel

    type: input_folder: str (caminho da pasta).
    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data = pd.read_excel(file)
        data_frame_list.append(data)

    return data_frame_list


if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
