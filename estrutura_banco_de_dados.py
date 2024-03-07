from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar um API flask
app = Flask(__name__)
# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'dfEo38jO09nNGO#9B@d920n'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db: SQLAlchemy

# Definir a estrutura da tabela Postagem
# id_postagem, título, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    # ForeignKey serve para ligar uma tabela com outra
    # Nesse caso, cada postagem PRECISA ter um autor
    # Autor esse que é vinculado pelo id_autor
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))


# Definir a estrutura da tabela Autor
# id_autor, nome, email, senha, admin, postagens  
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    # Aqui está formando a relação do outro lado
    postagens = db.relationship('Postagem')


def initialize_bank():
    with app.app_context():
        #executar o comando para criar o banco de dados
        db.drop_all()
        db.create_all()
        # Criar usuários administradores
        autor = Autor(nome='victor', email='victordonizete65@gmail.com', senha='12345', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    initialize_bank()
