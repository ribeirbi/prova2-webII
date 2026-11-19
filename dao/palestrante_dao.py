# DAO - concentra o acesso aos dados de Palestrante.

from extensions import db
from models.palestrante import Palestrante


class PalestranteDAO:

    # CREATE
    @staticmethod
    def salvar(palestrante):
        db.session.add(palestrante)

    # READ (todos)
    @staticmethod
    def listar():
        return Palestrante.query.all()

    # READ (um) - devolve o objeto ou None
    @staticmethod
    def buscar_por_id(id):
        return Palestrante.query.get(id)

    # UPDATE
    @staticmethod
    def atualizar(palestrante, nome, tema, minutos):
        palestrante.nome = nome
        palestrante.tema = tema
        palestrante.minutos = minutos
        db.session.commit()

    # DELETE
    @staticmethod
    def excluir(palestrante):
        db.session.delete(palestrante)
        db.session.commit()
