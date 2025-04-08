import os
import pandas as pd
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi



os.environ['KAGGLE_USERNAME'] = "vinikawwa"
os.environ['KAGGLE_KEY'] = "4ba26a0180c25ddedde09cf7b9013057"


try:
    api = KaggleApi()
    api.authenticate()
    print("✅ Autenticação bem-sucedida!")

    
    dataset_ref = 'swarnendud/data-analysis-on-amazon-forest-fires'
    path_destino = 'amazon.csv'


    
    os.makedirs(path_destino, exist_ok=True)

    api.dataset_download_files(dataset_ref, path=path_destino, unzip=True)
    print(f"📥 Dataset '{dataset_ref}' baixado e extraído com sucesso em '{path_destino}'!")

except Exception as e:
    print(f"❌ Erro ao autenticar ou baixar o dataset: {e}")


import os


for arquivo in os.listdir('amazon.csv'):
    print(arquivo)





