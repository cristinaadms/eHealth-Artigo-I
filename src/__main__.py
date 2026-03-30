"""
Script principal para pré-processamento da base filter03.csv
"""
import os
from load_data import load_and_inspect
from clean_data import clean_data
from transform_data import transform_multivalue_cells
from normalize_data import normalize_columns
import pandas as pd

def main():
    data_path = os.path.join('..', 'data', 'filter03.csv')
    output_path = os.path.join('..', 'data', 'data_processed.csv')
    # 1. Carregamento e inspeção
    df = load_and_inspect(data_path)
    # 2. Limpeza
    df = clean_data(df)
    # 3. Transformação
    df = transform_multivalue_cells(df)
    # 4. Normalização
    df = normalize_columns(df, method='minmax')
    # 5. Exportação
    df.to_csv(output_path, index=False)
    print(f"Arquivo processado salvo em: {output_path}")

if __name__ == "__main__":
    main()
