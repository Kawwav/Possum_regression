import os
import pandas as pd
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi


os.environ['KAGGLE_USERNAME'] = "vinikawwa"
os.environ['KAGGLE_KEY'] = "548dbb9c523da36ad8226a9218bcbeb6"


try:
    api = KaggleApi()
    api.authenticate()
    print("✅ Autenticação bem-sucedida!")

    
    dataset_ref = 'mateus558/brazilian-legal-amazon-burned-area-dataset'
    path_destino = './dados'

    
    os.makedirs(path_destino, exist_ok=True)

    api.dataset_download_files(dataset_ref, path=path_destino, unzip=True)
    print(f"📥 Dataset '{dataset_ref}' baixado e extraído com sucesso em '{path_destino}'!")

except Exception as e:
    print(f"❌ Erro ao autenticar ou baixar o dataset: {e}")

    !pip install kaggle

import os


for arquivo in os.listdir('./dados'):
    print(arquivo)



df = pd.read_csv('./dados/Burned_Area_1999_2019.csv')
df.head()
df.columns
