# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************
from typing import Tuple

from app import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Autores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    especialidade = db.Column(db.String(50))

    def criar(self):
        db.session.add(self)
        return self

    def __init__(self, _nome: str, _especialidade: Tuple[str]):
        self.nome = _nome
        self.especialidade = _especialidade

    def __repr__(self):
        return f'<Autor {self.id}>'


class AutorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        modelo = Autores
        sqla_sessao = db.session

    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)
    especialidade = fields.String(required=True)


db.create_all()
