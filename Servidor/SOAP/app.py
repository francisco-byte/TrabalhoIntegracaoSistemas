from spyne import Application, rpc, ServiceBase, Integer, Unicode, Decimal
from spyne.protocol.soap import Soap11
from lxml import etree
import json
import os

DATA_FILE = '/shared/produtos.json'

def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f, indent=2)

class ProdutoService(ServiceBase):
    @rpc(Unicode, Integer, Decimal, Integer, _out_variable_name="produto", _returns=Unicode)
    def create_produto(ctx, name, id, price, stock):
        # Validar XML contra o XSD
        produto_xml = f"""
        <produto>
            <id>{id}</id>
            <name>{name}</name>
            <price>{price}</price>
            <stock>{stock}</stock>
        </produto>
        """
        
        with open('./servidor/soap/schema.xsd', 'r') as f:
            xsd_content = f.read()
        xsd_schema = etree.XMLSchema(etree.fromstring(xsd_content))
        xml_doc = etree.fromstring(produto_xml)
        
        try:
            xsd_schema.assertValid(xml_doc)
        except etree.DocumentInvalid as e:
            return f"Erro na validação XSD: {str(e)}"

        produto = {
            'id': id,
            'name': name,
            'price': price,
            'stock': stock
        }
        produtos = carregar_dados()
        produtos.append(produto)
        salvar_dados(produtos)
        
        return f"Produto {name} com ID {id} criado com sucesso!"

application = Application(
    [ProdutoService],
    tns='spyne.examples.produto',
    in_protocol=Soap11(),
    out_protocol=Soap11(),
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8002, application)
    server.serve_forever()
