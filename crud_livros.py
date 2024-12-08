import psycopg2

class Livros:
    def __init__(self, id_livro, nome_livro, autor, num_paginas, ano_lancamento, editora):
        self.id_livro = id_livro
        self.nome = nome_livro
        self.autor = autor
        self.paginas = num_paginas
        self.lancamento = ano_lancamento
        self.editora = editora

class CrudLivros:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = psycopg2.connect(
            database=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port='5432'
        )

    def create_table(self):
        query = '''
            CREATE TABLE public.livro(
                id_livro INTEGER, 
                nome_livro VARCHAR, 
                autor VARCHAR, 
                num_paginas INTEGER,
                ano_lancamento INTEGER, 
                editora VARCHAR
            );
        '''

        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def insert(self, livro):
        query = f'''
            INSERT INTO public.livro(
                id_livro, 
                nome_livro, 
                autor, 
                num_paginas, 
                ano_lancamento, 
                editora
            )
            VALUES(
                {livro.id_livro},
                '{livro.nome}',
               '{livro.autor}',
                {livro.paginas},
                {livro.lancamento},
                '{livro.editora}'
            );
        '''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def read_all(self):
        query = '''
            SELECT *
            FROM public.livro
        '''

        cur = self.conn.cursor()
        cur.execute(query)

        return cur.fetchall()

    def read_by_id(self, id_livro):
        query = f'''
                   SELECT *
                   FROM public.livro
                   WHERE id_livro = {id_livro}
               '''

        cur = self.conn.cursor()
        cur.execute(query)

        return cur.fetchall()


    def update(self, livro):
        pass

    def delete(self, livro):
        pass


crud = CrudLivros(
    dbname='postgres',
    user='jessica',
    password='DoL&Fl0r2410',
    host='localhost'
)

# crud.create_table()
sda = Livros(
    id_livro = 1,
    nome_livro = "Senhor dos Anéis - As Duas Torres",
    autor = "Tolkien",
    num_paginas = 1000,
    ano_lancamento = 1945,
    editora = "Rocco"
)

hp = Livros(
    id_livro = 2,
    nome_livro = "Harry POtter - A Pedra Filosofal ",
    autor = "J.K. Rolling",
    num_paginas = 350,
    ano_lancamento = 1997,
    editora = "Intríseca"
)
# crud.insert(hp)

crud.read_by_id(2)