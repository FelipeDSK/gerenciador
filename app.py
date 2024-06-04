from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tarefas = []

@app.route('/')
def index():
    tarefas_ordenadas = sorted(tarefas, key=lambda x: (datetime.strptime(x['data'], '%Y-%m-%d'), x['hora']))
    return render_template('index.html', tarefas=tarefas_ordenadas)

@app.route('/add_tarefa', methods=['POST'])
def add_tarefa():
    descricao = request.form.get('descricao')
    data = request.form.get('data')
    hora = request.form.get('hora')
    tarefas.append({'descricao': descricao, 'data': data, 'hora': hora, 'concluida': False})
    return redirect(url_for('index'))

@app.route('/remover_tarefa/<int:tarefa_id>', methods=['POST'])
def remover_tarefa(tarefa_id):
    del tarefas[tarefa_id]
    return redirect(url_for('index'))

@app.route('/concluir_tarefa/<int:tarefa_id>', methods=['POST'])
def concluir_tarefa(tarefa_id):
    tarefas[tarefa_id]['concluida'] = True
    return redirect(url_for('index'))

@app.route('/desmarcar_tarefa/<int:tarefa_id>', methods=['POST'])
def desmarcar_tarefa(tarefa_id):
    tarefas[tarefa_id]['concluida'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

