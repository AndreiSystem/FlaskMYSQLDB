import MySQLdb

# --- Conectar com o banco de dados:
conn = MySQLdb.connect(host='mysql.topskills.study',
                       database='topskills05', user='topskills05', passwd='Andrei2019')

# --- executar a conexão:
cursor = conn.cursor()


def listar():
    # --- executar a operação no banco:
    cursor.execute('select * from pessoa')
    # --- trazer todos os dados
    lista = cursor.fetchall()
    return lista


def buscar_por_id(id):
    # --- executar o comando do busca via ID:
    cursor.execute(f'select * from pessoa where id = {id}')
    # --- trazer o dado do ID:
    item = cursor.fetchone()
    return item


def inserir(nome, sobrenome, cpf):
    # --- inserir dado na tabela:
    cursor.execute(
        f('insert into pessoa(nome, sobrenome, cpf) values("{nome}","{sobrenome}","{cpf}")')
    # --- executa o comando (commit) para a tabela:
    conn.commit()


def alterar(id, nome, sobrenome, cpf):
    # --- alterar dado de um ID específico:
    cursor.execute(
        f'update pessoa set nome = "{nome}", sobrenome = "{sobrenome}", cpf = "{cpf}" where id = {id}')
    # --- executa o comando (commit) para a tabela:
    conn.commit()


def deletar(id):
    # --- deleta a pessoa da tabela via ID:
    cursor.execute(f'delete from pessoa where id = {id}')
    # --- executa o comando (commit) para a tabela:
    conn.commit()
