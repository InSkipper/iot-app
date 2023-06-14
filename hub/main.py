import datetime

from . import db
from .models import Modules

from flask import request, Blueprint
import requests

main = Blueprint("main", __name__)


# @main.route("/api")
# def test():
#     return "OK", 200


@main.route("/api/add-module", methods=['POST'])
def add_module():
    content = request.json
    ip = content['local_ip']

    module = Modules.query.filter_by(ip=ip).first()
    if module:
        return "Module already exists", 400

    new_module = Modules(ip=content['local_ip'], name=content['name'])
    db.session.add(new_module)
    db.session.commit()

    return "Module added", 200


@main.route("/api", methods=['POST'])
def send_request():
    content = request.json
    module_name = content["module_name"]
    event = content["event"]

    module = Modules.query.filter_by(name=module_name).first()
    if not module:
        return "Check modules' name", 404

    res = requests.get(
        f'http://{module.ip}/{event}')  # TODO: send json, if useful: .../change-status', json=content['event'])

    return res.text, res.status_code


@main.route("/data", methods=['POST'])
def greenhouse_data():
    content = request.json

    res = requests.post(f"http://127.0.0.1:5000/data", json=content)

    return content, res.status_code
