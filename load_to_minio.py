from minio import Minio
import os

# Configura el cliente de MinIO
client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

# Nombre del bucket
bucket_name = "gh-archive"

# Crea el bucket si no existe
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
    print(f"✅ Bucket '{bucket_name}' creado")
else:
    print(f"📦 Bucket '{bucket_name}' ya existe")

# Carpeta con los archivos a subir
local_folder = "data"

# Sube todos los archivos .json.gz
for root, _, files in os.walk(local_folder):
    for file_name in files:
        if file_name.endswith(".json.gz"):
            local_path = os.path.join(root, file_name)
            object_name = os.path.relpath(local_path, local_folder)
            try:
                client.fput_object(bucket_name, object_name, local_path)
                print(f"⬆️  Subido: {object_name}")
            except Exception as e:
                print(f"❌ Error subiendo {object_name}: {e}")
