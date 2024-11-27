import boto3
import os
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'backup-demo-bucket'

def fazer_backup(diretorio_local):
    for root, dirs, files in os.walk(diretorio_local):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            chave_s3 = f"backups/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}/{file}"
            s3.upload_file(caminho_arquivo, bucket_name, chave_s3)
            print(f"Arquivo {file} enviado para {chave_s3}")
