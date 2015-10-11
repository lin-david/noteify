from flask import Flask
from flask import request
from flask import render_template
from main import main

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/noteified', methods=['POST'])
def my_form_post():

    f = open('input.txt', 'w')
    f.truncate()
    f.write(request.form['text'])
    f.close()
    html_file = open('templates/page.html', 'w')
    html_file.truncate()
    html_file.write(main())
    html_file.close()
    return render_template('page.html')


if __name__ == '__main__':
    app.run()
