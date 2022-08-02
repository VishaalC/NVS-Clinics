from flask import Flask, render_template, request, session
import os
from twilio.rest import Client
import sqlite3 as sql
import jinja2
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
account_sid = 'ACe9020837345b57ad970947e85ad6f004'
auth_token =  'aecd8e0110127ec82910a861a8fad19f'
client = Client(account_sid, auth_token)

Session(app)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@ app.route('/register.html')
def register():
    return render_template('register.html')


@ app.route('/success', methods=['POST'])
def success():
    f_name = request.form.get('f-name')
    l_name = request.form.get('l-name')
    email = request.form.get('email')
    passw = request.form.get('passw')
    addr = request.form.get('addr')
    num = request.form.get('num')

    with sql.connect('Database.db') as db:
        db.execute('''INSERT INTO patients
                    (f_name, l_name, email, passw, addr, num)
                    VALUES(?, ?, ?, ?, ?, ?)''',
                   (f_name, l_name, email, passw, addr, num))

    return render_template('success.html')


@ app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html')


@ app.route('/login-succ.html', methods=['POST'])
def login_success():
    if request.method == 'POST':
        email = request.form.get('email')
        passw = request.form.get('passw')
        session.permanent = False

        print(email)

        with sql.connect('Database.db') as db:
            passw_check = db.execute(
                "SELECT passw FROM patients WHERE email IN (?)", (email,))

        if passw == passw_check.fetchall()[0][0]:
            session['email'] = email
            return render_template('login-succ.html')
        else:
            return render_template('error.html')


@app.route('/appointment.html')
def appointment():
    if not session.get('email'):
        return render_template('login.html')
    else:
        return render_template('appoint.html')


@app.route('/booking-confirm', methods=['POST'])
def confirm():
    appt = request.form.get('appt')
    date = request.form.get('date')
    doc = request.form.get('doc')
    email = session.get('email')
    with sql.connect('Database.db') as db:
        num = db.execute(
            "SELECT num FROM patients WHERE email IN (?)", (email,))
    
    num_f = num.fetchall()[0][0]
    message = client.messages \
        .create(
            body=f'''Dear patient, Your appointment on {date} at {appt} with Dr.{doc} has been confirmed.
Kindly arrive a few minutes before the expected time.
Thank you.''',
            from_='+19703641899',
            to=f'+91{num_f}'
        )

    print(message.sid)
    return render_template('success.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
