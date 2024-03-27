from flask import Flask, request, jsonify, render_template
from wtforms import Form, StringField, TextAreaField, validators
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'senhatop123'
app.config['MYSQL_DB'] = 'bdftt'

conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)
cursor = conn.cursor()

class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

    def to_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "link_imagem": self.link_imagem,
            "programa": self.programa,
            "animador": self.animador
        }
class CharacterForm(Form):
    nome = StringField("Nome", validators=[validators.DataRequired()])
    descricao = TextAreaField("Descrição", validators=[validators.DataRequired()])
    link_imagem = StringField("Link da Imagem")
    programa = StringField("Programa")
    animador = StringField("Animador")

@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')
@app.route("/add_character", methods=["GET", "POST"])
def add_character():
    if request.method == "POST":
        form = CharacterForm(request.form)
        if form.validate():
            try:
                sql = "INSERT INTO personagens (nome, descricao, link_imagem, programa, animador) VALUES (%s, %s, %s, %s, %s)"
                values = (form.nome.data, form.descricao.data, form.link_imagem.data, form.programa.data, form.animador.data)
                cursor.execute(sql, values)
                conn.commit()
                return jsonify("Personagem criado com sucesso!"), 201
            except mysql.connector.Error as err:
                return jsonify(f"Erro ao criar personagem: {err}"), 500
        else:
            return jsonify(form.errors), 400
    else:
        form = CharacterForm()
        return render_template("character_form.html", form=form)
@app.route("/characters/", methods=["GET"])
def listar_personagens():
    try:
        cursor.execute("SELECT * FROM personagens")
        rows = cursor.fetchall()
        personagens = [Personagem(*row[1:]) for row in rows]
        return render_template("character_list.html", personagens=personagens)
    except mysql.connector.Error as err:
        return jsonify(f"Erro ao listar personagens: {err}"), 500
@app.route("/clear_characters", methods=["POST"])
def limpar_personagens():
    try:
        cursor.execute("DELETE FROM personagens")
        conn.commit()
        return jsonify("Lista de personagens limpa com sucesso!"), 200
    except mysql.connector.Error as err:
        return jsonify(f"Erro ao limpar a lista de personagens: {err}"), 500

if __name__ == "__main__":
    app.run(debug=True)
