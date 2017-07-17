from flask import Flask, render_template, request
import server_programming

app = Flask(__name__)

print(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    print(request.form)
    return render_template('index.html')

if(__name__ == '__main__'):
    app.run(debug=True)
