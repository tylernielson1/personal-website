from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

class ContactForm(Form):
    name = StringField('Name:', [validators.Required()])
    email = StringField('Email:', [validators.Required(), validators.Email('your@email.com')])
    message = TextAreaField('Message:', [validators.Required()])
    submit = SubmitField('Send')


def CheckNameLength(form, field):
    if len(field.data) < 4:
        raise ValidationError('Name must have more than 3 characters')