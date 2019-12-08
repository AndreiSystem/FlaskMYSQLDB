from flask import Flask, render_template, request, redirect
from class_Pessoa import Person_DB


app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('home.html')


@app.route('/listagem')
def listagem():
    start = Person_DB()
    list_now = start.get_to_list()
    return render_template('listagem.html', list_return=list_now)


@app.route('/editar')
def editar():
    id = request.args['id']
    start = Person_DB()
    person_id = start.search_for_id(id)
    return render_template('editar.html', person=person_id)


@app.route('/excluir')
def excluir():
    id = request.args['id']
    start = Person_DB()
    delete_id = start.delete(id)
    return redirect('/listagem')


@app.route('/salvar_editar', methods=['POST'])
def editar_salvar():
    id = request.form['id']
    name = request.form['name']
    last_name = request.form['last_name']
    cpf = request.form['cpf']

    person = Person_DB(name, last_name, cpf, id)
    person.changedata_for_id(id)
    return redirect('/listagem')


@app.route('/cadastrar')
def register():
    return render_template('formulario.html')


@app.route('/salvar', methods=['POST'])
def save():
    name = request.form['name']
    last_name = request.form['last_name']
    cpf = request.form['cpf']
    start = Person_DB()
    register = start.register(name, last_name, cpf)
    return redirect('/listagem')


app.run(debug=True)
