from flask import Flask, render_template

# Create the Flask app instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return  render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run()
