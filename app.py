from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')


from pages.assignment10.assignment10 import assignment10  
app.register_blueprint(assignment10)


from components.base.base import base
app.register_blueprint(base)


if __name__ == '__main__':
    app.run(debug=True)

