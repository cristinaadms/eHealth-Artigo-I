"""
Módulo para normalização de colunas numéricas.
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def identify_numeric_columns(df):
    """
    Identifica colunas numéricas (exclui binárias 0/1 e categóricas).
    """
    numeric_cols = []
    for col in df.columns:
        try:
            vals = pd.to_numeric(df[col], errors='coerce')
            unique_vals = set(vals.dropna().unique())
            if unique_vals.issubset({0, 1}):
                continue  # binária
            if vals.notna().sum() > 0 and len(unique_vals) > 2:
                numeric_cols.append(col)
        except Exception:
            continue
    return numeric_cols

def normalize_columns(df, method='minmax'):
    """
    Normaliza colunas numéricas usando Min-Max ou Z-score.
    """
    df_norm = df.copy()
    numeric_cols = identify_numeric_columns(df_norm)
    if not numeric_cols:
        return df_norm
    if method == 'minmax':
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df_norm[numeric_cols] = scaler.fit_transform(df_norm[numeric_cols].astype(float))
    return df_norm
