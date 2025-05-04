import os
import gzip
import shutil

def unzip_json_gz_files(input_dir, output_dir):
    """
    Descomprime todos los archivos .json.gz de input_dir y los guarda en output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ Carpeta de salida creada: {output_dir}")

    for root, _, files in os.walk(input_dir):
        for file_name in files:
            if file_name.endswith('.json.gz'):
                input_path = os.path.join(root, file_name)
                # Mantener la estructura de carpetas relativa
                rel_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, rel_path)
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)
                output_file = os.path.join(output_subdir, file_name[:-3])  # Quita el .gz
                try:
                    with gzip.open(input_path, 'rb') as f_in, open(output_file, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    print(f"🟢 Descomprimido: {input_path} -> {output_file}")
                except Exception as e:
                    print(f"❌ Error descomprimiendo {input_path}: {e}")

if __name__ == '__main__':
    input_dir = 'gharchive_data'
    output_dir = 'unzipped'
    unzip_json_gz_files(input_dir, output_dir)