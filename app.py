from flask import Flask
from blueprints.endpoints import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run()
