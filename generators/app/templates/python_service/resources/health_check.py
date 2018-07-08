import logging
from http import HTTPStatus

from flask_restful_swagger_2 import Resource, swagger

import swagger_docs


class HealthCheck(Resource):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(self.__class__.__name__)

    @swagger.doc(swagger_docs.docs['health_check']['get'])
    def get(self):
        '''Get the status of the <%= APP_NAME %>.'''

        self.logger.info('get HealthCheck')
        return {"msg": "<%= APP_NAME %> is up and running."}
