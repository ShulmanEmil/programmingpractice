from flask import Flask
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'noebgqebrgwdfvlbdwif'

@app.route('')
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

if __name__ == "__main__":
    app.run(
        host='localhost',
        port=7589
    )
