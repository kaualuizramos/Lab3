from flask import Flask, render_template, request, jsonify
from frete import calcular_frete

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.get_json() or {}

    try:
        valor_carrinho = float(data.get("valor_carrinho", 0))
        regiao = str(data.get("regiao", "")).strip()

        # O frete base pode vir do form ou ser omitido para usar o padrão da região
        valor_frete_base = data.get("valor_frete_base")
        if valor_frete_base not in (None, "", "null"):
            valor_frete_base = float(valor_frete_base)
        else:
            valor_frete_base = None

        resultado = calcular_frete(valor_carrinho, regiao, valor_frete_base)
        return jsonify({"sucesso": True, "frete": resultado}), 200

    except ValueError as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 400
    except Exception:
        return jsonify({"sucesso": False, "erro": "Erro ao processar cálculo."}), 500

if __name__ == "__main__":
    app.run(debug=True)