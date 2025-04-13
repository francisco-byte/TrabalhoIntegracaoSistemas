import grpc
from concurrent import futures
import produtos_pb2
import produtos_pb2_grpc
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

def salvar_dados(dados):
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f, indent=2)

class ProdutoService(produtos_pb2_grpc.ProdutoServiceServicer):
    def UpdateProduto(self, request, context):
        produtos = carregar_dados()
        for i, p in enumerate(produtos):
            if p['id'] == request.id:
                produtos[i] = {
                    'id': request.id,
                    'name': request.name,
                    'price': request.price,
                    'stock': request.stock
                }
                salvar_dados(produtos)
                return produtos_pb2.Resposta(mensagem="Produto atualizado com sucesso.")
        return produtos_pb2.Resposta(mensagem="Produto com ID não encontrado.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    produtos_pb2_grpc.add_ProdutoServiceServicer_to_server(ProdutoService(), server)
    server.add_insecure_port('[::]:8003')
    print("gRPC server online em porta 8003")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
