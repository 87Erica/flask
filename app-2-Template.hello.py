from flask import Flask, render_template
app = Flask(__name__)

#Example URL: http://127.0.0.1:5000/hello/John

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()