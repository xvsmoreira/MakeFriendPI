from flask import Flask, render_template, request, url_for, flash, redirect, send_file, send_from_directory
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
from flask import flash

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foto = db.Column(db.String)
    nome = db.Column(db.String, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    historia = db.Column(db.Text, nullable=False)
    tutor = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)
    cep = db.Column(db.String, nullable=False)
    rua = db.Column(db.String, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String)
    bairro = db.Column(db.String, nullable=False)
    cidade = db.Column(db.String, nullable=False)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/doeseupet", methods=('GET', 'POST'))
def doeseupet():
    if request.method == 'POST':
        foto = request.files['foto']
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto.filename))
        pet = Pets(nome=request.form['nome'],
                   idade=request.form['idade'],
                   historia=request.form['historia'],
                   tutor=request.form['tutor'],
                   telefone=request.form['telefone'],
                   cep=request.form['cep'],
                   rua=request.form['rua'],
                   numero=request.form['numero'],
                   complemento=request.form['complemento'],
                   bairro=request.form['bairro'],
                   cidade=request.form['cidade'],
                   foto=foto.filename)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('index', success=True))
    return render_template('doeseupet.html')

@app.route("/adote")
def adote():
    pets = Pets.query.all()
    return render_template("adote.html", pets=pets)

@app.route('/pet/<int:pet_id>')
def view_pet(pet_id):
    pet = Pets.query.get_or_404(pet_id)
    return render_template('adotar.html', pet=pet)

@app.route('/image/<path:filename>')
def servir_imagem(filename):
    """Serve image files from the UPLOAD_FOLDER directory."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/excluir_pet/<int:pet_id>', methods=['POST'])
def excluir_pet(pet_id):
    pet = Pets.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    flash('Pet excluído com sucesso!')
    return redirect(url_for('adote'))

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route('/filtro')
def filtro():
    pets = Pets.query.all()
    cidade = request.args.get('cidade')
    if cidade:
        pets_filtrados = [pet for pet in pets if pet.cidade == cidade]
    else:
        pets_filtrados = pets
    
    cidades_dict = {}
    for pet in pets:
        if pet.cidade not in cidades_dict:
            cidades_dict[pet.cidade] = []
        cidades_dict[pet.cidade].append(pet)
    
    cidades = list(cidades_dict.keys())
    cidades.sort()  
    
    return render_template('filtro.html', pets=pets_filtrados, cidades=cidades)

if __name__ == '__main__':
    app.run(debug=True)
