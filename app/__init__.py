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
        print('Form Data Submitted:', form_data)
        flash('Form submitted successfully!', 'success')

        return redirect(url_for('submitted_info', **form_data))

    @app.route('/submitted_info')
    def submitted_info():
        form_data = request.args
        return render_template('submitted_info.html', form_data=form_data)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
