"""
Módulo para carregamento e inspeção inicial dos dados.
"""
import pandas as pd

def load_and_inspect(filepath):
    """
    Carrega o dataset e exibe informações iniciais.
    """
    df = pd.read_csv(filepath, header=None, dtype=str, keep_default_na=False)
    print("Shape:", df.shape)
    print("Head:")
    print(df.head())
    print("Info:")
    print(df.info())
    return df
