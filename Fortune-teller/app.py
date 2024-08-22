from flask import Flask,render_template,url_for,redirect,request
import random

app = Flask(__name__,
template_folder='templetes',
static_folder='static')


@app.route('/home', methods=["POST","GET"])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        birthday = request.form['birthday']
        print(birthday)
        return redirect(url_for('fortune',
            b = birthday))



@app.route('/fortune/<b>',methods=["POST","GET"])
def fortune(b):
    future=["millions","marrige","no job","kids","divorse","9-5 job","elite athlete","MEET instructor","a trip around the world","free PC"]
    f= random.choice(future) 
    len_b=len(b)
    if len_b > 10:
        return render_template("home.html")
    print(len_b)
    fortune_final=future[len_b]
    return render_template("fortune.html", f=fortune_final)



if __name__ == '__main__':
    app.run(debug = True)


'''
@app.route('/your fortune is.../<string:future>')
def hello_name_route(name):
    return render_template(
        'future.html', f = millions)
'''