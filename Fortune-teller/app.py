from flask import Flask,render_template,url_for,redirect,request
import random
from flask import session as session

app = Flask(__name__,
template_folder='templetes',
static_folder='static')

app.config['SECRET_KEY'] = "my_key"

@app.route('/home', methods=["POST","GET"])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        birthday = request.form['birthday']
        print(birthday)
        return redirect(url_for('fortune',
            b = birthday))



@app.route('/fortune',methods=["POST","GET"])
def fortune():
    future=["millions","marrige","no job","kids","divorse","9-5 job","elite athlete","MEET instructor","a trip around the world","free PC"]
    f= random.choice(future) 
    len_b=len(session['birthM'])
    if len_b > 10:
        return render_template("home.html")
    print(len_b)
    fortune_final=future[len_b]
    return render_template("fortune.html", f=fortune_final)

@app.route('/',methods=["POST","GET"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        name = request.form['name']
        birthM = request.form['birth_month']
        session['name']=name 
        session['birthM']=birthM
        print(session)
        return redirect('/home')




if __name__ == '__main__':
    app.run(debug = True)


'''
@app.route('/your fortune is.../<string:future>')
def hello_name_route(name):
    return render_template(
        'future.html', f = millions)
'''