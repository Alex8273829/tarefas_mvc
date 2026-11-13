from flask import Flask, redirect, render_template, request, url_for
from flask.config import T
 
from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa
 
app = Flask(__name__)
with app.app_context():
    init_db()
@app.route('/test')
def test():
    return "Servidor Online!"
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method== 'POST':
        titulo_form= request.form['tituloTarefa']
        data_form= request.form['dataConclusao']
        data_corrigida= data_form or None
 
        tarefa= Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)
        tarefa.salvasTarefa()
 
        return redirect(url_for('home'))
 
    tarefas= Tarefa.listarTarefas()
    return render_template(
        'base.html',
        titulo_da_pagina ='Minha lista de tarefas',
        tarefas_da_pagina = tarefas
        )
@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    Tarefa.apagarTarefa(id)
    return redirect(url_for('home'))
@app.route('/', methods=['GET', 'POST'])
def editar(id):
    tarefa= Tarefa.buscarTarefaPorId(id)
 
    if request.method== 'POST':
        titulo_form= request.form['tituloTarefa']
        data_form= request.form['dataConclusao'] or None
 
        tarefa.titulo= titulo_form
        tarefa.data_conclusao= data_form
        tarefa.editarTarefa()
       
        return redirect(url_for('home'))
   
    return render_template(
        'base.html',
        titulo_da_pagina='Editar Tarefa',
        tarefa= tarefa
    )
 
if __name__ == "__main__":
    app.run()
tem menu de contexto