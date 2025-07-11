from flask import Blueprint, jsonify, current_app
import requests
import os

bp = Blueprint("routes", __name__)


@bp.route("/api-de-dados/pessoa-fisica/cpf", methods=["GET"])
def consulta_por_cpf():
    cpf = os.getenv("CPF")
    if not cpf:
        return jsonify({"error": "CPF não definido"}), 400

    api_url = f"https://api.gov.br/exemplo/pessoa-fisica?cpf={cpf}"

    headers = {"chave-api-dados": os.getenv("API_KEY_DADOS")}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Falha ao consultar a API"}), response.status_code


@bp.route("/api-de-dados/pessoa-fisica/nis", methods=["GET"])
def consulta_por_nis():
    nis = os.getenv("NIS")
    if not nis:
        return jsonify({"error": "NIS não definido"}), 400

    api_url = f"https://api.gov.br/exemplo/pessoa-fisica?nis={nis}"

    headers = {"chave-api-dados": os.getenv("API_KEY_DADOS")}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Falha ao consultar a API"}), response.status_code
