import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi


os.environ['KAGGLE_USERNAME'] = "vinikawwa"
os.environ['KAGGLE_KEY'] = "4ba26a0180c25ddedde09cf7b9013057"

try:
    
    api = KaggleApi()
    api.authenticate()
    print("✅ Autenticação bem-sucedida!")

    dataset_ref = 'abrambeyer/openintro-possum'
    path_destino = 'openintro-possum'
    os.makedirs(path_destino, exist_ok=True)

    api.dataset_download_files(dataset_ref, path=path_destino, unzip=True)
    print(f"📥 Dataset '{dataset_ref}' baixado e extraído com sucesso em '{path_destino}'!")

    print("📄 Arquivos disponíveis:")
    for arquivo in os.listdir(path_destino):
        print("-", arquivo)

    caminho_arquivo = os.path.join(path_destino, 'possum.csv')
    df = pd.read_csv(caminho_arquivo)

  
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    print("\n📊 Primeiras linhas da tabela:")
    print(df.head())

 
    plt.figure(figsize=(10, 6))
    sns.histplot(df['hdlngth'].dropna(), kde=True, bins=20, color='skyblue')
    plt.title('Distribuição do Comprimento da Cabeça (hdlngth)')
    plt.xlabel('Comprimento da Cabeça')
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(8, 5))
    sns.countplot(x='sex', data=df, palette='pastel')
    plt.title('Contagem de Possums por Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"❌ Erro ao autenticar ou baixar o dataset: {e}")
print("\n🧩 Colunas disponíveis no DataFrame:")
print(df.columns.tolist())
sns.histplot(df['head_length'].dropna(), kde=True, bins=20, color='skyblue')
sns.histplot(df['<nome_da_coluna_correto>'].dropna(), kde=True, bins=20, color='skyblue')
