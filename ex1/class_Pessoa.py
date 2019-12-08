import MySQLdb


class Person_DB:

    def __init__(self, name=None, last_name=None, cpf=None, id=None):
        self.name = name
        self.last_name = last_name
        self.cpf = cpf
        self.id = id

        self.connection = MySQLdb.connect(
            host='mysql.topskills.study', database='topskills05', user='topskills05', passwd='Andrei2019')

        self.cursor = self.connection.cursor()

    def register(self, name, last_name, cpf):
        self.cursor.execute(
            f'insert into pessoa(nome, sobrenome, cpf) values("{name}","{last_name}","{cpf}")')
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute(f'delete from pessoa where id = {id}')
        self.connection.commit()

    def changedata_for_id(self, id):
        self.cursor.execute(
            f'update pessoa set nome = "{self.name}", sobrenome = "{self.last_name}", cpf = "{self.cpf}" where id = {id}')
        self.connection.commit()

    def search_for_id(self, id):
        id_list = []
        self.cursor.execute(f'select * from pessoa where id = {id}')
        pessoa = self.cursor.fetchone()
        return pessoa

    def get_to_list(self):

        self.cursor.execute(f'select * from pessoa')
        list_person = self.cursor.fetchall()
        return list_person
