import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = os.getenv("STRING_CONNECTION")

conn = pyodbc.connect(conn_str)

query = f"SELECT nome,foto FROM funcionario WHERE ativo = 1"

cursor = conn.cursor()
cursor.execute(query)
funcionarios = cursor.fetchall()

for funcionario in funcionarios:
    if funcionario.foto is not None:
        image_data = funcionario.foto
        
        caminho_imagem = os.path.join(os.getcwd(),"Fotos\\" + funcionario.nome + ".jpg")
        
        with open(caminho_imagem, 'wb') as foto:
            foto.write(image_data)
        print("Imagem salva com sucesso em:", caminho_imagem)
    else:
        print("Nenhuma imagem encontrada para a pessoa", funcionario.nome)
conn.close()