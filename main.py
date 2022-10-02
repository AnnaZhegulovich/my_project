from flask import request, render_template, redirect, url_for
from form import MyForm
from models import app, db, Patients
import numpy as np
import pandas as pd
from tensorflow import keras
import os
import logging


logging.getLogger('tensorflow').disabled = True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


loaded_model = keras.models.load_model(r'_model.h5')#pickle.load(open('my_model.h5', 'rb'))


@app.route('/index', methods=['POST', 'GET'])
def index():
    form = MyForm(request.form)
    if request.method == 'POST':
        db.create_all()
        u = Patients(pressure_sist=form.pressure_sist.data, pressure_dia=form.pressure_dia.data,
                     breath=form.breath.data, pulse=form.pulse.data, iss=form.iss.data, glasgo=form.gsg.data)
        db.session.add(u)
        db.session.commit()
    return render_template('index.html', title='Form', form=form)


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        labels = ['1 степень', ' 2 степень', '3 степень', '4 степень']
        to_predict_list = list(map(int, request.form.values()))
        features_names = ['Pressure_sist', 'pressure_dia', 'breath', 'pulse', 'iss', 'glasgo']
        df = pd.DataFrame([to_predict_list], columns=features_names)
        array = df.values
        features_value = [np.array(array)]
        prediction = loaded_model.predict(features_value)
        prediction = np.argmax(prediction)
        if prediction == 1:
            rec = 'Тактика одномоментного оказания помощи.'
        elif prediction == 0:
            rec = 'Стабилизация состояния, тактика этапного оказания помощи.'
        elif prediction == 3:
            rec = 'Стабилизация состояния, тактика этапного оказания помощи.'
        else:
            rec = 'Тактитка этапного оказания помощи.'
        return render_template("result.html", data=labels[prediction], data2=rec)


@app.route('/')
def layout():
    return redirect(url_for('index'), code=302)
    #return render_template('layout.html')


@app.route('/about')
def about():
    return render_template('about.html', data="test")


@app.route('/sh')
def sh():
    return render_template('sh.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


if __name__ == "__main__":
    app.run(debug=True)
