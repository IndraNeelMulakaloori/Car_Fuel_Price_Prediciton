from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def result():
    distance = request.form['distance']
    return render_template('result.html',distance=distance)
if __name__ == '__main__':
    app.run(debug=True)