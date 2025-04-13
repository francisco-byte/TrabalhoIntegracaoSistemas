
import grpc
from concurrent import futures
import produtos_pb2
import produtos_pb2_grpc
import json
import os

DATA_FILE = '/shared/produtos.json'

class ProdutoServiceServicer(produtos_pb2_grpc.ProdutoServiceServicer):
    def UpdateProduto(self, request, context):
        produto = {
            'id': request.id,
            'name': request.name,
            'price': request.price,
            'stock': request.stock
        }
        produtos = carregar_dados()
        for i, p in enumerate(produtos):
            if p['id'] == request.id:
                produtos[i] = produto
                break
        else:
            produtos.append(produto)

        salvar_dados(produtos)

        return produtos_pb2.ProdutoResponse(message=f"Produto {request.name} atualizado com sucesso!")

def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f, indent=2)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    produtos_pb2_grpc.add_ProdutoServiceServicer_to_server(ProdutoServiceServicer(), server)
    server.add_insecure_port('[::]:5004')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()