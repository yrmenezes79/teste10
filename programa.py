import mysql.connector

# Defina as informações de conexão
host = 'localhost'  # Endereço do servidor MySQL
usuario = 'impacta'  # Nome de usuário do MySQL
senha = '123impacta'  # Senha do MySQL
banco_de_dados = 'seu_banco_de_dados'  # Nome do banco de dados a ser acessado

try:
    # Crie uma conexão com o banco de dados
    conexao = mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=banco_de_dados
    )

    if conexao.is_connected():
        print("Conexão bem-sucedida!")
        # Faça operações no banco de dados aqui, se necessário

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ao banco de dados: {erro}")

finally:
    # Certifique-se de fechar a conexão, independentemente de ter sido bem-sucedida ou não
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")
