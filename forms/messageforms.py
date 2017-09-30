from flask_wtf import Form
from wtforms import StringField, BooleanField, TextField
from wtforms.validators import DataRequired, NumberRange

class MessageForm(Form):
    message = StringField('message', [DataRequired()])