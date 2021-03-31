# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************

from app import *
from app.models import Autores, AutorSchema

apigc = Blueprint('apigc', __name__)


@apigc.route('/')
@apigc.route('/index')
def index():
    return render_template("index.html")


@apigc.route('/autores', methods=['GET'])
def autor():
    get_autores = Autores.query.all()
    autor_schema = AutorSchema(many=True)
    autores = autor_schema.dump(get_autores)
    return make_response(jsonify(autores=autores))


@apigc.route('/autores', methods=['POST'])
def criar_autor():
    dados = request.get_json()
    get_autor = Autores('Nurul', ('Python', 'PHP'))
    get_autor.criar()
    autor_schema = AutorSchema()
    autores = autor_schema.load(get_autor)
    resultado = autor_schema.dump(autores.criar())
    return make_response(jsonify(autores=resultado))
