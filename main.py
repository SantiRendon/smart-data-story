import load_to_minio, extract_gh_archives

if __name__ == "__main__":
    extract_gh_archives.download_gharchive_data(
        start_date=datetime(2025, 1, 1),
        end_date=datetime(2025, 1, 2),
        download_dir="gharchive_data",
    )
    load_to_minio.load_to_minio(
        download_dir="gharchive_data",
        minio_client=minio_client,
    )
