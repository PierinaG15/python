from flask import Flask,render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


#recibir parametros nombre y edad
@app.route('/saludo/<nombre>/<int:edad>')
def saludo(nombre,edad):
    return 'Hola, '+ nombre+'! tienes '+str(edad)+' años'

#login post
@app.route('/login',methods=['POST'])
def login():
   #obtener datos del formulario
   username= request.form['username']
   password= request.form['password']
   if (username=='admin' and password =='admin'):
        return redirect(url_for('admin'))
   else:
      return 'usuario o contraseña incorrectos'

@app.route('/admin',methods=['GET'])
def admin():
   return render_template("admin/admin.html")




#donde dice "prueba" es un (decorador) se puede llamar como yo quiera
@app.route('/saludo/<nombre>')
def prueba(nombre):
    return 'Hola, '+ nombre+'!'






if __name__ == '__main__':
    app.run(debug=True,port=80)
    
    



    
    