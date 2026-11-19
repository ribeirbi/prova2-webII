# Model - entidade Palestrante.

from extensions import db


class Palestrante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    tema = db.Column(db.String(120))
    minutos = db.Column(db.Integer)

    # O objeto se descreve como dicionario, para as rotas que respondem JSON.
    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tema": self.tema,
            "minutos": self.minutos
        }
