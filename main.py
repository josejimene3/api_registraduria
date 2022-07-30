from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from waitress import serve
from controllers.candidateController import CandidateController
from controllers.tableController import TableController
from controllers.resultController import ResultController
from controllers.partyController import PartyController
import pymongo
import certifi


app = Flask(__name__)
cors = CORS(app)
party_controller = PartyController()
candidate_controller = CandidateController()
table_controller = TableController()
result_controller = ResultController()

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://jajimenez:jajimenez@cluster0.ufffl4d.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
print(client)
db = client.test
print(db)
university_bd = client["db_project_votes"]
print(university_bd.list_collection_names())


def load_file_config():
    with open("config.json") as archivo:
        data = json.load(archivo)
    return data


"""
---------------------------
    ENDPOINTS PARTY
--------------------------
"""


@app.route("/parties", methods=['GET'])
def get_parties():
    response = party_controller.index()
    return jsonify(response)


@app.route("/party/<string:id>", methods=['GET'])
def get_party(id):
    response = party_controller.show(id)
    return jsonify(response)


@app.route("/party", methods=['POST'])
def create_party():
    info = request.get_json()
    response = party_controller.create(info)
    return jsonify(response)


@app.route("/party/<string:id>", methods=['PUT'])
def update_party(id):
    info = request.get_json()
    response = party_controller.update(id, info)
    return jsonify(response)


@app.route("/party/<string:id>", methods=["DELETE"])
def delete_party(id):
    response = party_controller.delete(id)
    return jsonify(response)


"""
---------------------------
    ENDPOINTS CANDIDATE
--------------------------
"""


@app.route("/candidates", methods=['GET'])
def get_candidates():
    response = candidate_controller.index()
    return jsonify(response)


@app.route("/candidate/<string:id>", methods=['GET'])
def get_candidate(id):
    response = candidate_controller.show(id)
    return jsonify(response)


@app.route("/candidate/party/<string:id_party>", methods=['POST'])
def create_candidate(id_party):
    info = request.get_json()
    response = candidate_controller.create(info, id_party)
    return jsonify(response)


@app.route("/candidate/<string:id>/party/<string:id_party>", methods=['PUT'])
def update_candidate(id, id_party):
    info = request.get_json()
    response = candidate_controller.update(id, info, id_party)
    return jsonify(response)


@app.route("/candidate/<string:id>", methods=["DELETE"])
def delete_candidate(id):
    response = candidate_controller.delete(id)
    return jsonify(response)


"""
---------------------------
    ENDPOINTS TABLE
--------------------------
"""


@app.route("/tables", methods=['GET'])
def get_tables():
    response = table_controller.index()
    return jsonify(response)


@app.route("/table", methods=['POST'])
def create_table():
    info = request.get_json()
    response = table_controller.create(info)
    return jsonify(response)


@app.route("/table/<string:id>", methods=['GET'])
def get_table(id):
    response = table_controller.show(id)
    return jsonify(response)


@app.route("/table/<string:id>", methods=['PUT'])
def update_table(id):
    info = request.get_json()
    response = table_controller.update(id, info)
    return jsonify(response)


@app.route("/table/<string:id>", methods=["DELETE"])
def delete_table(id):
    response = table_controller.delete(id)
    return jsonify(response)


"""
---------------------------
    ENDPOINTS RESULT
--------------------------
"""


@app.route("/results", methods=["GET"])
def get_results():
    response = result_controller.index()
    return jsonify(response)


@app.route("/result", methods=["GET"])
def get_result(id):
    response = result_controller.show(id)
    return jsonify(response)


@app.route("/result/table/<string:id_table>/candidate/<string:id_candidate>", methods=["POST"])
def create_result(id_table, id_candidate):
    info_result = request.get_json()
    response = result_controller.create(info_result, id_table, id_candidate)
    return jsonify(response)


@app.route("/result/<string:id>/table/<string:id_table>/candidate/<string:id_candidate>", methods=["PUT"])
def update_result(id, id_table, id_candidate):
    info_result = request.get_json()
    response = result_controller.update(id, info_result, id_table, id_candidate)
    return jsonify(response)


@app.route("/result/<string:id>", methods=["DELETE"])
def delete_result(id):
    response = result_controller.delete(id)
    return jsonify(response)


@app.route("/result/party/<string:id_party>", methods=["GET"])
def get_result_by_party(id_party):
    response = result_controller.find_by_party(id_party)
    return jsonify(response)


"""
---------------------------
    ENDPOINTS REPORTS
--------------------------
"""


@app.route("/result/votesxcandidates", methods=["GET"])
def get_result_total_votesxcandidates():
    response = result_controller.total_votes_candidate()
    return jsonify(response)


@app.route("/result/votesxcandidates/table/<string:id_table>", methods=["GET"])
def get_result_total_votesxcandidates_table(id_table):
    response = result_controller.total_votes_candidate_table(id_table)
    return jsonify(response)


@app.route("/result/votesxtables", methods=["GET"])
def get_result_total_votesxtables():
    response = result_controller.total_votes_tables()
    return jsonify(response)


@app.route("/result/votesxtable/<string:id_table>", methods=["GET"])
def get_result_total_votesxtable(id_table):
    response = result_controller.total_votes_table(id_table)
    return jsonify(response)


@app.route("/result/votesxparties", methods=["GET"])
def get_result_total_votesxparties():
    response = result_controller.total_votes_parties()
    return jsonify(response)


@app.route("/result/votesxparty/table/<string:id_table>", methods=["GET"])
def get_result_total_votesxparty(id_table):
    response = result_controller.total_votes_party(id_table)
    return jsonify(response)


dataConfig = load_file_config()
url = "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"])
print("Server running ", url)
serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])


