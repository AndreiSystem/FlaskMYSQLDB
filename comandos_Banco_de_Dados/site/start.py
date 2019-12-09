from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

name_site = 'Site'


@app.route('/')
def home():
    return render_template('home.html', name=name_site)


@app.route('/login', methods=['POST', 'GET'])
def login():
    conn = MySQLdb.connect(host='mysql.topskills.study',
                           database='topskills05', user='topskills05', passwd='Andrei2019')
    cursor = conn.cursor()

    name = str(request.form['email'])
    password = str(request.form['password'])

    cursor.execute(
        f'SELECT * FROM registers WHERE email ="{name}" AND password = "{password}"')

    result = cursor.fetchone()
    try:
        if len(result) > 0:
            return 'logado'
    except Exception as erro:
        return 'Email ou Senha errado!'


app.run(debug=True)
