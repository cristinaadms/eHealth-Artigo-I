"""
Módulo para limpeza dos dados: remoção de linhas e tratamento de valores ausentes.
"""
import pandas as pd
import numpy as np

def clean_data(df):
    """
    Remove as 5 primeiras linhas e trata valores ausentes e "X".
    """
    # Remove as 5 primeiras linhas
    df = df.iloc[5:].reset_index(drop=True)
    # Define a primeira linha como header
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)
    # Substitui valores vazios, nulos ou células em branco por 0
    df = df.replace({np.nan: 0, "": 0, None: 0})
    df = df.map(lambda x: 0 if str(x).strip() == "" else x)
    # Substitui "X" por 1
    df = df.replace("X", 1)
    return df
