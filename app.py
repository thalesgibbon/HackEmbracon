#!flask/bin/python
from flask import Flask, request, jsonify
from CategorizaDream import CategorizaDream
from PontuacaoDream import PontuacaoDream
from AtualizaSaldo import AtualizaSaldo
from SaldoUser import SaldoUser


app = Flask(__name__)


@app.route('/CategorizaDream', methods=['GET'])
def index():
    dicio = {}
    if 'descricao' in request.args:
        d = request.args['descricao']
        cd = CategorizaDream(d)
        resulto = cd.resultado
        pontos = PontuacaoDream(resulto).resultado
        dicio['status'] = "ok"
        result = {}
        result['resultado'] = resulto
        result['pontos'] = pontos
        dicio['result'] = result
    else:
        dicio['status'] = "error"
        dicio['result'] = "Esta faltando o campo descricao."
    return jsonify(dicio)


@app.route('/AtualizaPontuacao', methods=['GET'])
def index2():
    dicio = {}
    if 'user_id' in request.args and 'pontos' in request.args:
        u = request.args['user_id']
        p = request.args['pontos']
        saldo = AtualizaSaldo(u, p)
        dicio['status'] = saldo.status
    else:
        dicio['status'] = "error"
    return jsonify(dicio)


@app.route('/SaldoUser', methods=['GET'])
def index3():
    dicio = {}
    if 'user_id' in request.args:
        u = request.args['user_id']
        saldo = SaldoUser(u)
        dicio['status'] = "ok"
        dicio['result'] = {'saldo_atual': saldo.saldo_atual}
    else:
        dicio['status'] = "error"
        dicio['result'] = "Esta faltando o campo user_id ou pontos."
    return jsonify(dicio)


if __name__ == '__main__':
    app.run(debug=True)
