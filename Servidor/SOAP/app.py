from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json
import os

# Caminho para o arquivo 'produtos.json' na pasta 'shared'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Caminho da pasta onde o script está
SHARED_DIR = os.path.join(BASE_DIR, '..', 'shared')  # Pasta 'shared'
DATA_FILE = os.path.join(SHARED_DIR, 'produtos.json')

def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

class ProdutoReadService(ServiceBase):
    @rpc(_returns=Unicode)
    def read_all(ctx):  # Mudado de 'read_produtos' para 'read_all'
        produtos = carregar_dados()
        return json.dumps(produtos)

application = Application([ProdutoReadService],
    tns='spyne.examples.readproduto',
    in_protocol=Soap11(),
    out_protocol=Soap11(),
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8002, wsgi_app)
    print("SOAP server online em http://localhost:8002")
    server.serve_forever()
