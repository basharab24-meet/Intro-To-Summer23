from flask import Flask,render_template
import random

app = Flask(__name__,
template_folder='templetes',
static_folder='static')


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/fortune')
def fortune():
    future=["millions","marrage","no job","kids","divorse","9-5 job","elite athlete","MEET instructor","a trip around the world","free PC"]
    f= random.choice(future)
    return render_template("fortune.html", f=f)



if __name__ == '__main__':
    app.run(debug = True)


'''
@app.route('/your fortune is.../<string:future>')
def hello_name_route(name):
    return render_template(
        'future.html', f = millions)
'''