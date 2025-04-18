from flask import Flask, jsonify
from models import db
from config import Config
from sqlalchemy import text
from routes import routes
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(routes)
@app.route('/')
def health_check():
    try:
        # Quick DB connectivity check
        db.session.execute(text('SELECT 1'))
        db_status = 'up'
    except Exception as e:
        db_status = f'down ({str(e)})'

    return jsonify({
        "status": "ok" if db_status == 'up' else 'db error',
        "database": db_status
    })
if __name__ == '__main__':
    app.run(debug=True)
