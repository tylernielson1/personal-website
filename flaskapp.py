from flask import Flask, render_template, request, flash
from flask_mail imoport Mail, Message
from forms import ContactForm

app = Flask(__name__)
mail = Mail(app)
app.secret_key = 'dev_key'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'devemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'testtesttest'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=('GET', 'POST"'))
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message("You have a message from a visitor to your site: " + form.name.data,
                          sender='YourUser@NameHere',
                          recipients=['devemail@gmail.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True, form=form)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.route('/about')
def projects():
    return render_template('/projects.html')

@app.route('/blog')
def blog():
    return render_template('/blog.html')

@app.route('/resume')
def resume():
    return render_template('/resume.html')


if __name__ == '__main__':
    app.run()
