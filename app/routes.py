# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************

from app import app, render_template, request, make_response, jsonify
from app.models import Autores, AutorSchema


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/autores', methods=['GET'])
def autor():
    get_autores = Autores.query.all()
    autor_schema = AutorSchema(many=True)
    autores, erro = autor_schema.dump(get_autores)
    resposta = make_response(jsonify(autores=autores))
    return resposta


@app.route('/autores', methods=['POST'])
def criar_autor():
    dados = request.get_json()
    autor_schema = AutorSchema()
    autores, erro = autor_schema.load(dados)
    resultado = autor_schema.dump(autores.criar()).data
    resposta = make_response(jsonify(autores=autores))
    return resposta
