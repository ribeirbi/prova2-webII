# Controller da API - as rotas daqui respondem DADOS em JSON.
#
#   Metodo   Endereco                 O que faz       Sucesso   Recusas
#   GET      /api/palestrantes            lista todos     200       401
#   GET      /api/palestrantes/<id>       devolve um      200       401 404   <- ITEM 7
#   DELETE   /api/palestrantes/<id>       remove          204       401 404   <- ITEM 9
#
# Toda recusa tem o mesmo formato: {"erro": "mensagem"}.

from flask import Blueprint, request, session, jsonify
from models.palestrante import Palestrante
from dao.palestrante_dao import PalestranteDAO

api_bp = Blueprint("api", __name__, url_prefix="/api")



@api_bp.before_request
def exigir_login():
    if not session.get("usuario_id"):
        return jsonify({"erro": "Autenticacao necessaria."}), 401


@api_bp.route("/palestrantes", methods=["GET"])
def listar():
    lista = []

    for palestrante in PalestranteDAO.listar():
        lista.append(palestrante.para_dicionario())

    return jsonify(lista)

@api_bp.route("/palestrantes/<int:id>", methods=["GET"])
def buscar(id):
    palestrante = PalestranteDAO.buscar_por_id(id)

    if not palestrante:
        return jsonify({
            "erro": "Palestrante nao encontrado."
        }), 404


@api_bp.route("/palestrantes/<int:id>", methods=["DELETE"])
def excluir_api(id):
    palestrante = PalestranteDAO.buscar_por_id(id)

    if not palestrante:
        return jsonify({
            "erro": "Palestrante nao encontrado."
        }), 404

    PalestranteDAO.excluir(palestrante)
    return "", 204