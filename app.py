from flask import Flask, render_template
from forms.messageforms import MessageForm
from messenger import Messenger

messenger = Messenger()
messages = []

app = Flask(__name__, template_folder='templates')

@app.route('/')
def getHome():
    return render_template('DebugPage.html', status=messenger.status())

@app.route('/sendmessage', methods=['GET', 'POST'])
def processMessage():
    form = MessageForm()
    if form.validate_on_submit():
        messages.append(form.message)
    return render_template('IMPage.html', messages = messages)

@app.route('/connect')
def connect():
    messenger.connect()
    return render_template('DebugPage.html', status = messenger.status())

@app.route('/disconnect')
def disconnect():
    messenger.disconnect()
    return render_template('DebugPage.html', status=messenger.status())

@app.route('/requestpage')
def send():
    result = messenger.getMainPage()
    return render_template('DebugPage.html', status = result)
