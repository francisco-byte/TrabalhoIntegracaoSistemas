from flask import Flask, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = '/shared/produtos.json'

def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f, indent=2)

@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
def deletar_produto(produto_id):
    produtos = carregar_dados()
    novos_produtos = [p for p in produtos if p["id"] != produto_id]
    if len(novos_produtos) == len(produtos):
        return jsonify({"error": "Produto não encontrado"}), 404
    salvar_dados(novos_produtos)
    return jsonify({"message": f"Produto {produto_id} deletado com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
