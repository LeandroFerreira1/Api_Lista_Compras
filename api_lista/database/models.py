from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    senha = Column(String)
    listas = relationship('Lista', backref='usuario', lazy='subquery')

class Lista(Base):
    __tablename__= 'lista'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    itens = relationship('Item', backref='lista', lazy='subquery')

class Item(Base):
    __tablename__= 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String)
    quantidade = Column(Integer)
    preco = Column(String)
    lista_id = Column(Integer, ForeignKey('lista.id'))
