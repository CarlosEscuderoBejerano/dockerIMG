from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.modelo.usuario import Usuario
from app.data.userDao import UserDao
from app.data.personajeDao import PersonajeDao
from app.data.armaDao import ArmaDao
import os

bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
    personaje_services = PersonajeDao(db.session)
    arma_services = ArmaDao(db.session)
    return render_template("index.html", personaje=personaje_services.get_all(), 
    arma=arma_services.get_all())

@bp.route("/add_user", methods=['Get','POST'])
def add_user():
    nombre: str = request.form.get("nombre", default="No Nombre", type=str)
    personajeMasUtilizado: str = int(request.form.get("n_personaje", default="5", type=str))
    armaMasUtilizada: str = int(request.form.get("n_arma", default="18", type=str))
    user_services = UserDao(db.session)
    usuario = Usuario(nombre=nombre, personaje_mas_utilizado = personajeMasUtilizado  ,
           arma_mas_utilizada = armaMasUtilizada)
    usuario=user_services.add_user(usuario)
    return redirect("usuarios")


    

@bp.route("/personajes")
def personajes():
    personaje_services = PersonajeDao(db.session)
    return render_template("personajes.html", personaje=personaje_services.get_all())

@bp.route("/armas")
def armas():
    arma_services = ArmaDao(db.session)
    return render_template("armas.html", arma=arma_services.get_all())

@bp.route("/usuarios")
def usuarios():
    user_services = UserDao(db.session)
    return render_template("usuarios.html", usuarios=user_services.get_all())
