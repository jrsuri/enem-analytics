import msvcrt
try:
    import requests
    import zipfile
    import os
    from tqdm import tqdm

    # Directory settings
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(base_dir, 'data')
    output_path = os.path.join(data_dir, 'microdados_enem_2022.zip')
    extract_path = os.path.join(data_dir, 'microdados_enem_2022')
    os.makedirs(data_dir, exist_ok=True)

    # Request
    url = 'https://download.inep.gov.br/microdados/microdados_enem_2022.zip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    print('Downloading microdata...')

    # Gets total file size
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))

    # Download execution
    with open(output_path, 'wb') as file, tqdm(
        desc='Download',
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            bar.update(len(chunk))
        print('Download complete!')

    print('Extracting files...')
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print('Extraction complete!')

    os.remove(output_path)
    print('Process finished. Microdata is available in the folder:', extract_path)
    print('\nPress any key to close.')
    msvcrt.getch()

except Exception as e:
    print(e)
    print('\nPress any key to close.')
    msvcrt.getch()