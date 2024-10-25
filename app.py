from flask import Flask, render_template

from auth.routes import auth_bp
from config import connection_string, check_db_connection
from extensions import db  # Nhập db từ extensions.py

app = Flask(__name__)

# Register db
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init SQLAlchemy
db.init_app(app)

# check connect
check_db_connection()


@app.route('/')
def index():
    return render_template('index.html')


# Register Blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

print(f"main: {__name__}")

if __name__ == '__main__':
    print("ok,,,,")
    app.run(debug=True, port=8080)
