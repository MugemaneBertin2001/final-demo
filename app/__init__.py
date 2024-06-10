import gzip
import os
import pickle
import joblib
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash

def create_app():
    app = Flask(__name__)
    app.secret_key = 'Mine'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/submit', methods=['POST'])
    def submit():
        form_data = request.form.to_dict()
        flash('Form submitted successfully!', 'success')
        
        # Convert form data to the list format for prediction
        to_predict_list = [
            int(form_data.get('paid_tuition_fees', 0)),
            int(form_data.get('admission_grade', 0)),
            int(form_data.get('age_at_admission', 0)),
            int(form_data.get('course', 0)),
            int(form_data.get('scholarship_holder', 0)),
            int(form_data.get('date_of_birth', 0)),
            int(form_data.get('gender', 0)),
            int(form_data.get('application_choice', 0)),
            int(form_data.get('displaced', 0)),
            int(form_data.get('debtor', 0)),
            int(form_data.get('marital_status', 0)),
            int(form_data.get('country_id', 0)),
            int(form_data.get('previous_qualification', 0)),
            int(form_data.get('has_special_needs', 0)),
            int(form_data.get('attendance_mode', 0))
        ]
    
        prediction = value_predictor(to_predict_list)
        form_data['prediction'] = prediction
        
        return redirect(url_for('submitted_info', **form_data))

    @app.route('/submitted_info')
    def submitted_info():
        form_data = request.args
        return render_template('submitted_info.html', form_data=form_data)

    return app

def value_predictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, -1)
    with open('app\\static\\model\\model.sav', 'rb') as model_file:
        loaded_model = joblib.load(model_file)
    result = loaded_model.predict(to_predict)
    return result[0]

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,port=499)
