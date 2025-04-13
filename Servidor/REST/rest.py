from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError
from jsonpath_ng import parse
import json
import os

app = Flask(__name__)

# Carregar schema
with open('.\Servidor\Rest\schema.json') as f:
    schema = json.load(f)

# Dados persistentes
DATA_FILE = 'produtos.json'

def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f, indent=2)

@app.route('/produtos', methods=['POST'])
def criar_produto():
    try:
        data = request.get_json()
        validate(instance=data, schema=schema)
        produtos = carregar_dados()
        produtos.append(data)
        salvar_dados(produtos)
        return jsonify({"message": "Produto criado com sucesso!"}), 201
    except ValidationError as e:
        return jsonify({"error": f"Validação falhou: {e.message}"}), 400

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = carregar_dados()
    return jsonify(produtos), 200

@app.route('/produtos/jsonpath', methods=['GET'])
def consultar_por_jsonpath():
    produtos = carregar_dados()
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Parâmetro 'query' é obrigatório"}), 400
    try:
        jsonpath_expr = parse(query)
        resultado = [match.value for match in jsonpath_expr.find(produtos)]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
