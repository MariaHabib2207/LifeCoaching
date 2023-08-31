from flask import Flask, render_template, request, flash, redirect
import requests
from flask_mail import Mail, Message
import stripe
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the Flask app instance
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['MAIL_SERVER']='smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'mariahabib2219@gmail.com'
app.config['MAIL_PASSWORD'] = 'jdUq7VgnB2fcTJhS'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
stripe.api_key = 'sk_test_51Nhx76L1PTlx4hpyJFwk2JxUkQdXXOTpIiEjkY2bOirQaAAISoBxIjszf0C8hyNH4BIwC1dEhUN4O9dukA7wE1TN00cMWvhPR3'
YOUR_DOMAIN = 'http://localhost:5000'
app.secret_key = 'your_secret_key_here'

# Define a route and a view function
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    email= request.form['email']

    response = requests.post(
        'https://api.mailgun.net/v3/sandboxce97a1b98496416d9f26ad2772e878ff.mailgun.org/messages',
        auth=("api", "3e2df77fa300f4e6a5c090d66663f14c-f0e50a42-307e6b08"),
        data={
            "from": "Excited User <mariahabib2219@gmail.com>",
            "to": email,
            "subject": "Contact",
            "text": f"Your appointment has been booked"
        },
        verify=False
        )
        
    if response.status_code == 200:
            flash("Email Sent")
    else:
            flash("Email Sending Failed")
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1Nk35wL1PTlx4hpyhQqi3S1j',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )

    except Exception as e:
        return str(e)



    return redirect(checkout_session.url, code=303)


# Define a route and view function for sending email
@app.route('/send-mail', methods=['POST'])
def send_mail():
    full_name = request.form['full_name']
    message = request.form['address']
    msg = Message('Hello from the other side!', sender =   'mariahabib2219@gmail.com', recipients = ['mariahabib2219@gmail.com'])
    msg.body = "hey, sending out email from flask!!!"
    mail.send(msg)
    try:
        response = requests.post(
            'https://api.mailgun.net/v3/sandboxce97a1b98496416d9f26ad2772e878ff.mailgun.org/messages',
            auth=("api", "3e2df77fa300f4e6a5c090d66663f14c-f0e50a42-307e6b08"),
            data={
                "from": "Excited User <mariahabib2219@gmail.com>",
                "to": ["mariahabib2219@gmail.com"],
                "subject": "Contact",
                "text": f"Email form: {full_name}, Message - {message}"
            },
            verify=False
        )
        
        if response.status_code == 200:
            flash("Email Sent")

    except Exception as e:
        flash("An error occurred while sending the email")
    
    return render_template('index.html')

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
 
    return redirect('/checkout')
 
      
   ## redirect to checkout functionheckout

# Run the app
if __name__ == '__main__':
    app.run()
