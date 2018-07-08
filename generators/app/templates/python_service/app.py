import logging.config
import os

import flask
import flask_cors
import flask_restful_swagger_2

import config
from resources import health_check


cfg = config.Config()
resource_args = {}

app = flask.Flask(__name__)
flask_cors.CORS(app)

api = flask_restful_swagger_2.Api(
    app,
    title='<%= APP_NAME %> API',
    api_version=os.environ.get('VERSION', '1.0'),
    api_spec_url='/v1/docs/private'
)

api.add_resource(health_check.HealthCheck, '/v1/status', resource_class_kwargs=resource_args)
api.add_resource(flask_restful_swagger_2.create_swagger_endpoint(api.get_swagger_doc()), '/v1/docs/private')

logging.config.fileConfig('logger_config.ini', None, False)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=<%= PORT %>)
