import os
import pandas as pd

def load_all_json_gz_to_dataframe(input_dir):
    """
    Lee todos los archivos .json.gz de input_dir y los concatena en un único DataFrame.
    """
    dataframes = []
    for root, _, files in os.walk(input_dir):
        for file_name in files:
            if file_name.endswith('.json.gz'):
                file_path = os.path.join(root, file_name)
                try:
                    df = pd.read_json(file_path, lines=True, compression='gzip')
                    dataframes.append(df)
                    print(f"✅ Cargado: {file_path} ({len(df)} filas)")
                except Exception as e:
                    print(f"❌ Error leyendo {file_path}: {e}")
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        print("🔢 DataFrame combinado:")
        print(combined_df.head())
        return combined_df
    else:
        print("No se encontraron archivos .json.gz.")
        return None

if __name__ == '__main__':
    input_dir = 'gharchive_data'
    load_all_json_gz_to_dataframe(input_dir)