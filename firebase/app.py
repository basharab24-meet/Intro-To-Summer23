from flask import Flask, render_template, request, redirect, url_for
from flask import session
import pyrebase
from flask_cors import CORS



firebaseConfig = {
  'apiKey': "AIzaSyAjr5JaJ1V4g41E0Zimh04ZkVNrzEQxDJA",
  'authDomain': "authentication-lab-60fb0.firebaseapp.com",
  'projectId': "authentication-lab-60fb0",
  'storageBucket': "authentication-lab-60fb0.appspot.com",
  'messagingSenderId': "469954462227",
  'appId': "1:469954462227:web:2d483b5cfae6436f79f5e6",
  'databaseURL':"https://authentication-lab-60fb0-default-rtdb.europe-west1.firebasedatabase.app"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"]=" MY_KEY "
CORS(app)

@app.route("/", methods=["POST","GET"])
def signup():
  error = ""
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    fullname = request.form['fullname']
    username = request.form['username']
    user = {"fullname" : fullname,"username" : username, "email" : email}
    session['email']=email
    session['password']=password
    try:
      session['user'] = auth.create_user_with_email_and_password(email, password)
      UID = session['user']['localId']
      db.child("Users").child(UID).set(user)

      return redirect(url_for("home"))
    except Exception as e:
      return render_template("signup.html")
      print(e)
  else:
    return render_template("signup.html")
  
@app.route("/home", methods=["POST","GET"])
def home():
  print('in home')
  if request.method =="POST":
    print('in if')
    quote = request.form['quote']
    print(quote)
    who = request.form['who']
    quote ={'text': quote, 'who': who}
    UID = session['user']['localId']
    db.child("quotes").child(UID).set(quote)
    # if 'quotes' not in session:
    # session['quotes'] = [" "]
    # session['quotes'].append(quote)
    # else:
    #   session['quotes'].append(quote)
    # print(session)
    return render_template('thanks.html')
  else:
    return render_template("home.html")
  return render_template("home.html")


@app.route("/signin", methods=["POST","GET"])
def signin():
  if request.method =='POST':
    email = request.form['email']
    password = request.form['password']
    try:
      session['user']= auth.sign_in_with_email_and_password(email,password)
      return redirect(url_for('home'))
    except Exception as e:
      error= "Authentication Failed"
      print(e)
      return render_template("signin.html")
  else:
    print('hi')
    return render_template("signin.html")


@app.route("/thanks", methods=["POST","GET"])
def thanks():
  return render_template("thanks.html")

@app.route("/display", methods=["POST","GET"])
def display():
  print('in display:', session)
  quotes = session['quotes']

  print(quotes)
  return render_template('display.html', quotes=quotes)

@app.route("/signout", methods=["POST","GET"])
def signout():
  session['user'] = None
  session['quotes']= ['']
  # session.pop()
  auth.current_user = None
  return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug = True)