from flask import Flask, request
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'noebgqebrgwdfvlbdwif'

@app.route('/test/index')
def main():
    return json.loads('{"result" : "hello world"}')

@app.route('/test/hello_world', methods=('GET','POST'))
def second():
    res = {}
    res.update({"success" : "true"})
    res.update({"result" : "hello world"})
    res.update({"version" : "1.0"})
    res = json.dumps(res)
    return json.loads(res)

@app.route('/test/get_square', methods=['POST'])
def calculate_square():
    a = float(request.form.get('a'))
    h = float(request.form.get('h'))
    s = 0.5*(a*h)
    res = {}
    res.update({"success" : "true"})
    res.update({"result" : s})
    res.update({"version" : "1.0"})
    res = json.dumps(res)
    return json.loads(res)

if __name__ == "__main__":
    app.run(
        host='localhost',
        port=7589
    )
