# import Flask
from flask import Flask

# Create an aoo, being able to pass __name__
app = Flask(__name__)


# Create a function
@app.route('/')
def hello_world():
    return 'Hello world'

if __name__== "__main__":
    app.run(debug=True)