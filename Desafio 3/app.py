from flask import Flask , render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config["MYSQL_Host"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "PASSWORD_HERE"
app.config["MYSQL_DB"] = "unes"


db = MySQL(app) 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contato', methods = ["POST","GET"])
def contato():

    if request.method == "POST" :
        try:

            email = request.form['email']


            assunto = request.form['subject']


            descricao = request.form['description']


            if email == '' or assunto  == '' or descricao == '':

                 return render_template('contato.html', status = 'Erro algum dos campos está vazio')

            cursor =  db.connection.cursor()
            

            cursor.execute(f"insert into  contatos (email, assunto, descricao) values ('{email}', '{assunto}', '{descricao}')")
            
            db.connection.commit() 

            cursor.close()
            
            return render_template('contato.html', status = 'Sucesso')
        except ValueError:
            return render_template('contato.html', status = 'Erro')
    else:
        return render_template('contato.html')


@app.route('/users')
def user():
        cursor = db.connection.cursor()
        users = cursor.execute("select * from contatos")
        if users > 0:
            userInfo = cursor.fetchall()
            return render_template('users.html', userInfo = userInfo)
        else:
            return render_template('users.html')