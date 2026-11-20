# Controller de PAGINAS - todas as rotas daqui respondem HTML ou
# redirecionamento.

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session
from models.palestrante import Palestrante
from dao.palestrante_dao import PalestranteDAO

palestrante_bp = Blueprint("palestrante", __name__)

@palestrante_bp.before_request
def proteger_paginas():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))


# ===== ITEM 5 ========================================================
# Hoje qualquer pessoa abre as paginas deste Blueprint sem entrar no
# sistema. Escreva aqui a protecao, em um ponto so.
# =====================================================================


# Listagem (GET) e cadastro (POST) na mesma rota
@palestrante_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        palestrante = Palestrante(
            nome=request.form["nome"],
            tema=request.form["tema"],
            minutos=request.form["minutos"]
        )
        PalestranteDAO.salvar(palestrante)
        flash("Palestrante cadastrado.")
        return redirect(url_for("palestrante.index")) 

    session["visitas"] = session.get("visitas", 0) + 1


    return render_template("index.html", palestrantes=PalestranteDAO.listar())


# Edicao - GET mostra o formulario preenchido
@palestrante_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    palestrante = PalestranteDAO.buscar_por_id(id)
    if request.method == "POST":
        PalestranteDAO.atualizar(
            palestrante,
            nome=request.form["nome"],
            tema=request.form["tema"],
            minutos=request.form["minutos"]
        )
        PalestranteDAO.atualizar(palestrante, request.form["nome"], request.form["tema"], request.form["minutos"])
        flash("Palestrante atualizado.")
        return redirect(url_for("palestrante.index"))

    return render_template("editar.html", palestrante=palestrante)


# Exclusao
@palestrante_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    palestrante = PalestranteDAO.buscar_por_id(id)
    PalestranteDAO.excluir(palestrante)
    flash("Palestrante excluido.")
    return redirect(url_for("palestrante.index"))
