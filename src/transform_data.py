"""
Módulo para transformação dos dados: tratamento de múltiplos valores em células e padronização de termos.
"""
import pandas as pd

def transform_multivalue_cells(df):
    """
    Para cada coluna, separa valores por ';', remove espaços extras, padroniza capitalização e contabiliza todas as ocorrências.
    """
    df_transformed = df.copy()
    for col in df_transformed.columns:
        # Aplica transformação apenas em colunas não numéricas
        if not pd.api.types.is_numeric_dtype(df_transformed[col]):
            df_transformed[col] = df_transformed[col].astype(str).apply(lambda cell: ';'.join([w.strip().capitalize() for w in str(cell).split(';') if w.strip() != '']))
    return df_transformed

def explode_and_count(df):
    """
    Explode as colunas para análise de frequência real dos termos por categoria.
    Retorna um dicionário de DataFrames de contagem por coluna.
    """
    freq_tables = {}
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            exploded = df[col].astype(str).str.split(';').explode().str.strip().str.capitalize()
            freq_tables[col] = exploded.value_counts().to_frame('count')
    return freq_tables
