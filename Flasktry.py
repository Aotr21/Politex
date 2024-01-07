from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('Code_Basics_бесплатные_курсы_программирования,_обучение_CodeBasics.html')


@app.route('/about')
def about():
    return 'ХУЙ ПИЗДА ГАВНО СОБАКА'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: '+ name + '-' + str(id)






if __name__ =='__main__':
    app.run(debug=True)