from flask import Flask, jsonify
from graphene import ObjectType, String, Int, Float, List, Schema
from graphene import Field
import json
import os

app = Flask(__name__)

DATA_FILE = '/shared/produtos.json'

# Modelo do Produto
class Produto(ObjectType):
    id = Int()
    name = String()
    price = Float()
    stock = Int()

# Consultar produtos
class Query(ObjectType):
    produtos = List(Produto)

    def resolve_produtos(self, info):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

# Criar o schema
schema = Schema(query=Query)

@app.route('/graphql', methods=['POST'])
def graphql_server():
    from graphene import gql
    from flask_graphql import GraphQLView

    return GraphQLView.as_view('graphql', schema=schema)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
