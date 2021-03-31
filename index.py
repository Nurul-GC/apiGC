"""
script principal do projecto
para executa-lo basta navegar ate a localização atual do script
e digitar no terminal:
*** linux ***
    ~$: python3 ./index.py
*** windows ***
    C:/localizacao/do/script/> py index.py
"""

# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************

from app import app
from app.routes import apigc

app.register_blueprint(apigc)

if __name__ == '__main__':
    app.run(debug=True)
