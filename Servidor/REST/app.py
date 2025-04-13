from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

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

@app.route('/create', methods=['POST'])
def create_produto():
    produto = request.json
    produtos = carregar_dados()

    # Evita produtos com o mesmo ID
    if any(p['id'] == produto['id'] for p in produtos):
        return jsonify({'erro': 'ID já existente'}), 400

    produtos.append(produto)
    salvar_dados(produtos)
    return jsonify({'mensagem': f"Produto {produto['name']} criado com sucesso!"})

if __name__ == '__main__':
    app.run(port=8001)
