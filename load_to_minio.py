from minio import Minio
import os

def load_to_minio(download_dir: str, minio_client: Minio, bucket_name: str = "gh-archive"):
    """
    Upload files from a specified directory to a MinIO bucket.

    Args:
        download_dir (str): Directory containing files to upload
        minio_client (Minio): MinIO client for uploading files
        bucket_name (str, optional): Name of the MinIO bucket. Defaults to 'gh-archive'.
    """
    # Create the bucket if it doesn't exist
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
        print(f"✅ Bucket '{bucket_name}' creado")
    else:
        print(f"📦 Bucket '{bucket_name}' ya existe")

    # Upload all .json.gz files
    for root, _, files in os.walk(download_dir):
        for file_name in files:
            if file_name.endswith(".json.gz"):
                local_path = os.path.join(root, file_name)
                object_name = os.path.relpath(local_path, download_dir)
                try:
                    minio_client.fput_object(bucket_name, object_name, local_path)
                    print(f"⬆️  Subido: {object_name}")
                except Exception as e:
                    print(f"❌ Error subiendo {object_name}: {e}")

# Example usage if script is run directly
if __name__ == '__main__':
    # Create a default MinIO client
    client = Minio(
        "localhost:9000",
        access_key="admin",
        secret_key="admin123",
        secure=False
    )
    
    # Default upload directory
    default_download_dir = "data"
    
    # Load files to MinIO
    load_to_minio(
        download_dir=default_download_dir, 
        minio_client=client
    )
