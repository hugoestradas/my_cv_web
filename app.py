from flask import Flask, render_template, flash, redirect, url_for
from forms import ContactForm
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_email(form.name.data, form.email.data, form.message.data)
        flash('¡Gracias por tu mensaje! Te contactaré pronto.')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

def send_email(name, email, message):
    msg = MIMEText(f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}")
    msg['Subject'] = "Nuevo mensaje de contacto"
    msg['From'] = "tu_email@ejemplo.com"
    msg['To'] = "info@ingeniero.com"

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "tu_email@gmail.com"
    smtp_password = "tu_contraseña_de_aplicación"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)

