from flask import Flask, jsonify
from models import db
from config import Config
from sqlalchemy import text
from routes import routes
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)

swagger = Swagger(app)  # <- Very Important

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(routes)
@app.route('/routes', methods=['GET'])
def list_routes():
    """
    List All Available Routes
    ---
    tags:
      - Utility
    summary: Get all registered routes in the application
    responses:
      200:
        description: A list of all available API routes with methods
        schema:
          type: array
          items:
            type: object
            properties:
              endpoint:
                type: string
                description: The function name handling the route
              methods:
                type: string
                description: Allowed HTTP methods
              route:
                type: string
                description: URL path
    """
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        route_info = {
            'endpoint': rule.endpoint,
            'methods': methods,
            'route': str(rule)
        }
        output.append(route_info)
    return jsonify(output)
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
