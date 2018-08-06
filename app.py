import random
from flask import Flask
app = Flask(__name__)

k=0
@app.route('/')
def randomer():
    global k
    k=k+1
    return str(k)+' ==> Random number generated below 100 is:' + str(random.randint(1,101))
@app.route('/move')
def checker():
    return 'Redefined'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
