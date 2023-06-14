import datetime
import requests
from datetime import datetime, timezone

from flask import Blueprint, request, render_template
from flask_login import current_user, login_required

from . import db
from .models import Data

hub = Blueprint("hub", __name__)


@hub.route('/api/set-hub', methods=['GET'])
@login_required
def set_hub():
    hub_ip = request.args.get('hub_ip')

    if not hub_ip:
        return f"Invalid ip: {hub_ip}", 400

    current_user.hub_ip = hub_ip
    db.session.commit()

    return f"Hub ip address set successfully: {current_user.hub_ip}", 200


@hub.route('/greenhouse/event', methods=['POST'])
@login_required
def greenhouse_event():
    name = request.form.get("name")
    event = request.form.get("event")

    res = requests.post(f'http://{current_user.hub_ip}:80/api', json={'module_name': name, "event": event})
    return render_template('data_iframe.html', data=res.text), res.status_code


@hub.route('/data', methods=['POST'])
def handle_data():
    content = request.json
    temp = content['temperature']
    press = content['pressure']
    hum = content['humidity']
    co2 = content['co2']

    time = datetime.utcnow()

    new_data = Data(temperature=temp, pressure=press, humidity=hum, co2=co2, time=time)
    db.session.add(new_data)
    db.session.commit()

    return "Ok", 200
