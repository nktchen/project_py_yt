from flask import Flask
import requests

api_key = 'PgEf8hGaSPHXDdhZOGx1fM6DgwA1HhiA'

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask hi"

if __name__ == '__main__':
    app.run(debug=True)
