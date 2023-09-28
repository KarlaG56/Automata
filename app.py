from flask import Flask, request, render_template

from automata import q0


app = Flask(__name__)


@app.route('/')
def render():
    return render_template('index.html')


@app.route('/automata', methods=['POST'])
def automata():
    data = request.get_json()
    cadena = data.get('cadena')

    return q0(cadena)


if __name__ == '__main__':
    app.run(debug=True)
