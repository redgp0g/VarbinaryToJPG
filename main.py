import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = os.getenv("STRING_CONNECTION")

conn = pyodbc.connect(conn_str)

query = """
SELECT DISTINCT F.IDFuncionario, F.nome, F.foto 
FROM Funcionario AS F 
"""

cursor = conn.cursor()
cursor.execute(query)

funcionarios = cursor.fetchall()

# Abre (ou cria) o arquivo txt para registrar nomes e IDs de quem não tem foto
with open("funcionarios_sem_foto.txt", 'w', encoding='utf-8') as txt_file:
    for funcionario in funcionarios:
        if funcionario.foto is not None:
            image_data = funcionario.foto
            
            image_path = os.path.join(os.getcwd(), "Fotos", f"{funcionario.nome}.jpg")

            with open(image_path, 'wb') as foto_file:
                foto_file.write(image_data)
            print("Imagem salva com sucesso em:", image_path)
        else:
            txt_file.write(f"ID: {funcionario.IDFuncionario}, Nome: {funcionario.nome}\n")
            print(f"Nenhuma imagem encontrada para a pessoa {funcionario.nome}")
conn.close()