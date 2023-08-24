from flask import Flask, render_template, request, flash
import requests
from flask_mail import Mail, Message

# Create the Flask app instance
app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mariahabib2219@gmail.com'
app.config['MAIL_PASSWORD'] = 'sarkaar2207?'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Define a route and a view function
@app.route('/')
def hello_world():
    return render_template('index.html')
    
# Define a route and view function for sending email
@app.route('/send-mail', methods=['POST'])
def send_mail():
    full_name = request.form['full_name']
    message = request.form['address']
    
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
        else:
            flash("Email Sending Failed")
    except Exception as e:
        flash("An error occurred while sending the email")
    
    return render_template('index.html')

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    full_name = request.form['full_name']
    email = request.form['email']
    phone = request.form['phone']
    
    try:
        response = requests.post(
            'https://api.mailgun.net/v3/sandboxce97a1b98496416d9f26ad2772e878ff.mailgun.org/messages',
            auth=("api", "3e2df77fa300f4e6a5c090d66663f14c-f0e50a42-307e6b08"),
            data={
                "from": "Excited User <mariahabib2219@gmail.com>",
                "to": ["mariahabib2219@gmail.com"],
                "subject": "Appointment Booked",
                "text": f"Appointment has been booked for user: {full_name} with email {email} and contact number {phone} for confirmation"
            },
            verify=False
        )
        
        if response.status_code == 200:
            flash("Appointment Email Shared")
        else:
            flash("Email Sending Failed")
    except Exception as e:
        flash("An error occurred while sending the email")
    
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run()
