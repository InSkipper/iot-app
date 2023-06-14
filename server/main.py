from . import db
from .models import Data
from flask import render_template, redirect, url_for, request, session, Blueprint
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def root():
    return redirect(url_for('main.index'))


@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/devices', methods=['GET'])
@login_required
def devices():
    return render_template('device.html', login=current_user.login)


@main.route('/devices/station', methods=['GET'])
def station():
    return render_template('station.html')


@main.route('/devices/security', methods=['GET'])
@login_required
def security():
    return render_template('device_security.html')


@main.route('/devices/weatherStation', methods=['GET'])
@login_required
def weatherStation():
    return render_template('device_weatherStation.html')


@main.route('/devices/greenhouse', methods=['GET'])
@login_required
def greenhouse():
    return render_template('device_greenhouse.html')


# Ппереписать, очень сильно плохо (
@main.route('/devices/greenhouse/getTemperature', methods=['GET'])
@login_required
def get_temperature():
    last = Data.query.order_by(Data.id.desc()).first()
    temp = last.temperature
    hum = last.humidity
    return render_template('data_iframe.html', data=f"{round(temp, 2)}°C\n{round(hum, 2)}%")


@main.route('/devices/greenhouse/getPressure', methods=['GET'])
@login_required
def get_pressure():
    press = Data.query.order_by(Data.id.desc()).first().pressure
    return render_template('data_iframe.html', data=f"{round(press, 2)}Па")


@main.route('/devices/greenhouse/getHumidity', methods=['GET'])
@login_required
def get_humidity():
    hum = Data.query.order_by(Data.id.desc()).first().humidity
    return render_template('data_iframe.html', data=f"{round(hum, 2)}%")


@main.route('/devices/greenhouse/getCo2', methods=['GET'])
@login_required
def get_co2():
    co2 = Data.query.order_by(Data.id.desc()).first().co2
    return render_template('data_iframe.html', data=f"{round(co2, 2)}ppm")
