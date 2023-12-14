from flask import Flask,render_template, request,redirect,session,flash

app = Flask(__name__)
app.secret_key = "Senai"
class cadInfluencer:
    def __init__(self,nome,social,seguidor,area):
        self.nome = nome
        self.social = social
        self.seguidor = seguidor
        self.area = area


lista = []

@app.route('/Influencer')
def Influencer():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Influencer.html',Titulo = "Influencers Iniciais:",ListaInfluencer = lista)

@app.route('/cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Cadastro.html', Titulo = "Cadastro de Influencer")

@app.route("/criar", methods= ["POST"])
def criar():
    if "salvar" in request.form:
        nome = request.form["nome"]
        social = request.form["social"]
        seguidor = request.form["seguidor"]
        area = request.form["area"]
        obj = cadInfluencer(nome, social, seguidor, area)
        lista.append(obj)
        return redirect('/Influencer')
    elif "deslogar" in request.form:
        session.clear()
        return redirect('/')

@app.route('/excluir/<nomeinflu>', methods=['GET','DELETE'])
def excluir(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            lista.pop(i)
            break
    return redirect('/Influencer')

@app.route('/editar/<nomeinflu>', methods=['GET'])
def editar(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            return render_template('Editar.html', influencer = influ, titulo="Alterar influencer")

@app.route('/alterar', methods=['POST', "PUT"])
def alterar():
    nome = request.form['nome']
    for i, influ in enumerate(lista): # o request acessa as informações do formulário
        if influ.nome == nome:
            influ.nome = request.form['nome']
            influ.social = request.form['social']
            influ.seguidor = request.form['seguidor']
            influ.area = request.form['area']
    return  redirect('/Influencer')

@app.route('/')
def login():
    session.clear()#limpa tudo que tem
    return render_template('Login.html', Titulo= "Faça seu login")

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form["usuario"] == "Agatha" and request.form ["senha"]=="123":
        session["Usuario_Logado"] = request.form["usuario"]
        flash("usuario logado com sucesso")#flash é basicamente uma mensagem
        return redirect("/cadastro")
    else:
        flash("usuario nao encontrado")
        return redirect("/")

if __name__ == '__main__':
    app.run()