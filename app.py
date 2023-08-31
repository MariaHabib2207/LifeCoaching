from flask import Flask, render_template, request, flash, redirect,  url_for,session
import requests
from flask_mail import Mail, Message
import stripe
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime



# Create the Flask app instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['MAIL_SERVER']='smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'info@coachingstudiony.com'
app.config['MAIL_PASSWORD'] = 'XqDg9E2zWw70ZKrC'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
stripe.api_key = 'sk_test_51Nhx76L1PTlx4hpyJFwk2JxUkQdXXOTpIiEjkY2bOirQaAAISoBxIjszf0C8hyNH4BIwC1dEhUN4O9dukA7wE1TN00cMWvhPR3'
YOUR_DOMAIN = 'http://localhost:5000'
app.secret_key = 'your_secret_key_here'

##### appointment class ####################

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    status = db.Column(db.String)
    payment_status = db.Column(db.String)
    date =  db.Column(db.DateTime)

    # @app.route('/shop')
    # def shop():
    #     return render_template('shop.html')



###########send mail function ####################
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
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

###########send mail function ####################
def send_mail(method, email, full_name, message, subject):
    msg = Message(subject, sender='info@coachingstudiony.com', recipients=[email])
    msg.body = message
    mail.send(msg)
    
    if method == "checkout":
        # Call the create_checkout_session function after sending the email
        create_checkout_session()


# Route and view function for booking an appointment
@app.route('/create_appointment', methods=['POST'])
def create_appointment():
    full_name = request.form['full_name']
    email = request.form['email']
    date_str = request.form['date']
    if date_str:
        date = datetime.strptime(date_str, '%d / %B / %Y')
    else:
        date = datetime.now()

    new_appointment = Appointment(
        full_name=full_name,
        email=email,
        status="Pending",
        payment_status="Unpaid",
        date=date
    )

    db.session.add(new_appointment)
    db.session.commit()

    # Send email to user
    message = f"{full_name} Your appointment has been booked for {date}"
    subject = "Appointment Booked"
    method = "checkout"
    send_mail(method, email, full_name, message, subject)
    return create_checkout_session()




##### edit  appointment and admin view ####################

@app.route('/edit_appointment/<int:appointment_id>', methods=['GET', 'POST'])
def edit_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)

    if request.method == 'POST':
        appointment.full_name = request.form['full_name']
        appointment.email = request.form['email']
        appointment.status = request.form['status']
        appointment.payment_status = request.form['payment_status']
        
        db.session.commit()
        
        return redirect(url_for('admin_view'))
    
    return render_template('edit_appointment.html', appointment=appointment)

@app.route('/admin_view', methods=['GET', 'POST'])
def admin_view():
    if 'admin_authenticated' not in session or not session['admin_authenticated']:
        return redirect(url_for('login'))

    appointments = Appointment.query.all()

    if request.method == 'POST':
        # Handle delete and update actions
        if request.form['action'] == 'delete':
            appointment_id = int(request.form['appointment_id'])
            appointment = Appointment.query.get(appointment_id)
            if appointment:
                db.session.delete(appointment)
                db.session.commit()
        # Handle other actions like update
        return redirect(url_for('admin_view'))

    return render_template('admin_view.html', appointments=appointments)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'admin_authenticated' in session and session['admin_authenticated']:
        return redirect(url_for('admin_view'))

    if request.method == 'POST':
        # Perform authentication check (replace this with your actual authentication logic)
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '123456':
            session['admin_authenticated'] = True
            return redirect(url_for('admin_view'))
        else:
            error = True
            return render_template('login.html', error=error)

    return render_template('login.html')  # Create the login template



##### rendering main index page ####################
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')






# Define a route and view function for sending email

@app.route('/contact_us', methods=['POST'])
def contact_us():
    method = "contact"
    full_name = request.form['full_name']
    email = request.form['email']
    admin_email = "info@coachingstudiony.com"
    user_message = request.form['message']  # Corrected the key to 'message'
    for_message = f"Message from {email}, {user_message}"  # Corrected the message formatting
    subject = "Contact Us"
    msg = Message(subject, sender=email, recipients=[admin_email])
    msg.body = for_message
    mail.send(msg)
    return hello_world()




      
   ## redirect to checkout functionheckout

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
